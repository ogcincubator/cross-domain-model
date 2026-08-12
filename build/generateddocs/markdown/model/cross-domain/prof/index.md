
# PROF vocabulary (Model)

`ogc.model.cross-domain.prof` *v1.0.0*

W3C Profiles Vocabulary (PROF) terms for describing resource profiles and their roles.

[*Status*](http://www.opengis.net/def/status): Under development

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: PROF vocabulary
description: 'Unconstrained carrier schema: this block''s content is its JSON-LD context,
  not a data shape. The schema exists only so other blocks can `$ref` it via `bblocks://`
  and inherit the context.'
type: object
x-jsonld-extra-terms:
  hasArtifact: http://www.w3.org/ns/dx/prof/hasArtifact
  hasResource: http://www.w3.org/ns/dx/prof/hasResource
  hasRole: http://www.w3.org/ns/dx/prof/hasRole
  hasToken: http://www.w3.org/ns/dx/prof/hasToken
  isProfileOf: http://www.w3.org/ns/dx/prof/isProfileOf
  ResourceDescriptor: http://www.w3.org/ns/dx/prof/ResourceDescriptor
  ResourceRole: http://www.w3.org/ns/dx/prof/ResourceRole
  Profile: http://www.w3.org/ns/dx/prof/Profile

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/cross-domain-model/build/annotated/model/cross-domain/prof/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/cross-domain-model/build/annotated/model/cross-domain/prof/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "hasArtifact": "http://www.w3.org/ns/dx/prof/hasArtifact",
    "hasResource": "http://www.w3.org/ns/dx/prof/hasResource",
    "hasRole": "http://www.w3.org/ns/dx/prof/hasRole",
    "hasToken": "http://www.w3.org/ns/dx/prof/hasToken",
    "isProfileOf": "http://www.w3.org/ns/dx/prof/isProfileOf",
    "ResourceDescriptor": "http://www.w3.org/ns/dx/prof/ResourceDescriptor",
    "ResourceRole": "http://www.w3.org/ns/dx/prof/ResourceRole",
    "Profile": "http://www.w3.org/ns/dx/prof/Profile",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://ogcincubator.github.io/cross-domain-model/build/annotated/model/cross-domain/prof/context.jsonld)

## Sources

* [Profiles Vocabulary (PROF)](https://www.w3.org/TR/dx-prof/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/cross-domain-model](https://github.com/ogcincubator/cross-domain-model)
* Path: `_sources/prof`

