"""
Materializes the rdf:type triples that PROV-O's own rdfs:domain/rdfs:range axioms imply
but that this block's shapes.shacl deliberately does not require locally (see that
file's header comment on the open-world, by-reference-typing relaxation).

Given a Turtle graph valid against ../shapes.shacl (which only checks sh:class on
blank-node values), this applies RDFS entailment -- via pySHACL's own `inference`
option, i.e. the SHACL "entailment regime" pySHACL's shapes-graph validation shapes
name but never itself executes for the data graph (see shapes.shacl's header for why
this had been left undone until now) -- against the graph merged with the live PROV-O
ontology, then keeps only the original triples plus any newly-entailed prov:* rdf:type
statements about nodes already present in the input. The result is validated (see
transforms.yaml's `outputs.profiles`) against ../../prov-strict, whose shapes require
sh:class for every value described in the graph, exempting only values with no
outgoing triples of their own. This entailment step matters even so: it types every
PROV object-property value from the property assertion alone, regardless of local
description, so a value that would otherwise only pass via that "not described"
exemption ends up genuinely, explicitly typed instead.
"""
import urllib.request

import pyshacl
import rdflib
from rdflib import RDF, Namespace, URIRef, BNode

PROV = Namespace("http://www.w3.org/ns/prov#")
PROV_O_URL = "https://www.w3.org/ns/prov-o#"

data_graph = rdflib.Graph()
data_graph.parse(data=input_data, format="turtle")

original_triples = set(data_graph)
original_nodes = {
    term for triple in original_triples for term in (triple[0], triple[2])
    if isinstance(term, (URIRef, BNode))
}

with urllib.request.urlopen(
    urllib.request.Request(PROV_O_URL, headers={"Accept": "text/turtle"})
) as resp:
    ontology_ttl = resp.read()

working_graph = rdflib.Graph()
for triple in original_triples:
    working_graph.add(triple)
working_graph.parse(data=ontology_ttl, format="turtle")

# inference='rdfs' is pySHACL's RDFS entailment regime; inplace=True materializes the
# inferred triples directly into working_graph instead of only reporting on them.
pyshacl.validate(data_graph=working_graph, shacl_graph=None, inference="rdfs",
                  inplace=True, advanced=True)

result_graph = rdflib.Graph()
for prefix, namespace in data_graph.namespaces():
    result_graph.bind(prefix, namespace, override=True)
for triple in original_triples:
    result_graph.add(triple)
for node in original_nodes:
    for entailed_type in working_graph.objects(node, RDF.type):
        if str(entailed_type).startswith(str(PROV)):
            result_graph.add((node, RDF.type, entailed_type))

output_data = result_graph.serialize(format="turtle")
