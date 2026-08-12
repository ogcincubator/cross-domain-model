
# GeoSPARQL (Model)

`ogc.model.cross-domain.geosparql` *v0.1*

GeoSPARQL Core (1.1). Simply wraps the published GeoSPARQL ontology with a Building Block to allow examples, default JSON-LD context, SHACL rules and transforms to be easily discovered.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

## GeoSPARQL

Wraps the [GeoSPARQL](http://www.opengis.net/ont/geosparql) ontology, currently providing a JSON-LD
context for `Geometry` and `asWKT`. Extend as further terms are needed by consumers.

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: GeoSPARQL
description: 'Unconstrained carrier schema: this block''s content is its JSON-LD context,
  not a data shape. The schema exists only so other blocks can `$ref` it via `bblocks://`
  and inherit the context.'
type: object
x-jsonld-extra-terms:
  Geometry: http://www.opengis.net/ont/geosparql#Geometry
  asWKT: http://www.opengis.net/ont/geosparql#asWKT

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/cross-domain-model/build/annotated/model/cross-domain/geosparql/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/cross-domain-model/build/annotated/model/cross-domain/geosparql/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "Geometry": "http://www.opengis.net/ont/geosparql#Geometry",
    "asWKT": "http://www.opengis.net/ont/geosparql#asWKT",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://ogcincubator.github.io/cross-domain-model/build/annotated/model/cross-domain/geosparql/context.jsonld)

## Sources

* [OGC GeoSPARQL](http://www.opengis.net/ont/geosparql)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/cross-domain-model](https://github.com/ogcincubator/cross-domain-model)
* Path: `_sources/geosparql`

