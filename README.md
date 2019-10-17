# cade-gest-diab3
This is a demo Resouces folder for the CADE2 pathway-based simulation tool

1. If you don't already have Docker on your system, download and install it from https://store.docker.com/search?type=edition&offering=community
2. If you don't already have Git on your system, download and install it from https://git-scm.com/downloads
3. Clone this project 
```sh
	git clone https://github.com/charliemccay/cade-gest-diab3
```
There is a docker-compose file to run the simulation using the following command:

docker-compose up

This will start a hapi fhir dstu2 server and populate it with resources from the CADE simulation 

The FHIR server can be stopped with ctrl-c.  When it is started again it will be empty.  This implementation of CADE uses UUIDs for the resource identifiers, so can be run multiple times without clashing identifiers - every time someone is born they are assumed to be a new person.

The BPMN models can be edited with the Camunda Modelling tool: https://camunda.com/download/modeler/

