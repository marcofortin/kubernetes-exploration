# kubernetes-exploration

## Setting up environment

Create virtual environment for Python3
```
python3 -m venv /path/to/new/virtual/environment
```

Activate virtual environment
```
source /path/to/new/virtual/environment/bin/activate
```

## Run locally

Install dependencies
```
pip install -r ./app/requirements.txt
```

Run application locally
```
python ./app/main.py
```

## Create an image
```
cd app
./createimage.sh
```

## Run in Docker
```
./rundocker.sh
```

## Run in Kubernetes
```
./deployk8s.sh
```