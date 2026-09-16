#!/usr/bin/env python3
"""
Maintenance script (not part of the published block) -- regenerates shapes.shacl's
OWL-derived section from the live W3C PROV-O ontology.

Requires: rdflib (`pip install rdflib`)
Run from this directory:  python3 generate-shapes.py

What it does
------------
Fetches https://www.w3.org/ns/prov-o (content-negotiated Turtle) and derives SHACL
shapes from its OWL axioms, following the rule *categories* documented by
sparna-git/owl2shacl (https://github.com/sparna-git/owl2shacl, itself an adaptation of
TopQuadrant's "From OWL to SHACL in an automated way"):

  - rdfs:domain  -> sh:property attached to the domain class's NodeShape,
                    and to every rdfs:subClassOf* descendant of that class
                    (datatype properties only -- see "Object properties" below)
  - rdfs:range (object property)   -> sh:class on the property's value
  - rdfs:range (datatype property) -> sh:datatype on the PropertyShape

Why not just run owl2shacl directly: its ruleset is SHACL-AF (sh:rule /
sh:SPARQLRule) and calls a TopBraid-only SPARQL extension function
(owl2sh-open:getPropertyShape) -- it only runs inside TopBraid or the
hosted SHACL Play converter (https://shacl-play.sparna.fr/play/convert),
not under an open-source engine such as pySHACL. This script re-implements
the same conversion categories directly with rdflib instead.

Deliberately NOT generated here (left to the curated, canonical
CDO-Shapes-PROV-O library, https://github.com/Cyber-Domain-Ontology/CDO-Shapes-PROV-O,
should this block ever need it again -- not currently declared in bblock.json's
shaclShapes):
  - the 4 owl:disjointWith class-pairs (Activity/Entity,
    ActivityInfluence/EntityInfluence, Agent/InstantaneousEvent,
    Entity/InstantaneousEvent)
  - the 1 owl:Restriction (ActivityInfluence: maxCardinality 0 on
    prov:hadActivity)

Datatype properties (unchanged design)
---------------------------------------
Still attached to sh:targetClass-based NodeShapes propagated down the
rdfs:subClassOf* hierarchy, exactly as before: a plain, reliable use of core
SHACL (sh:datatype) reached via sh:property.

Object properties: sh:class checking, and when it's skipped
--------------------------------------------------------------
A blank-node value is only checked against sh:class when it actually carries an
rdf:type -- if a type is given, it must be the right one, but a blank node is never
*required* to carry one. This is deliberately generic about everything else on the
node: ogc-na-tools' own generated PROV output (see e.g. icsm-vocabs' `*.ttl`
provenance footers) points at an activity tracked elsewhere via a bare
`[ dcterms:identifier "..." ]` blank node, but nothing here is keyed to
dcterms:identifier specifically, or to having exactly one triple, or any triple at
all -- a blank node with any number of properties, using any predicates, naming any
number of other things, is just as exempt as long as none of those predicates is
rdf:type. Other implementations may use a completely different vocabulary to leave
the same kind of breadcrumb (schema:identifier, skos:notation, a bare rdfs:label,
nothing at all); this rule doesn't need to recognise the pattern, only the absence of
a positive, checkable type claim. A plain IRI value is exempt for the same reason as
ever: it is a by-reference pointer to an object described elsewhere, and PROV-O's
rdfs:domain/rdfs:range axioms make its type real without this graph needing to
restate it locally (the semantically correct fix -- an entailment-aware validator --
is a separate concern; see ogc.model.cross-domain.prov-strict and this block's
`entail` transform).

Each object property therefore gets its own standalone NodeShape: a custom
`sh:target` (SPARQL-based) that selects every blank-node value belonging to a subject
of the property's own rdfs:domain (or a descendant thereof, same propagation as
datatype properties below -- this preserves the exact set of subjects this file
already checked before the rewrite that introduced this target, rather than widening
enforcement to untyped/differently-typed subjects as a side effect), plus a
`sh:sparql` constraint that reports a violation only for a value that *has* an
rdf:type and it isn't one of the property's range classes. This shape is
intentionally NOT reached via sh:targetClass/sh:property from a domain-class
NodeShape the way datatype properties are (nor expressed with sh:or): pySHACL (as
vendored by bblocks-postprocess, see its `shacl_validate()`) has two independent bugs
that silently turn a real violation into "no violation" instead of raising or
actually validating:

  1. A `sh:sparql`/`sh:closed`/`sh:property` constraint used as a *value shape*
     (reached via sh:or, sh:node, or sh:property from another shape's own
     sh:targetClass/sh:targetNode) is not evaluated against the correct focus node --
     only sh:class/sh:datatype/sh:nodeKind (the constraint types this file already
     relied on) are reliable there. A shape must declare its own top-level sh:target,
     and its sh:sparql constraint must be attached directly (not as an sh:or
     alternative), for anything more complex to actually run.
  2. Inside a `sh:sparql` SPARQLConstraint (but not a SPARQLTarget's own query), pySHACL
     appears to substitute $this textually rather than via a proper variable binding:
     $this used as a bare function argument (e.g. `isBlank($this)`) breaks silently
     when $this is a blank node, because a blank node's N3 label is not valid SPARQL
     syntax in an expression position -- only $this used inside a triple pattern
     (including within FILTER (NOT) EXISTS {...}) is reliable. A SPARQLTarget's own
     `?this`, by contrast, is bound by ordinary query execution, not substitution, so
     functions like `isBlank(?this)` there are unaffected -- which is why the
     blank/domain-gating logic below lives in the target query (using isBlank(?this)
     freely) while the constraint query below only ever uses $this inside triple
     patterns / FILTER (NOT) EXISTS {...} blocks, never as a bare function argument.

Output: overwrites shapes.shacl in this directory. Re-run whenever PROV-O itself is
revised; do not hand-edit the generated shapes below the header comment (hand edits
will be lost on the next run).
"""
import urllib.request

import rdflib
from rdflib import OWL, RDFS, RDF
from rdflib.collection import Collection
from rdflib.namespace import XSD

PROV_O_URL = "https://www.w3.org/ns/prov-o#"
LOCAL_CACHE = "prov-o.ttl"

HEADER = """# SHACL shapes for the W3C PROV-O ontology (http://www.w3.org/ns/prov#),
# mechanically derived from PROV-O's OWL axioms (rdfs:domain / rdfs:range
# per property, propagated down rdfs:subClassOf hierarchies for datatype
# properties).
#
# Generated by generate-shapes.py in this directory -- see that script's
# module docstring for the full rationale, the owl2shacl rule categories it
# follows, and -- importantly -- why object-property shapes below use a
# standalone sh:target (SPARQLTarget) rather than the sh:targetClass +
# sh:property structure still used for datatype properties. Do not hand-edit
# below this header; re-run the script instead.
#
# NOT covered here (left to the curated CDO-Shapes-PROV-O library,
# https://github.com/Cyber-Domain-Ontology/CDO-Shapes-PROV-O, not currently
# declared in bblock.json's shaclShapes):
#   - the 4 owl:disjointWith class-pairs
#   - the 1 owl:Restriction (ActivityInfluence: maxCardinality 0 on
#     prov:hadActivity)
#
# A blank-node object-property value is only sh:class-checked when it actually
# carries an rdf:type -- a blank node with any other content, using any predicates,
# is never *required* to be typed, exactly like a plain IRI value (a by-reference
# pointer to an object described elsewhere, per PROV-O's own open-world semantics).
# If a type IS given, it must be one of the property's range classes. See the script
# docstring for the two pySHACL evaluation quirks that make a standalone sh:target
# plus a direct (non-sh:or) sh:sparql constraint the only reliable way to express
# this.

@prefix sh:   <http://www.w3.org/ns/shacl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@base <https://www.ogc.org/rules/prov/> .

"""

XSD_TYPES = {
    XSD.dateTime, XSD.date, XSD.string, XSD.anyURI, XSD.boolean,
    XSD.integer, XSD.decimal, XSD.double, XSD.float,
}

OBJECT_TARGET_TEMPLATE = """
            PREFIX prov: <http://www.w3.org/ns/prov#>
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
            SELECT ?this
            WHERE {{
                ?s prov:{name} ?this .
                {domain_filter}
                FILTER isBlank(?this)
            }}
        """

# A violation only when $this HAS a type and that type isn't (a subclass of) one of
# the property's range classes -- an untyped value, whatever else it carries, is
# never flagged. $this only ever appears inside triple patterns / FILTER (NOT)
# EXISTS {{}} blocks here, never as a bare function argument -- see the module
# docstring's pySHACL quirk #2 for why that distinction matters.
OBJECT_CONSTRAINT_TEMPLATE = """
            PREFIX prov: <http://www.w3.org/ns/prov#>
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
            SELECT $this
            WHERE {{
                FILTER EXISTS {{ $this rdf:type ?bblocksType }}
                {mismatch_filters}
            }}
        """


def fetch_ontology():
    req = urllib.request.Request(PROV_O_URL, headers={"Accept": "text/turtle"})
    with urllib.request.urlopen(req) as resp:
        data = resp.read()
    with open(LOCAL_CACHE, "wb") as f:
        f.write(data)
    return LOCAL_CACHE


def local(uri):
    return uri.split('#')[-1]


def main():
    import os
    src = LOCAL_CACHE if os.path.exists(LOCAL_CACHE) else fetch_ontology()

    g = rdflib.Graph()
    g.parse(src, format="turtle")

    def resolve(node):
        """Resolve a class expression node (URIRef or owl:unionOf blank node) to named class IRIs."""
        if isinstance(node, rdflib.URIRef):
            return {node}
        out = set()
        for lst in g.objects(node, OWL.unionOf):
            for member in Collection(g, lst):
                out |= resolve(member)
        return out

    all_classes = {c for c in g.subjects(RDF.type, OWL.Class) if isinstance(c, rdflib.URIRef)}

    direct_sub = {}
    for s, o in g.subject_objects(RDFS.subClassOf):
        if isinstance(s, rdflib.URIRef) and isinstance(o, rdflib.URIRef):
            direct_sub.setdefault(o, set()).add(s)

    def descendants(c):
        seen = {c}
        stack = [c]
        while stack:
            cur = stack.pop()
            for sub in direct_sub.get(cur, ()):
                if sub not in seen:
                    seen.add(sub)
                    stack.append(sub)
        return seen

    def render_object_property_shape(prop):
        name = local(prop)
        range_classes = set()
        for r in g.objects(prop, RDFS.range):
            range_classes |= resolve(r)
        range_classes &= all_classes
        if not range_classes:
            return None

        # Same domain resolution as datatype properties: gate the target to subjects
        # whose own asserted type is the property's rdfs:domain or a descendant of it,
        # so this rewrite doesn't widen *which subjects* get checked as a side effect
        # of fixing what counts as a violation for the ones that already were.
        domain_classes = set()
        for d in g.objects(prop, RDFS.domain):
            domain_classes |= resolve(d)
        domain_classes &= all_classes
        if not domain_classes:
            return None
        domain_alts = " UNION ".join(
            f"{{ ?s rdf:type/rdfs:subClassOf* prov:{local(dc)} }}" for dc in sorted(domain_classes)
        )
        domain_filter = domain_alts if len(domain_classes) == 1 else f"{{ {domain_alts} }}"

        mismatch_filters = "\n                ".join(
            f"FILTER NOT EXISTS {{ $this rdf:type/rdfs:subClassOf* prov:{local(rc)} }}"
            for rc in sorted(range_classes)
        )
        range_names = ", ".join(f"prov:{local(rc)}" for rc in sorted(range_classes))

        target_query = OBJECT_TARGET_TEMPLATE.format(name=name, domain_filter=domain_filter)
        constraint_query = OBJECT_CONSTRAINT_TEMPLATE.format(mismatch_filters=mismatch_filters)
        lines = [
            f"<#prop-{name}>",
            "    a sh:NodeShape ;",
            f"    rdfs:isDefinedBy prov:{name} ;",
            "    sh:target [",
            "        a sh:SPARQLTarget ;",
            f'        sh:select """{target_query}""" ;',
            "    ] ;",
            "    sh:sparql [",
            "        a sh:SPARQLConstraint ;",
            f'        sh:message "When typed, prov:{name}\'s value must be one of: {range_names}." ;',
            f'        sh:select """{constraint_query}""" ;',
            "    ] ;",
        ]
        lines[-1] = lines[-1].rstrip(' ;') + " ."
        return "\n".join(lines)

    def render_datatype_property_shape(prop):
        name = local(prop)
        domain_classes = set()
        for d in g.objects(prop, RDFS.domain):
            domain_classes |= resolve(d)
        domain_classes &= all_classes

        lines = [f"<#prop-{name}>", "    a sh:PropertyShape ;", f"    sh:path prov:{name} ;",
                 f"    rdfs:isDefinedBy prov:{name} ;"]
        for r in g.objects(prop, RDFS.range):
            if r in XSD_TYPES:
                lines.append(f"    sh:datatype xsd:{local(r)} ;")
                break
        lines[-1] = lines[-1].rstrip(' ;') + " ."
        return "\n".join(lines), domain_classes

    obj_props = sorted(set(g.subjects(RDF.type, OWL.ObjectProperty)))
    data_props = sorted(set(g.subjects(RDF.type, OWL.DatatypeProperty)))

    object_shape_lines = []
    for p in obj_props:
        shape = render_object_property_shape(p)
        if shape is not None:
            object_shape_lines.append(shape)

    class_props = {c: set() for c in all_classes}
    datatype_shape_lines = []
    for p in data_props:
        text, domain_classes = render_datatype_property_shape(p)
        datatype_shape_lines.append(text)
        for d in domain_classes:
            for target in descendants(d):
                class_props.setdefault(target, set()).add(f"prop-{local(p)}")

    node_shape_lines = []
    for c in sorted(all_classes, key=local):
        props = class_props.get(c, set())
        if not props:
            continue
        name = local(c)
        lines = [f"<#{name}-shape>", "    a sh:NodeShape ;", f"    sh:targetClass prov:{name} ;"]
        prop_refs = " , ".join(f"<#{p}>" for p in sorted(props))
        lines.append(f"    sh:property {prop_refs} ;")
        lines[-1] = lines[-1].rstrip(' ;') + " ."
        node_shape_lines.append("\n".join(lines))

    attached = set()
    for props in class_props.values():
        attached |= props
    datatype_shape_lines = [t for t in datatype_shape_lines if t.split('\n', 1)[0].strip('<#>') in attached]

    with open("shapes.shacl", "w", encoding="utf-8") as f:
        f.write(HEADER)
        f.write("\n\n".join(node_shape_lines))
        f.write("\n\n")
        f.write("\n\n".join(datatype_shape_lines))
        f.write("\n\n")
        f.write("\n\n".join(object_shape_lines))
        f.write("\n")

    print(f"wrote shapes.shacl: {len(node_shape_lines)} node shapes, "
          f"{len(datatype_shape_lines)} datatype property shapes, "
          f"{len(object_shape_lines)} object property shapes")


if __name__ == "__main__":
    main()
