#!/usr/bin/env python
"""
Description goes here
"""
__author__ = "jupp"
__license__ = "Apache 2.0"
__date__ = "16/07/2019"

import json
import requests
import sys
import glob

from rdflib.plugin import register, Parser
from rdflib import Graph, ConjunctiveGraph

import rdflib_jsonld

# Initialize JSONLDParser
register('json-ld', Parser, 'rdflib_jsonld.parser', 'JsonLDParser')

with open('json-ld-context.json', 'r') as f:
    context = json.load(f)

LDP_SERVER="http://localhost:8890/DAV/home/LDP/"
LDP_USER='ldp'
LDP_PASS='ldp'

def creater_container():
    pass


def main():
    # print command line arguments
    container = open('container.ttl', 'rb').read()

    for arg in sys.argv[1:]:

        print ("processing " + arg)
        graph = ConjunctiveGraph()
        catalog_file = "{}/{}.ttl".format(arg, 'catalog')

        try:
            with open(arg+'/catalog.json', 'r') as f:
                catalog = json.load(f)
                catalog["@context"] = context["@context"]

                # convert JSON to ttl and dump
                graph.parse(data=json.dumps(catalog), format='json-ld')
                graph.serialize(destination=catalog_file, format='ttl')
        except:
            print ("No catalog.json found for {}".format(arg))


        # create the LDP container and upload ttl
        requests.post(url=LDP_SERVER,
                        data=container,
                        auth=(LDP_USER, LDP_PASS),
                        headers={
                            'Content-Type': 'text/turtle',
                            'Accept': 'text/turtle',
                            'Slug' : arg +'_catalog'
                        })

        data = open(catalog_file, 'rb').read()
        requests.put(url=LDP_SERVER + "/" + arg +'_catalog' + "/",
                        data=data,
                        auth=(LDP_USER, LDP_PASS),
                        headers={
                            'Content-Type': 'text/turtle',
                            'Accept': 'text/turtle',
                        })

        files = [f for f in glob.glob(arg + "/datasets/*.json")]
        fc = 1
        files_to_load =[]
        for f in files:
            with open(f, 'r') as json_file:
                dataset = json.load(json_file)

                dataset["@context"] = context["@context"]
                graph = ConjunctiveGraph()
                graph.parse(data=json.dumps(dataset), format='json-ld')
                dataset_file_name = "{}_registry_{}".format(arg, str(fc))
                dataset_file_path = "{}/datasets/{}.ttl".format(arg, dataset_file_name)
                graph.serialize(destination=dataset_file_path, format='ttl')

                file_info = {
                    'dataset_file_name' : dataset_file_name,
                    'dataset_file_path' : dataset_file_path
                }
                files_to_load.append(file_info)

                fc+=1

        # create the LDP container for datases and upload ttl
        files_to_load = [f for f in glob.glob(arg + "/datasets/*.ttl")]

        for ttl_file in files_to_load:

            dataset_file_name = ttl_file.split("/")[-1]
            requests.post(url=LDP_SERVER + "/" + arg + '_catalog' + "/",
                          data=container,
                          auth=(LDP_USER, LDP_PASS),
                          headers={
                              'Content-Type': 'text/turtle',
                              'Accept': 'text/turtle',
                              'Slug': dataset_file_name
                          })


            data = open(ttl_file, 'rb').read()
            requests.put(url=LDP_SERVER + "/" + arg + '_catalog' + "/" + dataset_file_name + "/",
                         data=data,
                         auth=(LDP_USER, LDP_PASS),
                         headers={
                             'Content-Type': 'text/turtle',
                             'Accept': 'text/turtle',
                         })



if __name__ == "__main__":
    main()


