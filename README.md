# AI from Zero to Production
This repository is created for demonstrating basic end-to-end AI/ML creation workflow from training a model to delivering it to the production environment.

## Prerequisites
- Python 3.9
- Docker
- Postman (or other similar REST client)
- Visual Studio Code

## Dataset
- [IMDb dataset](https://www.kaggle.com/datasets/ashirwadsangwan/imdb-dataset)

## Setup
0. Clone the repository
```sh
git clone https://github.com/luangtatipsy/ai-zero-to-production.git
cd ai-zero-to-production
```
1. Create and activate a virtual environment for Python _(recommended)_. If you do not prefer using a virtual environment, skip to step 4.
```sh
python -m venv env
source env/bin/activate
```
2. Update pip to latest version
```sh
python -m pip install --upgrade pip
```
3. Install requirements
```sh
python -m pip install -r requirements.txt
```

## Run API Locally
```sh
uvicorn src.app:app --reload
```

## Build Docker Image
a. Build locally
```sh
docker build -t <your-username>/<image>:<tag> -f docker/Dockerfile .
docker run -p <host-port>:80 <image>:<tag>
```

b. Build to Docker Hub to be used in production environment
```sh
docker buildx create --use
docker login
docker buildx build --platform linux/amd64,linux/arm64 -t <your-username>/<image>:<tag> -f docker/Dockerfile . --push
```

## License
This repository is distributed under [MIT License](https://github.com/luangtatipsy/ai-zero-to-production/blob/main/LICENSE)
