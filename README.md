# Linked data platform for EJP rare disease

This is an import script for loading data about catalogs of rare disease registries into a Linked Data Platform server (LDP).

## Start an local LDP server

`docker run      --name my_virtdb      --publish 1111:1111      --publish  8890:8890      markw/ldp_server`

## Install the requiremnts

`pip install -r requirements.txt`

# Run the loader

`python importer.py erdri rd-sample`

# Run a cool query

Go to http://localhost:8890/sparql to execute the follwowing queries:

1. Find all registries in all catalogs and get the name, disease code and registry country.


```
PREFIX foaf: <http://xmlns.com/foaf/0.1/>
PREFIX fo: <http://www.w3.org/1999/XSL/Format#>
PREFIX dc: <http://purl.org/dc/elements/1.1/>
PREFIX iao: <http://purl.obolibrary.org/obo/iao.owl#>
PREFIX schema: <http://schema.org/>
PREFIX sc: <http://purl.org/science/owl/sciencecommons/>
PREFIX sio: <http://semanticscience.org/resource/>
PREFIX ncit: <http://purl.obolibrary.org/obo/>
PREFIX dcat: <http://www.w3.org/ns/dcat#>
PREFIX dct: <http://purl.org/dc/terms/>
PREFIX ldp: <http://www.w3.org/ns/ldp#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX ejp: <http://purl.org/ejp-rd/vocabulary/>

SELECT DISTINCT ?catalog_title ?reg_title ?disease ?country
WHERE {

  <http://localhost:8890/DAV/home/LDP/> ldp:contains ?catalog_container .

  GRAPH ?catalog_container {
    ?catalog a ejp:CatalogOfRegistries .
    ?catalog dct:title ?catalog_title .
    ?catalog dcat:dataset ?registry .
    ?catalog_container ldp:contains ?registry_container
  }
  GRAPH ?registry_container {
    ?registry a ?registry_type .
    FILTER (?registry_type IN (ejp:BiobankDataset, ejp:PatientRegistryDataset))
    ?registry dct:title ?reg_title .
    ?registry dcat:theme ?disease .
    ?registry dct:publisher [ dct:spatial [ ejp:country ?country] ]
  }
}
```