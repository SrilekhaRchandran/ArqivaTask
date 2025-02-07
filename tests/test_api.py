import pytest
import requests


def test_api_status_code():
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    assert response.status_code == 200, "API did not return a 200 status code"


def test_api_response_content():
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    data = response.json()
    assert data["id"] == 1, "API response content is incorrect"
