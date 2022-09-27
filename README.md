Python Framework
================
[![annea-ai](https://circleci.com/gh/annea-ai/python-framework.svg?style=svg)](https://app.circleci.com/pipelines/github/annea-ai/python-framework)

An implementation of a Python Framework

# Apps
Contains runnable apps. Apps are by default run with docker

## Docker Hub
Docker images are automatically built and published to [Docker Hub](https://hub.docker.com/r/anneaai/baz)

## Run
The functionality of all apps are exposed as entrypoints accepting arguments. 

### Docker Compose

Can be run using [Docker Compose](https://docs.docker.com/compose/install/). You can run a specific app using: 
```bash
docker-compose up annea_baz
```

## Natively 
The app can be installed as a pip package 
```
pip install .
annea_baz
```

# Libs
Contains reusable libs

# Dependencies
* Apps may depend on libs
* Libs may depend on other libs
* Apps may _not_ depend on other apps

# Test
Each app and lib contains a tox file which automatically runs test and lint as appropriate

# Pipeline
A [Circle CI](https://app.circleci.com/pipelines/github/annea-ai/python-framework) pipeline is connected to this repo, automatically running:
* Test
  * Python testing and linting
* Build and push docker
  * Build and push apps to Docker Hub