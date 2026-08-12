
# Dublin Core Terms vocabulary (Model)

`ogc.model.cross-domain.dcterms` *v1.0.0*

DCMI Metadata Terms used across metadata models (`conformsTo`, `Standard`, etc.).

[*Status*](http://www.opengis.net/def/status): Under development

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: Dublin Core Terms vocabulary
description: 'Unconstrained carrier schema: this block''s content is its JSON-LD context,
  not a data shape. The schema exists only so other blocks can `$ref` it via `bblocks://`
  and inherit the context.'
type: object
x-jsonld-extra-terms:
  conformsTo: http://purl.org/dc/terms/conformsTo
  Standard: http://purl.org/dc/terms/Standard

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/cross-domain-model/build/annotated/model/cross-domain/dcterms/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/cross-domain-model/build/annotated/model/cross-domain/dcterms/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "conformsTo": "http://purl.org/dc/terms/conformsTo",
    "Standard": "http://purl.org/dc/terms/Standard",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://ogcincubator.github.io/cross-domain-model/build/annotated/model/cross-domain/dcterms/context.jsonld)

## Sources

* [DCMI Metadata Terms](http://purl.org/dc/terms/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/cross-domain-model](https://github.com/ogcincubator/cross-domain-model)
* Path: `_sources/dcterms`

