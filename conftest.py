import pytest
import requests

BASE_URL = "https://restful-booker.herokuapp.com"


@pytest.fixture(scope="session")
def base_url():
    return BASE_URL


@pytest.fixture(scope="session")
def auth_token(base_url):
    """Generate and cache an auth token for the full test session."""
    response = requests.post(
        f"{base_url}/auth",
        json={"username": "admin", "password": "password123"},
        headers={"Content-Type": "application/json"}
    )
    return response.json().get("token")


@pytest.fixture
def sample_booking():
    """Return sample booking payload for use in tests."""
    return {
        "firstname": "Kavya",
        "lastname": "Test",
        "totalprice": 150,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2025-01-01",
            "checkout": "2025-01-07"
        },
        "additionalneeds": "Breakfast"
    }
