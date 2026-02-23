import requests
import pytest

BASE_URL = "https://restful-booker.herokuapp.com"


class TestGetBookings:
    """Tests for GET /booking endpoints."""

    def test_get_all_bookings_returns_200(self, base_url):
        """Health check — GET all bookings returns 200."""
        response = requests.get(f"{base_url}/booking")
        assert response.status_code == 200

    def test_get_all_bookings_returns_list(self, base_url):
        """Response is a non-empty list of booking IDs."""
        response = requests.get(f"{base_url}/booking")
        data = response.json()
        assert isinstance(data, list)
        assert len(data) > 0

    def test_get_booking_by_id_returns_200(self, base_url):
        """GET a specific booking by ID returns 200."""
        bookings = requests.get(f"{base_url}/booking").json()
        booking_id = bookings[0]["bookingid"]
        response = requests.get(f"{base_url}/booking/{booking_id}")
        assert response.status_code == 200

    def test_get_booking_has_required_fields(self, base_url):
        """Booking response contains all required fields."""
        bookings = requests.get(f"{base_url}/booking").json()
        booking_id = bookings[0]["bookingid"]
        response = requests.get(f"{base_url}/booking/{booking_id}").json()
        assert "firstname" in response
        assert "lastname" in response
        assert "totalprice" in response
        assert "depositpaid" in response
        assert "bookingdates" in response

    def test_get_nonexistent_booking_returns_404(self, base_url):
        """GET a booking that doesn't exist returns 404."""
        response = requests.get(f"{base_url}/booking/999999")
        assert response.status_code == 404


class TestCreateBooking:
    """Tests for POST /booking endpoint."""

    def test_create_booking_returns_200(self, base_url, sample_booking):
        """POST creates a booking and returns 200."""
        response = requests.post(
            f"{base_url}/booking",
            json=sample_booking,
            headers={"Content-Type": "application/json"}
        )
        assert response.status_code == 200

    def test_create_booking_returns_id(self, base_url, sample_booking):
        """Response contains a bookingid."""
        response = requests.post(
            f"{base_url}/booking",
            json=sample_booking,
            headers={"Content-Type": "application/json"}
        ).json()
        assert "bookingid" in response
        assert isinstance(response["bookingid"], int)

    def test_create_booking_data_matches(self, base_url, sample_booking):
        """Created booking data matches what was sent."""
        response = requests.post(
            f"{base_url}/booking",
            json=sample_booking,
            headers={"Content-Type": "application/json"}
        ).json()
        booking = response["booking"]
        assert booking["firstname"] == sample_booking["firstname"]
        assert booking["lastname"] == sample_booking["lastname"]
        assert booking["totalprice"] == sample_booking["totalprice"]


class TestUpdateDeleteBooking:
    """Tests for PUT and DELETE /booking/:id endpoints."""

    def test_delete_booking_requires_auth(self, base_url, sample_booking):
        """DELETE without token returns 403."""
        booking_id = requests.post(
            f"{base_url}/booking",
            json=sample_booking,
            headers={"Content-Type": "application/json"}
        ).json()["bookingid"]
        response = requests.delete(f"{base_url}/booking/{booking_id}")
        assert response.status_code == 403

    def test_delete_booking_with_auth(self, base_url, auth_token, sample_booking):
        """DELETE with valid token returns 201."""
        booking_id = requests.post(
            f"{base_url}/booking",
            json=sample_booking,
            headers={"Content-Type": "application/json"}
        ).json()["bookingid"]
        response = requests.delete(
            f"{base_url}/booking/{booking_id}",
            headers={"Cookie": f"token={auth_token}"}
        )
        assert response.status_code == 201

    def test_ping_returns_201(self, base_url):
        """Health check endpoint returns 201."""
        response = requests.get(f"{base_url}/ping")
        assert response.status_code == 201
