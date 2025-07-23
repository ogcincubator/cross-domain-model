
# PROV (Model)

`ogc.model.cross-domain.prov` *v0.1*

Provenance Ontology

[*Status*](http://www.opengis.net/def/status): Under development

## Description

## PROV-O ontology 

![](https://www.w3.org/TR/prov-o/diagrams/starting-points.svg)


## Examples

### Examples from CDT shapes
#### ttl
```ttl
# imports: http://example.org/shapes/sh-prov-o

@prefix drafting: <http://example.org/ontology/drafting/> .
@prefix kb: <http://example.org/kb/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<http://example.org/kb>
	a owl:Ontology ;
	rdfs:comment "This knowledge base instantiates each of the shape-reviewed classes and properties, so SHACL shapes can be exercised for the reviewed ontology."@en ;
	owl:imports <http://example.org/shapes/sh-prov-o> ;
	.

kb:Activity-055ad0f6-ac79-426a-9ff4-916d91408abb
	a prov:Activity ;
	prov:wasAssociatedWith kb:Agent-8dc1c08a-ce57-42d8-a5a8-5ddb866e1af4 ;
	.

kb:Activity-259084ee-1443-413a-be5e-19258700c938
	a prov:Activity ;
	prov:wasStartedBy kb:Entity-80e065c3-d2eb-44e3-8766-74c175b92253 ;
	.

kb:Activity-3208838f-ca7b-4f3b-bd9f-218bb284dba6
	a prov:Activity ;
	.

kb:Activity-3866ba0c-d3a5-4abe-ba66-38364b1bcc60
	a prov:Activity ;
	.

kb:Activity-3a6e56f3-82bf-4845-a3e3-db2629aefcc5
	a prov:Activity ;
	.

kb:Activity-3f0811bf-e8f3-486a-8e13-c80eadba535b
	a prov:Activity ;
	.

kb:Activity-423a095c-a035-45d6-83b5-b2e9b285e0c1
	a prov:Activity ;
	prov:qualifiedAssociation kb:Association-1166bd60-44eb-4fef-9dfa-768c2e48c067 ;
	.

kb:Activity-43b7bf02-c671-4118-92de-f11c803f4ee4
	a prov:Activity ;
	prov:wasEndedBy kb:Entity-40e0e42c-f0c5-443f-99a5-76e2aeda6e6a ;
	.

kb:Activity-6854f134-b36e-49b3-a1ce-c40a3186cb2d
	a prov:Activity ;
	prov:atLocation kb:Location-b63f7462-6712-4643-b79f-dbd2fd9a22be ;
	.

kb:Activity-70570b7c-fb1d-4aa4-93ca-4362511c04a4
	a prov:Activity ;
	prov:qualifiedUsage kb:Usage-dacf47cb-8db8-4b3c-9bfc-1be9492357f9 ;
	.

kb:Activity-78726a45-1b8e-4ff9-bb85-a589794c19a2
	a prov:Activity ;
	prov:generated kb:Entity-b03af4c5-a534-445c-a5f3-95a19dfba668 ;
	.

kb:Activity-78d0e682-85c9-4a98-a2bd-c9a9711f4c6e
	a prov:Activity ;
	prov:endedAtTime "2021-02-03T04:05:06"^^xsd:dateTime ;
	.

kb:Activity-892328a0-623f-4205-85fb-2a609a64c1d8
	a prov:Activity ;
	.

kb:Activity-982eadb7-6fc0-4b45-b4c3-e265443fda2e
	a prov:Activity ;
	prov:qualifiedCommunication kb:Communication-249d734c-3ef0-48ce-b299-c1761e7a0c16 ;
	.

kb:Activity-a1cdd771-e354-492c-a416-21dc87aba671
	a prov:Activity ;
	prov:wasInformedBy kb:Activity-c07999ab-2fda-407f-a56b-f9cb629a3d32 ;
	.

kb:Activity-b468d52a-fb50-4487-88fb-75684f1a8ed3
	a prov:Activity ;
	.

kb:Activity-c07999ab-2fda-407f-a56b-f9cb629a3d32
	a prov:Activity ;
	.

kb:Activity-c1f47707-71b8-465f-ad93-88ad513a6097
	a prov:Activity ;
	prov:Influencer kb:Thing-93559753-d7e7-4386-9f41-8c3b116e765e ;
	.

kb:Activity-c764f492-7f26-4169-8d2f-e7e178988c7a
	a prov:Activity ;
	.

kb:Activity-c8886e5d-9222-4376-870b-27fd07f2afd3
	a prov:Activity ;
	prov:startedAtTime "2021-02-03T04:05:06"^^xsd:dateTime ;
	.

kb:Activity-d726cd73-b3f9-4b98-8b80-54e2d57852cc
	a prov:Activity ;
	.

kb:Activity-e6c4261d-cc3b-4e37-9e23-00581db63cb0
	a prov:Activity ;
	prov:qualifiedStart kb:Start-7025ecf0-2da7-44d5-9a5c-34d973612b00 ;
	.

kb:Activity-ede98f6c-f7a8-4536-87ff-ec56d4ff5e41
	a prov:Activity ;
	prov:invalidated kb:Entity-4ab95072-98c8-414b-93a7-5a3d7ce8c70a ;
	.

kb:Activity-efe0303d-4894-48db-9386-25de485d0ebf
	a prov:Activity ;
	.

kb:Activity-fdd6bfe5-9e6c-46c9-8a19-c4fb2cc6886c
	a prov:Activity ;
	prov:qualifiedEnd kb:End-e576a7c7-c9de-49e8-b804-1d7b17194094 ;
	.

kb:Activity-fe9bb476-30f2-4529-913b-f4b4bc05e7d6
	a prov:Activity ;
	prov:used kb:Entity-fcb4ebbb-0e0c-4fc8-b9b9-e49b40aa9a67 ;
	.

kb:Agent-04d88a23-7bdf-4871-bff2-15146bc86a60
	a prov:Agent ;
	.

kb:Agent-18bf466c-cdd9-44f3-baf7-b4b07fd09108
	a prov:Agent ;
	.

kb:Agent-1d02a26f-331b-49aa-aea9-9af962660f44
	a prov:Agent ;
	.

kb:Agent-4cfffba0-49fd-4bd1-a394-080eab9bc9e6
	a prov:Agent ;
	.

kb:Agent-574c5e77-6115-4cd3-a23d-383822297327
	a prov:Agent ;
	.

kb:Agent-632af3ab-40de-4a56-99dc-53fe7ba59152
	a prov:Agent ;
	.

kb:Agent-66d6b439-4ec4-4aaf-a900-854774536854
	a prov:Agent ;
	prov:atLocation kb:Location-b7e65ef4-43cd-4a53-8846-296cc08e98b1 ;
	.

kb:Agent-7034a8cd-0e41-4dde-8c7a-e942758a4ad1
	a prov:Agent ;
	.

kb:Agent-77a51580-ac66-4e36-ace2-c43b5673c432
	a prov:Agent ;
	prov:actedOnBehalfOf kb:Agent-1d02a26f-331b-49aa-aea9-9af962660f44 ;
	.

kb:Agent-845c1d7f-a0c1-429a-9222-50aa7e4476b5
	a prov:Agent ;
	prov:qualifiedDelegation kb:Delegation-4360182c-2964-41e3-ac38-53f94114d312 ;
	.

kb:Agent-8dc1c08a-ce57-42d8-a5a8-5ddb866e1af4
	a prov:Agent ;
	.

kb:Agent-a411145a-2e53-4257-b7ac-5d45ebde85f8
	a prov:Agent ;
	.

kb:Agent-b2bfb91f-8d01-4ba6-b6d2-3eae5ada781e
	a prov:Agent ;
	.

kb:Agent-b644388b-cdc9-4b83-8c8b-cb602348a8bb
	a prov:Agent ;
	.

kb:Agent-d104b300-8ee5-4121-9b03-4d6648e7410a
	a prov:Agent ;
	.

kb:Association-04eba989-1566-4ff6-ac69-10efa79de275
	a prov:Association ;
	prov:agent kb:Agent-7034a8cd-0e41-4dde-8c7a-e942758a4ad1 ;
	prov:hadPlan kb:Plan-72046d3a-85f9-4f65-8e08-bcbc2087e038 ;
	.

kb:Association-1166bd60-44eb-4fef-9dfa-768c2e48c067
	a prov:Association ;
	prov:agent kb:Agent-b2bfb91f-8d01-4ba6-b6d2-3eae5ada781e ;
	.

kb:Association-c6e63cf0-a3a1-4698-b661-250a1477c892
	a prov:Association ;
	prov:agent kb:Agent-18bf466c-cdd9-44f3-baf7-b4b07fd09108 ;
	.

kb:Association-d52a7030-35ec-4490-93bc-a5996b29c033
	a prov:Association ;
	prov:agent kb:Agent-574c5e77-6115-4cd3-a23d-383822297327 ;
	prov:hadRole kb:Role-254159a1-0454-41a2-905e-b718f009daf7 ;
	.

kb:Attribution-dfc5046f-70f3-4699-91ba-40f33ab7f8a6
	a prov:Attribution ;
	prov:agent kb:Agent-632af3ab-40de-4a56-99dc-53fe7ba59152 ;
	.

kb:Attribution-efc9ce2e-45b1-464a-8de3-0da30b9e697d
	a prov:Attribution ;
	prov:agent kb:Agent-d104b300-8ee5-4121-9b03-4d6648e7410a ;
	.

kb:Collection-c446e934-bd1b-4415-9aa0-a315215b6fcd
	a prov:Collection ;
	prov:hadMember kb:Entity-64668442-c9bc-4d8d-a99a-3ec3579648e2 ;
	.

kb:Communication-249d734c-3ef0-48ce-b299-c1761e7a0c16
	a prov:Communication ;
	.

kb:Communication-2e79a35c-93b0-49ba-adc6-8e0189f40b64
	a prov:Communication ;
	.

kb:Communication-d3da045b-3ed7-4458-8bdc-59de3b3df288
	a prov:Communication ;
	prov:activity kb:Activity-b468d52a-fb50-4487-88fb-75684f1a8ed3 ;
	.

kb:Delegation-11b363d8-3a59-4b41-b6cc-3a74f25bee1a
	a prov:Delegation ;
	prov:agent kb:Agent-04d88a23-7bdf-4871-bff2-15146bc86a60 ;
	prov:hadActivity kb:Activity-3a6e56f3-82bf-4845-a3e3-db2629aefcc5 ;
	.

kb:Delegation-23cb2d60-1b4d-4938-bf53-e111e5f06544
	a prov:Delegation ;
	prov:agent kb:Agent-a411145a-2e53-4257-b7ac-5d45ebde85f8 ;
	.

kb:Delegation-4360182c-2964-41e3-ac38-53f94114d312
	a prov:Delegation ;
	prov:agent kb:Agent-b644388b-cdc9-4b83-8c8b-cb602348a8bb ;
	.

kb:Derivation-1576da3f-8839-44e5-9f9a-36198fe1370c
	a prov:Derivation ;
	.

kb:Derivation-3cd44de5-990d-4ca7-82c8-f21bd926b45b
	a prov:Derivation ;
	prov:hadUsage kb:Usage-1a8c5d7b-fad5-4337-bd24-6482179054a4 ;
	.

kb:Derivation-567379e6-cde8-4a47-b900-a41b27873654
	a prov:Derivation ;
	prov:hadActivity kb:Activity-d726cd73-b3f9-4b98-8b80-54e2d57852cc ;
	.

kb:Derivation-618708b2-bee1-4753-92ac-2505818fc445
	a prov:Derivation ;
	prov:entity kb:Entity-edbe2219-ebfe-43ad-9cc0-66e9a93754c3 ;
	.

kb:Derivation-722d3628-f779-48a4-b489-bd0af1119cff
	a prov:Derivation ;
	prov:hadGeneration kb:Generation-85bf06f0-f653-449d-80c5-43617901893f ;
	.

kb:EmptyCollection-32383360-03ef-4391-bcfa-887d676349d4
	a prov:EmptyCollection ;
	.

kb:End-2ab5742c-a99b-48c4-b8c8-dd5d757a2410
	a prov:End ;
	prov:hadActivity kb:Activity-efe0303d-4894-48db-9386-25de485d0ebf ;
	.

kb:End-7ba3b622-f9e5-4a9f-9e3b-5facd1ebe017
	a prov:End ;
	prov:hadRole kb:Role-cbb24b2b-f007-4cff-adb5-34d32a69746a ;
	.

kb:End-b6722f22-d1f2-4131-8f34-5b71f2063a53
	a prov:End ;
	prov:entity kb:Entity-9d0fb4a7-3188-4f65-add5-e020fba7e1d2 ;
	.

kb:End-e576a7c7-c9de-49e8-b804-1d7b17194094
	a prov:End ;
	.

kb:Entity-0c4f2cd1-0fee-4255-ab57-35d737c8eab7
	a prov:Entity ;
	.

kb:Entity-2bab1b00-d279-4558-83bf-2c5f6e74afd6
	a prov:Entity ;
	prov:qualifiedAttribution kb:Attribution-efc9ce2e-45b1-464a-8de3-0da30b9e697d ;
	.

kb:Entity-40e0e42c-f0c5-443f-99a5-76e2aeda6e6a
	a prov:Entity ;
	.

kb:Entity-431b574e-43a3-46c9-b57c-097e75692c3c
	a prov:Entity ;
	prov:invalidatedAtTime "2021-02-03T04:05:06"^^xsd:dateTime ;
	.

kb:Entity-472918e7-30c3-476a-8bdd-ffff3b74fe66
	a prov:Entity ;
	prov:value "" ;
	.

kb:Entity-4ab95072-98c8-414b-93a7-5a3d7ce8c70a
	a prov:Entity ;
	.

kb:Entity-5783a28e-28b9-4c95-a53f-9a3ec5618afc
	a prov:Entity ;
	prov:qualifiedQuotation kb:Quotation-bc6a70c7-7d80-4f7d-a3cb-023d026a7829 ;
	.

kb:Entity-59e8d749-a708-4572-a77d-a243c5da0b08
	a prov:Entity ;
	prov:qualifiedDerivation kb:Derivation-1576da3f-8839-44e5-9f9a-36198fe1370c ;
	.

kb:Entity-64668442-c9bc-4d8d-a99a-3ec3579648e2
	a prov:Entity ;
	.

kb:Entity-6afcf87b-0cfe-4c41-a48e-69b88c419277
	a prov:Entity ;
	prov:qualifiedPrimarySource kb:PrimarySource-f9da2989-49af-4572-bebe-6211d8049307 ;
	.

kb:Entity-6d214b7a-a23e-4557-bd30-9967c29248ba
	a prov:Entity ;
	prov:qualifiedGeneration kb:Generation-3b74f860-58a3-429b-b8bb-1db73af3c93b ;
	.

kb:Entity-745cc019-a274-4ddd-971d-ec71de6a73bf
	a prov:Entity ;
	prov:hadPrimarySource kb:Entity-d17a5554-cbaa-401a-88e6-d20dde65f18b ;
	.

kb:Entity-7672323d-4b1f-4bb1-96bc-e569d3bcdaf9
	a prov:Entity ;
	prov:generatedAtTime "2021-02-03T04:05:06"^^xsd:dateTime ;
	.

kb:Entity-80e065c3-d2eb-44e3-8766-74c175b92253
	a prov:Entity ;
	.

kb:Entity-931da65d-356e-4206-9be5-e051b268e4a6
	a prov:Entity ;
	.

kb:Entity-9d0fb4a7-3188-4f65-add5-e020fba7e1d2
	a prov:Entity ;
	.

kb:Entity-a2d4e498-411a-4bb2-9afb-745cdc994b01
	a prov:Entity ;
	prov:qualifiedInvalidation kb:Invalidation-7de11ce3-82d4-4b73-b897-5a7a9c4c6fa1 ;
	.

kb:Entity-a644ab7a-af35-4d41-a499-15b6c0cc7149
	a prov:Entity ;
	prov:wasAttributedTo kb:Agent-4cfffba0-49fd-4bd1-a394-080eab9bc9e6 ;
	.

kb:Entity-b03af4c5-a534-445c-a5f3-95a19dfba668
	a prov:Entity ;
	.

kb:Entity-b03e9e8b-c532-4196-9a2e-d03ca4d0b410
	a prov:Entity ;
	prov:wasGeneratedBy kb:Activity-3208838f-ca7b-4f3b-bd9f-218bb284dba6 ;
	.

kb:Entity-c373f9c2-2b89-4d2f-a15d-d32cb8eb0b7d
	a prov:Entity ;
	prov:atLocation kb:Location-df1498ad-f23d-4a4a-9e2e-819699bf756f ;
	.

kb:Entity-cc8fd573-5a5f-46f3-98a4-267c74c7237c
	a prov:Entity ;
	prov:wasInvalidatedBy kb:Activity-3866ba0c-d3a5-4abe-ba66-38364b1bcc60 ;
	.

kb:Entity-d17a5554-cbaa-401a-88e6-d20dde65f18b
	a prov:Entity ;
	.

kb:Entity-dd0ff55f-9d3c-4015-b615-1af278b9416d
	a prov:Entity ;
	prov:wasQuotedFrom kb:Entity-0c4f2cd1-0fee-4255-ab57-35d737c8eab7 ;
	.

kb:Entity-ebab84f1-c588-4322-a2df-299c83e3ca1d
	a prov:Entity ;
	prov:qualifiedRevision kb:Revision-c95166e6-026c-4c09-8de0-17cb45b6c032 ;
	.

kb:Entity-edbe2219-ebfe-43ad-9cc0-66e9a93754c3
	a prov:Entity ;
	.

kb:Entity-f79f45be-2688-4f4f-8685-b0bb8bebc99e
	a prov:Entity ;
	.

kb:Entity-fcb4ebbb-0e0c-4fc8-b9b9-e49b40aa9a67
	a prov:Entity ;
	.

kb:Generation-206644ad-0d51-41e3-abc2-62accb95dfc4
	a prov:Generation ;
	prov:activity kb:Activity-892328a0-623f-4205-85fb-2a609a64c1d8 ;
	.

kb:Generation-32bb59df-587e-4629-9bec-563da666aa07
	a prov:Generation ;
	prov:hadRole kb:Role-2ab1eb15-5ae7-46ed-bbb7-2c1296f46ecc ;
	.

kb:Generation-3b74f860-58a3-429b-b8bb-1db73af3c93b
	a prov:Generation ;
	.

kb:Generation-85bf06f0-f653-449d-80c5-43617901893f
	a prov:Generation ;
	.

kb:InstantaneousEvent-48b77196-256b-4461-a22e-8ba5f3e8ccef
	a prov:InstantaneousEvent ;
	prov:atLocation kb:Location-6bbfca64-537b-480c-9a11-20bace29f2f7 ;
	.

kb:InstantaneousEvent-d0940846-eac6-42be-ac67-5fec49c05306
	a prov:InstantaneousEvent ;
	prov:atTime "2021-02-03T04:05:06"^^xsd:dateTime ;
	.

kb:Invalidation-0cfe9dca-bbd2-4ff2-af7b-c41a6b3534ff
	a prov:Invalidation ;
	prov:hadRole kb:Role-e5b38f09-1935-4182-b055-e267c89e4162 ;
	.

kb:Invalidation-7de11ce3-82d4-4b73-b897-5a7a9c4c6fa1
	a prov:Invalidation ;
	.

kb:Invalidation-eeca51e2-d180-4b72-87ac-0a3ce472029f
	a prov:Invalidation ;
	prov:activity kb:Activity-3f0811bf-e8f3-486a-8e13-c80eadba535b ;
	.

kb:Location-6bbfca64-537b-480c-9a11-20bace29f2f7
	a prov:Location ;
	.

kb:Location-b63f7462-6712-4643-b79f-dbd2fd9a22be
	a prov:Location ;
	.

kb:Location-b7e65ef4-43cd-4a53-8846-296cc08e98b1
	a prov:Location ;
	.

kb:Location-df1498ad-f23d-4a4a-9e2e-819699bf756f
	a prov:Location ;
	.

kb:Plan-72046d3a-85f9-4f65-8e08-bcbc2087e038
	a prov:Plan ;
	.

kb:PrimarySource-f9da2989-49af-4572-bebe-6211d8049307
	a prov:PrimarySource ;
	.

kb:Quotation-bc6a70c7-7d80-4f7d-a3cb-023d026a7829
	a prov:Quotation ;
	.

kb:Revision-c95166e6-026c-4c09-8de0-17cb45b6c032
	a prov:Revision ;
	.

kb:Role-254159a1-0454-41a2-905e-b718f009daf7
	a prov:Role ;
	.

kb:Role-294b74e9-6a0e-4ce9-8e9a-8aea2342244d
	a prov:Role ;
	.

kb:Role-2ab1eb15-5ae7-46ed-bbb7-2c1296f46ecc
	a prov:Role ;
	.

kb:Role-b83c0430-0b67-4399-8b31-0d1ba5fd3dc0
	a prov:Role ;
	.

kb:Role-cbb24b2b-f007-4cff-adb5-34d32a69746a
	a prov:Role ;
	.

kb:Role-e5b38f09-1935-4182-b055-e267c89e4162
	a prov:Role ;
	.

kb:Start-024b6c55-9f58-42bf-8ee6-bb5ae63b3b22
	a prov:Start ;
	prov:hadActivity kb:Activity-c764f492-7f26-4169-8d2f-e7e178988c7a ;
	.

kb:Start-2d92e44c-8d08-404d-9d20-918763d934ac
	a prov:Start ;
	prov:entity kb:Entity-931da65d-356e-4206-9be5-e051b268e4a6 ;
	.

kb:Start-7025ecf0-2da7-44d5-9a5c-34d973612b00
	a prov:Start ;
	.

kb:Start-fd19e3ff-65c3-4b07-b041-baf5d0cf3a74
	a prov:Start ;
	prov:hadRole kb:Role-294b74e9-6a0e-4ce9-8e9a-8aea2342244d ;
	.

kb:Thing-93559753-d7e7-4386-9f41-8c3b116e765e
	a owl:Thing ;
	.

kb:Usage-0f857657-0e9b-4c8c-b682-1a647ff2ea5c
	a prov:Usage ;
	prov:entity kb:Entity-f79f45be-2688-4f4f-8685-b0bb8bebc99e ;
	.

kb:Usage-1a8c5d7b-fad5-4337-bd24-6482179054a4
	a prov:Usage ;
	.

kb:Usage-ad78fe82-889d-46a2-8b80-cf73772dbf05
	a prov:Usage ;
	prov:hadRole kb:Role-b83c0430-0b67-4399-8b31-0d1ba5fd3dc0 ;
	.

kb:Usage-dacf47cb-8db8-4b3c-9bfc-1be9492357f9
	a prov:Usage ;
	.


```

## Sources

* [PROV-O Specification](https://www.w3.org/TR/prov-o/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/cross-domain-model](https://github.com/ogcincubator/cross-domain-model)
* Path: `_sources/prov`

