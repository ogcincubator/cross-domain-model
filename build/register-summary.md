# Cross-domain model

Defines a reusable baseline "cross-domain semantic model" by defining a series of profiles and dependencies on available standards and where appropriate a set of constraints for application of such standards in the spatio-temporal domain.



These models are defined as ["building blocks"](https://ogcincubator.github.io/bblocks-docs/) to allow for transparent reuse of a range of semantic models published by OGC and other international standards organisations (SDO) that may be used to define semantic models for application domains in a consistent and interoperable way.

Application domains will typically define profiles of these core models to meet specific needs. Infrastructures supporting application domains may define more general profiles to support commonality of implementation necessary to exploit infrastructure services. 

The Cross-domain model underpins proposed domain models for Agriculture, Oceans and AG4DG.
By defining these models using this common cross-domain model the interoperability between such domains is enhanced, and made transparent to applications.

Note that metadata models may be defined to exploit these semantics -
the cross-domain model is agnostic of the various metadata schemas or models that may be used, recognising that most "systems of systems" will have 
multiple metadata formats in play due to evolution, backwards compatibility requirements and specific metadata needs of different communities and systems.

![](https://lucid.app/publicSegments/view/eebe9d1b-d2ae-4bb9-a929-1d4414abcd47/image.png)

Defining constraints using SHACL for these building blocks allows for inheritance of validation rules. 
This will dramatically reduce the complexity of defining and testing domain models in a consistent fashion.

Many such restrictions will relate to the way these models are combined -
for example the way GeoDCAT, PROV, RDF-Datacube and SOSA may be combined to standardise the way observational data is described using available standards.


## Building Blocks

### `ogc.model.cross-domain.prov` — PROV

**Type:** model

Provenance Ontology

### `ogc.model.cross-domain.geosparql` — GeoSPARQL

**Type:** model

GeoSPARQL Core (1.1). Simply wraps the published GeoSPARQL ontology with a Building Block to allow examples, default JSON-LD context, SHACL rules and transforms to be easily discovered.

### `ogc.model.cross-domain.datacube` — RDF-DataCube

**Type:** model

Dimensional Data Model based on SDMX

### `ogc.model.cross-domain.sosa` — SOSA/SSN

**Type:** model

Sensors, Observations, Sampling and Actuation (ISO 19156 Observations and Measurements) Ontology 

### `ogc.model.cross-domain.codemeta` — CodeMeta vocabulary

**Type:** model

CodeMeta 3.0 terms for describing software (`buildInstructions`, `developmentStatus`, `continuousIntegration`, `embargoEndDate`, `hasSourceCode`, `isSourceCodeOf`, `issueTracker`, `readme`, `referencePublication`, `softwareSuggestions`).

### `ogc.model.cross-domain.dcterms` — Dublin Core Terms vocabulary

**Type:** model

DCMI Metadata Terms used across metadata models (`conformsTo`, `Standard`, etc.).

### `ogc.model.cross-domain.iana-relations` — IANA link relations vocabulary

**Type:** model

IANA link relation terms (e.g. `cite-as`, RFC 8574) for marking preferred citation targets and other link semantics.

### `ogc.model.cross-domain.pav` — PAV vocabulary

**Type:** model

Provenance, Authoring and Versioning (PAV) terms for import/retrieval provenance (`importedFrom`, `importedOn`, `importedBy`, `retrievedFrom`, `retrievedOn`, `retrievedBy`). Complements PROV-O, which this register already covers separately.

### `ogc.model.cross-domain.pcdm` — PCDM vocabulary

**Type:** model

Portland Common Data Model terms for describing repositories and collections of digital objects (`RepositoryObject`, `RepositoryCollection`, `RepositoryFile`, `hasMember`, `hasFile`).

### `ogc.model.cross-domain.prof` — PROF vocabulary

**Type:** model

W3C Profiles Vocabulary (PROF) terms for describing resource profiles and their roles.

### `ogc.model.cross-domain.qudt` — QUDT

**Type:** model

Quantities, Units etc.

### `ogc.model.cross-domain.schema-org` — Schema.org vocabulary

**Type:** model

The full Schema.org term vocabulary: every Schema.org type and property name mapped 1:1 to its `http://schema.org/` URI.

### `ogc.model.cross-domain.sosa-profiles.sosa-sta` — SOSA Profile for STA data model

**Type:** model

Defines a profile of SOSA with constraints to fit the Sensor Things API object types. .....

### `ogc.model.cross-domain.sosa-spec-examples` — SOSA Examples

**Type:** schema

This Building Block identifies examples from the SOSA specification and supports validation of these examples

### `ogc.model.cross-domain.qudt-basic` — QUDT Basic Profile

**Type:** model

Minimal implementation of Quantities, Units etc.

### `ogc.model.cross-domain.all` — Cross Domain Model (Complete)

**Type:** model

All modules of the Cross Domain model

