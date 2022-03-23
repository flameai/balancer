# Network load balancer

Test task for More.tv company from Andryukov.A.L andryukov@gmail.com

## Requirements
- python3.10
- redis-server


## Installation
### First way locally
Clone repo

Create virtual environment
```bash
python -m venv venv
```

Activate env
```bash
source ./venv/bin/activate
```
Upgrade pip
```bash
pip install --upgrade pip
```
Install poetry
```bash
pip install poetry
```
Install packages
```bash
poetry install
```
Copy env.example and put appropriate variables there
```bash
cp .env.example .env
```

Run service
```bash
python main.py
```

Now you can try to send requests to http://127.0.0.1:8000/?video=http://server_number123.cluster/path/to/your/video

### Second way with Docker

```bash
docker-compose up
```

Now you can try to send requests to http://127.0.0.1/?video=http://server_number123.cluster/path/to/your/video

## Tests

Be sure that all parts work all right with command:
```bash
pytest
```
