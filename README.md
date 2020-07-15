# Command line swagger client

A CLI for every service which exposes a Swagger specification endpoint.

### Install libraries
Run the below commands in your terminal to install the libraries

    cd Aftermath
    pip3 install -r requirements.txt

### Run app

To start a CLI session run:

    python main.py -url <swagger-spec-url>

e.g:

    python main.py -url http://petstore.swagger.io/v2/swagger.json


### Demo

![Alt Text](https://github.com/turntabl/aftermath/blob/master/demo.gif)

Credits
-------
This project relies on rich (https://github.com/willmcgugan/rich) python library.
