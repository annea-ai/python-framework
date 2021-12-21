Python Framework
================
[![annea-ai](https://circleci.com/gh/annea-ai/python-framework.svg?style=svg)](https://app.circleci.com/pipelines/github/annea-ai/python-framework)

An implementation of a Python Framework

# Apps
Contains runnable apps. Apps are by default run with docker

## Run
Can be run using [Docker Compose](https://docs.docker.com/compose/install/). You can run a specific app using: 
```bash
docker-compose up baz
```

# Libs
Contains reusable libs

# Dependencies
* Apps may depend on libs
* Libs may depend on other libs
* Apps may _not_ depend on other apps

# Test
Each app and lib contains a tox file which automatically runs test and lint as appropriate