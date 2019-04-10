# Twitter Harvester

A harvester app for twitter data

# Getting Started

## Prerequisites Stack
Make sure you have this stack installed on your machine first
- [CouchDB](http://couchdb.apache.org/)
- [RabbitMQ](https://www.rabbitmq.com/)
- Python 3.7

## Install dependencies
To avoid any conflict with system dependencies, run the installation under `virtual environment`.
```
$ pip install -r rquirements.txt
```

## Setup your config data
Copy `data/config.json.example` and rename it to `data/config.json`. Adjust the value in it to your own system configuration.

## Run the app
The script contain two main components
- Producer
  Fetch twitter data from streaming API and push it to message queue
- Consumer
  Consume twitter data from RabbitMQ queue and store it to CouchDB collection

### Run Producer
```
$ make producer
```

### Run Consumer
```
$ make consumer
```


# TODO
- [ ] Dockerize the app
- [ ] Run the whole system with `docker-compose`
