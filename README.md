Python Framework
================
[![annea-ai](https://circleci.com/gh/annea-ai/python-framework.svg?style=svg)](https://app.circleci.com/pipelines/github/annea-ai/python-framework)

An implementation of a Python Framework

# Apps
Contains runnable apps. Apps are by default run with docker

## Docker Hub
Docker images are automatically built and published to [Docker Hub](https://hub.docker.com/r/anneaai/baz)

## Run
Can be run using [Docker Compose](https://docs.docker.com/compose/install/). You can run a specific app using: 
```bash
docker-compose up baz
```

# Libs
Contains reusable libs

## Pypi
Libs are automatically built as pip packages and published to [pypi](https://pypi.org/project/annea-foo/)

# Dependencies
* Apps may depend on libs
* Libs may depend on other libs
* Apps may _not_ depend on other apps

# Test
Each app and lib contains a tox file which automatically runs test and lint as appropriate

# Pipeline
A [Circle CI](https://app.circleci.com/pipelines/github/annea-ai/python-framework) pipeline is connected to this repo, automatically running:
* Build and test
  * Python testing and linting
* Pypi Publish
  * Build and upload libs to pypi
* Build and push docker
  * Build and push apps to Docker Hub