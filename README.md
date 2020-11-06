# MTA Data Consumer

## Introduction
MTA Data consumer is a Python application for interfacing the [New York MTA Realtime Data Feeds](https://api.mta.info/)  
The Data Feeds are based on the General Transit Feed Specification (GTFS). The data exchange is based on Protocol Buffers.  
In this app we decode the protocol buffers and save the data as `json`. Each realtime data feed is registered as an endpoint and generates a unique filename.  
The feed is specified via the `endpoint_id` argument. The `repeat` and `interval` arguments are for number of requests and time between requests.  
Note that an interval of `-1` means that the script will run infinitely.    
The underlying data processing is done via asynchronous python datastreams built with [Tributary](https://github.com/timkpaine/tributary)

## Installation
The app is supposed to be executed within a docker container. Howver it can also be executed as a python scrpit.  
Install from source:

`python setup.py install`  
`python -m mta_data --endpoint_id 3 --repeat 2 --interval 5`

Run With Docker:

`docker build . -t mta_data`  
`docker run -v $(pwd)/data:/app/data -e MTA_DATA_API_KEY="<key here>" mta_data:latest --endpoint_id 3 --repeat 2 --interval 5`





