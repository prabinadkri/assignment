
# 📝 Text Summarizer App

A FastAPI-based web app that uses Hugging Face Transformers to generate summaries for long texts. This project includes Docker support, GitHub Actions CI/CD, pre-commit hooks, and automated tests with pytest.

## 🚀 Features

- Summarizes long-form content using `facebook/bart-large-cnn`
- FastAPI backend with Jinja2 templates
- Stylish web interface with CSS
- Containerized with Docker
- CI pipeline with GitHub Actions
- Pre-commit hooks for code quality
- Unit testing using pytest

---

## 📦 Quick Start

### 🔧 Prerequisites

- Docker and Docker Compose
- Python 3.10+
- `pre-commit` CLI

### 🐳 Run with Docker Compose

```bash
docker-compose up --build
````

Visit: [http://localhost:8000](http://localhost:8000)

### 🧪 Run Locally Without Docker

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

---

## 🧬 Project Structure

```
project_root/
├── app/
│   ├── main.py           # FastAPI app entry
│   ├── summarizer.py     # Summarization logic using HuggingFace
├── static/style.css      # App styling
├── templates/index.html  # Web UI
├── tests/test_main.py    # Pytest test cases
├── .env                  # Environment variables
├── Dockerfile            # Docker image definition
├── docker-compose.yml    # Service orchestration
├── pre-commit-config.yaml# Code quality hooks
└── .github/workflows/ci.yml # GitHub Actions
```

---

## 🔑 .env

```env
MODEL_NAME=facebook/bart-large-cnn
```

---

## 🧪 Testing

Run tests using:

```bash
pytest
```

Expected test coverage:

* Homepage loads successfully
* Summarization returns output for long text

---

## ✅ Pre-commit Hooks

```bash
pip install pre-commit
pre-commit install
pre-commit run --all-files
```

Includes:

* Black formatting
* Flake8 linting
* Whitespace cleanup

---

## ⚙️ GitHub Actions CI/CD

Location: `.github/workflows/ci.yml`

Triggers on `push`/`pull_request` to `main` branch:

* Sets up Python environment
* Installs dependencies
* Runs tests with pytest
* Runs pre-commit checks

---

## 🐳 Docker Details

**Dockerfile**

Builds app with FastAPI and Python.

**docker-compose.yml**

Simplifies running the app with one command and loads `.env`.

---

```

Let me know if you'd like badges or deployment instructions added.
```
