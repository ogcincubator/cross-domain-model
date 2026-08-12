
# PCDM vocabulary (Model)

`ogc.model.cross-domain.pcdm` *v1.0.0*

Portland Common Data Model terms for describing repositories and collections of digital objects (`RepositoryObject`, `RepositoryCollection`, `RepositoryFile`, `hasMember`, `hasFile`).

[*Status*](http://www.opengis.net/def/status): Under development

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: PCDM vocabulary
description: 'Unconstrained carrier schema: this block''s content is its JSON-LD context,
  not a data shape. The schema exists only so other blocks can `$ref` it via `bblocks://`
  and inherit the context.'
type: object
x-jsonld-extra-terms:
  hasFile: http://pcdm.org/models#hasFile
  hasMember: http://pcdm.org/models#hasMember
  RepositoryCollection: http://pcdm.org/models#Collection
  RepositoryObject: http://pcdm.org/models#Object
  RepositoryFile: http://pcdm.org/models#File

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/cross-domain-model/build/annotated/model/cross-domain/pcdm/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/cross-domain-model/build/annotated/model/cross-domain/pcdm/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "hasFile": "http://pcdm.org/models#hasFile",
    "hasMember": "http://pcdm.org/models#hasMember",
    "RepositoryCollection": "http://pcdm.org/models#Collection",
    "RepositoryObject": "http://pcdm.org/models#Object",
    "RepositoryFile": "http://pcdm.org/models#File",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://ogcincubator.github.io/cross-domain-model/build/annotated/model/cross-domain/pcdm/context.jsonld)

## Sources

* [Portland Common Data Model (PCDM)](https://pcdm.org/2016/04/18/models)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/cross-domain-model](https://github.com/ogcincubator/cross-domain-model)
* Path: `_sources/pcdm`

