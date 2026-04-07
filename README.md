# 🐳 Flask + PostgreSQL + Docker

A simple REST API built with Flask and PostgreSQL, containerized with Docker.

## 🚀 Quick Start
```bash
docker compose up --build -d
```

## 📡 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /health | Health check |
| GET | /users | Get all users |
| POST | /users | Create a user |

## 🧪 Test API
```bash
# Health check
curl http://localhost:5000/health

# Create user
curl -X POST http://localhost:5000/users \
  -H "Content-Type: application/json" \
  -d '{"name": "John", "email": "john@example.com"}'

# Get users
curl http://localhost:5000/users
```
