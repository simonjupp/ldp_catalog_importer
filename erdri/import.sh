
curl -v -H "Accept: text/turtle" -H "Content-type: text/turtle" -u ldp:ldp --data-binary @container.ttl -H "Slug: ERDRIDorCatalog" http://localhost:8890/DAV/home/LDP/
curl -v -H "Accept: text/turtle" -H "Content-type: text/turtle" -X PUT -u ldp:ldp --data-binary @catalog.ttl -H "Slug: edricatalog" http://localhost:8890/DAV/home/LDP/ERDRIDorCatalog/


curl -v -H "Accept: text/turtle" -H "Content-type: text/turtle" -u ldp:ldp --data-binary @container.ttl -H "Slug: ERDRIRegistry1" http://localhost:8890/DAV/home/LDP/ERDRIDorCatalog/
curl -v -H "Accept: text/turtle" -H "Content-type: text/turtle" -X PUT -u ldp:ldp --data-binary @dataset_0.ttl -H "Slug: edricatalog_dataset1" http://localhost:8890/DAV/home/LDP/ERDRIDorCatalog/ERDRIRegistry1/

curl -v -H "Accept: text/turtle" -H "Content-type: text/turtle" -u ldp:ldp --data-binary @container.ttl -H "Slug: ERDRIRegistry2" http://localhost:8890/DAV/home/LDP/ERDRIDorCatalog/
curl -v -H "Accept: text/turtle" -H "Content-type: text/turtle" -X PUT -u ldp:ldp --data-binary @dataset_0.ttl -H "Slug: edricatalog_dataset2" http://localhost:8890/DAV/home/LDP/ERDRIDorCatalog/ERDRIRegistry2/
