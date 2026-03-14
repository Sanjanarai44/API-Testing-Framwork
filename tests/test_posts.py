import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from utils.api_client import get, post

def test_get_posts_status():
    response = get("/posts")
    assert response.status_code == 200

def test_create_post():
    payload = {
        "title": "SDET test",
        "body": "testing api",
        "userId": 1
    }

    response = post("/posts", payload)

    assert response.status_code == 201
    assert response.json()["title"] == "SDET test"