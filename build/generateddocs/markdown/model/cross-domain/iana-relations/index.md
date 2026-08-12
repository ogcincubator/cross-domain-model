
# IANA link relations vocabulary (Model)

`ogc.model.cross-domain.iana-relations` *v1.0.0*

IANA link relation terms (e.g. `cite-as`, RFC 8574) for marking preferred citation targets and other link semantics.

[*Status*](http://www.opengis.net/def/status): Under development

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: IANA link relations vocabulary
description: 'Unconstrained carrier schema: this block''s content is its JSON-LD context,
  not a data shape. The schema exists only so other blocks can `$ref` it via `bblocks://`
  and inherit the context.'
type: object
x-jsonld-extra-terms:
  cite-as: http://www.iana.org/assignments/relation/cite-as

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/cross-domain-model/build/annotated/model/cross-domain/iana-relations/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/cross-domain-model/build/annotated/model/cross-domain/iana-relations/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "cite-as": "http://www.iana.org/assignments/relation/cite-as",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://ogcincubator.github.io/cross-domain-model/build/annotated/model/cross-domain/iana-relations/context.jsonld)

## Sources

* [IANA Link Relations registry](http://www.iana.org/assignments/relation/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/cross-domain-model](https://github.com/ogcincubator/cross-domain-model)
* Path: `_sources/iana-relations`

