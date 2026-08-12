
# CodeMeta vocabulary (Model)

`ogc.model.cross-domain.codemeta` *v1.0.0*

CodeMeta 3.0 terms for describing software (`buildInstructions`, `developmentStatus`, `continuousIntegration`, `embargoEndDate`, `hasSourceCode`, `isSourceCodeOf`, `issueTracker`, `readme`, `referencePublication`, `softwareSuggestions`).

[*Status*](http://www.opengis.net/def/status): Under development

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: CodeMeta vocabulary
description: 'Unconstrained carrier schema: this block''s content is its JSON-LD context,
  not a data shape. The schema exists only so other blocks can `$ref` it via `bblocks://`
  and inherit the context.'
type: object
x-jsonld-extra-terms:
  softwareSuggestions: https://codemeta.github.io/terms/softwareSuggestions
  continuousIntegration: https://codemeta.github.io/terms/continuousIntegration
  buildInstructions: https://codemeta.github.io/terms/buildInstructions
  developmentStatus: https://codemeta.github.io/terms/developmentStatus
  embargoEndDate: https://codemeta.github.io/terms/embargoEndDate
  readme: https://codemeta.github.io/terms/readme
  issueTracker: https://codemeta.github.io/terms/issueTracker
  referencePublication: https://codemeta.github.io/terms/referencePublication
  hasSourceCode: https://codemeta.github.io/terms/hasSourceCode
  isSourceCodeOf: https://codemeta.github.io/terms/isSourceCodeOf

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/cross-domain-model/build/annotated/model/cross-domain/codemeta/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/cross-domain-model/build/annotated/model/cross-domain/codemeta/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "softwareSuggestions": "https://codemeta.github.io/terms/softwareSuggestions",
    "continuousIntegration": "https://codemeta.github.io/terms/continuousIntegration",
    "buildInstructions": "https://codemeta.github.io/terms/buildInstructions",
    "developmentStatus": "https://codemeta.github.io/terms/developmentStatus",
    "embargoEndDate": "https://codemeta.github.io/terms/embargoEndDate",
    "readme": "https://codemeta.github.io/terms/readme",
    "issueTracker": "https://codemeta.github.io/terms/issueTracker",
    "referencePublication": "https://codemeta.github.io/terms/referencePublication",
    "hasSourceCode": "https://codemeta.github.io/terms/hasSourceCode",
    "isSourceCodeOf": "https://codemeta.github.io/terms/isSourceCodeOf",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://ogcincubator.github.io/cross-domain-model/build/annotated/model/cross-domain/codemeta/context.jsonld)

## Sources

* [CodeMeta 3.0](https://w3id.org/codemeta/3.0)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/cross-domain-model](https://github.com/ogcincubator/cross-domain-model)
* Path: `_sources/codemeta`

