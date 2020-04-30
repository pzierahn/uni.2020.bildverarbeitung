# uni.2020.bildverarbeitung

## Before you start:

```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run docker

```
docker run -p 8888:8888 --rm -v $(pwd)/exercise.01.notebook:/home/jovyan jupyter/datascience-notebook
```

### Git Stuff
```
git tag Exercise-01
git push origin Exercise-01
```