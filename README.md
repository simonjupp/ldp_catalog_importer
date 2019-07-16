# Linked data platform for EJP rare disease

This is an import script for loading data about catalogs of rare disease registries into a Linked Data Platform server (LDP).

## Start an local LDP server

`docker run      --name my_virtdb      --publish 1111:1111      --publish  8890:8890      markw/ldp_server`

## Install the requiremnts

`pip install -r requirements.txt`

# Run the loader

`python importer.py erdri rd-sample`
