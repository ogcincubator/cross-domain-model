
# SOSA Examples (Schema)

`ogc.model.cross-domain.sosa-spec-examples` *v1.0*

This Building Block identifies examples from the SOSA specification and supports validation of these examples

[*Status*](http://www.opengis.net/def/status): Under development

## Description

## SOSA Specification Examples

This building block runs tests against the SOSA specification examples.

As TTL files these examples are validated against the SHACL rules inherited from the building blocks for elements of the specification

## Examples

### Example bubble-provenance.ttl
#### ttl
```ttl
@prefix ex: <https://example.org/data/> .
@prefix geo: <http://www.opengis.net/ont/geosparql#> .
@prefix orcid: <https://orcid.org/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix sosa: <http://www.w3.org/ns/sosa/> .
@prefix unit: <http://qudt.org/vocab/unit/> .
@prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .

ex:IceCore12 a sosa:Sample , sosa:MaterialSample ;
  sosa:isSampleOf ex:Antarctic_ice_sheet ;
  sosa:isResultOf ex:WellDrilling4578 ;
.
ex:Bubble873 a sosa:Sample , sosa:MaterialSample ;
  sosa:isSampleOf ex:IceCore12 , ex:EarthAtmosphere;
  sosa:hasSampledFeature ex:Antarctic_ice_sheet ;
  sosa:isResultOf ex:CoreEx1923 ;
.
ex:WellDrilling4578 a sosa:Sampling ;
  geo:hasGeometry [ 
    a geo:Point ;
    geo:asWKT "POINT (9.32 -73.35)"^^geo:WktLiteral ;
  ] ;
  sosa:hasResult ex:IceCore12 ;
  sosa:madeBySampler ex:ThermalDrill2 ;
  sosa:resultTime "2017-04-03T11:12:00Z"^^xsd:dateTime ;
  sosa:hasFeatureOfInterest ex:Antarctic_ice_sheet ;
.
ex:CoreEx1923 a sosa:Sampling ;
  sosa:hasInputValue [
      ex:offset "15.202"^^unit:M ;
  ] ;
  sosa:hasResult ex:Bubble873 ;
  sosa:madeBySampler orcid:0000-0002-3884-3420 ;
  sosa:resultTime "2018-01-09T14:12:00Z"^^xsd:dateTime ;
  sosa:hasFeatureOfInterest ex:IceCore12 ;
  sosa:hasUltimateFeatureOfInterest ex:Antarctic_ice_sheet ;
.
ex:Antarctic_ice_sheet a sosa:FeatureOfInterest ;
  owl:sameAs <https://www.wikidata.org/wiki/Q571430> ;
. 
ex:EarthAtmosphere a sosa:FeatureOfInterest ;
  owl:sameAs <https://www.wikidata.org/wiki/Q3230> ;
. 

```

## Sources

* [Semantic Sensor Network Ontology](https://www.w3.org/TR/vocab-ssn/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/cross-domain-model](https://github.com/ogcincubator/cross-domain-model)
* Path: `_sources/sosa-spec-examples`

