
# SOSA Examples (Schema)

`ogc.model.cross-domain.sosa-spec-examples` *v1.0*

This Building Block identifies examples from the SOSA specification and supports validation of these examples

[*Status*](http://www.opengis.net/def/status): Under development

## Description

## SOSA Specification Examples

This building block runs tests against the SOSA specification examples.

As TTL files these examples are validated against the SHACL rules inherited from the building blocks for elements of the specification

## Examples

### Example ice-core.ttl
#### ttl
```ttl
@prefix rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix time: <http://www.w3.org/2006/time#>.
@prefix sosa: <http://www.w3.org/ns/sosa/> .
@prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
@prefix geo: <http://www.w3.org/2003/01/geo/wgs84_pos#>.
@base <http://example.org/data/> .


# The CO2 level observed in an ice core is 240 parts per million.
# the ice core is a sample of the polar ice sheet of Antarctica. 

<http://dbpedia.org/resource/Antarctic_ice_sheet> a sosa:FeatureOfInterest ;
  sosa:hasSample <iceCore/12>, <iceCore/13>, <iceCore/14> .

<iceCore/12> rdf:type sosa:Sample ;
  sosa:isSampleOf <http://dbpedia.org/resource/Antarctic_ice_sheet> ;
  sosa:isResultOf <WellDrilling/4578> ;
  sosa:madeBySampler <thermalDrill/2> .

  <WellDrilling/4578> a sosa:Sampling ;
    geo:lat -73.35 ; 
    geo:long 9.32 ;
    sosa:hasResult <iceCore/12> ;
    sosa:madeBySampler <thermalDrill/2> ;
    sosa:resultTime "2017-04-03T11:12:00Z"^^xsd:dateTime ;
    sosa:hasFeatureOfInterest <http://dbpedia.org/resource/Antarctic_ice_sheet> .

<iceCore/12#observation> a sosa:Observation ;
  sosa:observedProperty <iceCore/12#CO2> ;
  sosa:hasSimpleResult 240 .

# using SSN one can explicitly state that <iceCore/12#CO2> is the property of <iceCore/12> .

<iceCore/12#CO2> sosa:isPropertyOf <iceCore/12> .
  
```

## Sources

* [Semantic Sensor Network Ontology](https://www.w3.org/TR/vocab-ssn/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/cross-domain-model](https://github.com/ogcincubator/cross-domain-model)
* Path: `_sources/sosa-spec-examples`
