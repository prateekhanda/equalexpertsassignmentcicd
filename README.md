# GitHub Gists API

A simple, production-ready REST API built with FastAPI that fetches publicly available GitHub Gists for a given user.

---

## Project Structure

```
project-root/
│
├── app/
│   ├── main.py
│   │
│   ├── core/
│   │   └── config.py
│   │
│   ├── api/
│   │   └── v1/
│   │       └── routers/
│   │           └── gists.py
│   │
│   ├── services/
│   │   └── github_service.py
│   │
│   ├── schemas/
│   │   └── gist.py
│   │
│   ├── utils/
│   │   └── http_client.py
│   │
│   └── __init__.py
│
├── tests/
│   ├── test_home.py
│   ├── test_health.py
│   └── test_gists.py
│
├── requirements.txt
├── requirements-dev.txt
├── pytest.ini
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the repository
```
git clone <repo-url>
cd <project-folder>
```

### 2. Create virtual environment
```
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies
```
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

---

## ▶️ Running the Application

```
python3 -m uvicorn app.main:app --reload
```

Server will start at:
```
http://localhost:8000
```

---

## API Endpoints

### Home
```
GET /api/v1/
GET /api/v1/home
```

### Get User Gists
```
GET /api/v1/users/{username}
```

Example:
```
GET /api/v1/users/octocat
```

---

### Health Check
```
GET /health
```

## Running Tests

```
python3 -m pytest -v
```

---

### Readiness Check
```
GET /ready
```

---

## Sample Response of http://localhost:8000/api/v1/octocat

```
[
  {
    "id": "6cad326836d38bd3a7ae",
    "description": "Hello world!",
    "url": "https://gist.github.com/octocat/6cad326836d38bd3a7ae",
    "files": [
      "hello_world.rb"
    ]
  }
]
```

---

## API Documentation

Swagger UI:
```
http://localhost:8000/docs
```


---

## 🛠️ Requirements

- Python 3.9+
- pip

---

## Running with Docker (Multi-stage Build)

This project uses a multi-stage Docker build with:

- Builder stage → installs production dependencies  
- Test stage → runs all unit tests using requirements-dev.txt  
- Final stage → lightweight, secure runtime image  

---

### Build the Docker image

```
docker build -t github-gists-api .
```

During build:
- Tests are automatically executed inside the container  
- If any test fails → build will fail  
- If all tests pass → final image is created  

---

### (Optional) Run only tests

```
docker build --target test .
```
---

###  Run the container

```
docker run -d -p 8000:8000 github-gists-api
```
---

### Access the application

Base URL:
```
http://localhost:8000
```
