import pytest
from app import app, db

@pytest.fixture
def client():
    """Set up test client with in-memory SQLite database"""
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"

    with app.app_context():
        db.create_all()
        yield app.test_client()
        db.drop_all()

# ─── Tests ────────────────────────────────────────

def test_home(client):
    """Test home endpoint returns 200"""
    response = client.get("/")
    assert response.status_code == 200

def test_health(client):
    """Test health endpoint returns healthy status"""
    response = client.get("/health")
    assert response.status_code == 200
    data = response.get_json()
    assert data["status"] == "healthy"

def test_get_users_empty(client):
    """Test users endpoint returns empty list initially"""
    response = client.get("/users")
    assert response.status_code == 200
    assert response.get_json() == []

def test_create_user(client):
    """Test creating a user successfully"""
    response = client.post("/users",
        json={"name": "John Doe", "email": "john@example.com"}
    )
    assert response.status_code == 201
    data = response.get_json()
    assert data["name"] == "John Doe"
    assert data["email"] == "john@example.com"
    assert "id" in data

def test_get_users_after_create(client):
    """Test users list after creating a user"""
    # Create a user first
    client.post("/users",
        json={"name": "Jane Doe", "email": "jane@example.com"}
    )
    # Now fetch all users
    response = client.get("/users")
    assert response.status_code == 200
    data = response.get_json()
    assert len(data) == 1
    assert data[0]["name"] == "Jane Doe"
