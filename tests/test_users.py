import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from utils.api_client import get

def test_get_users_status():
    response = get("/users")
    assert response.status_code == 200

def test_users_data_not_empty():
    response = get("/users")
    data = response.json()
    assert len(data) > 0

def test_user_has_required_fields():
    response = get("/users")
    user = response.json()[0]

    assert "id" in user
    assert "name" in user
    assert "email" in user
    
def test_response_time():
    response = get("/users")
    assert response.elapsed.total_seconds() < 1