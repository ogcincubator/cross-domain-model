
# PAV vocabulary (Model)

`ogc.model.cross-domain.pav` *v1.0.0*

Provenance, Authoring and Versioning (PAV) terms for import/retrieval provenance (`importedFrom`, `importedOn`, `importedBy`, `retrievedFrom`, `retrievedOn`, `retrievedBy`). Complements PROV-O, which this register already covers separately.

[*Status*](http://www.opengis.net/def/status): Under development

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: PAV vocabulary
description: 'Unconstrained carrier schema: this block''s content is its JSON-LD context,
  not a data shape. The schema exists only so other blocks can `$ref` it via `bblocks://`
  and inherit the context.'
type: object
x-jsonld-extra-terms:
  importedFrom: http://purl.org/pav/importedFrom
  importedOn: http://purl.org/pav/importedOn
  importedBy: http://purl.org/pav/importedBy
  retrievedFrom: http://purl.org/pav/retrievedFrom
  retrievedOn: http://purl.org/pav/retrievedOn
  retrievedBy: http://purl.org/pav/retrievedBy

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/cross-domain-model/build/annotated/model/cross-domain/pav/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/cross-domain-model/build/annotated/model/cross-domain/pav/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "importedFrom": "http://purl.org/pav/importedFrom",
    "importedOn": "http://purl.org/pav/importedOn",
    "importedBy": "http://purl.org/pav/importedBy",
    "retrievedFrom": "http://purl.org/pav/retrievedFrom",
    "retrievedOn": "http://purl.org/pav/retrievedOn",
    "retrievedBy": "http://purl.org/pav/retrievedBy",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://ogcincubator.github.io/cross-domain-model/build/annotated/model/cross-domain/pav/context.jsonld)

## Sources

* [Provenance, Authoring and Versioning (PAV) ontology](https://pav-ontology.github.io/pav/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/cross-domain-model](https://github.com/ogcincubator/cross-domain-model)
* Path: `_sources/pav`

