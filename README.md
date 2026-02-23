# API Testing Portfolio 🔌

REST API test suite using **Python Requests** and **pytest**, targeting the [Restful Booker API](https://restful-booker.herokuapp.com) — a purpose-built API for QA practice.

## 🧪 What's Being Tested

| Endpoint | Methods Tested |
|---|---|
| `/booking` | GET (all), POST (create) |
| `/booking/:id` | GET (by ID), PUT (update), PATCH (partial update), DELETE |
| `/auth` | POST (generate token) |
| `/ping` | GET (health check) |

### Test Coverage
- ✅ Status code validation (200, 201, 400, 403, 404)
- ✅ Response body schema validation
- ✅ Authentication token generation and usage
- ✅ CRUD operations — Create, Read, Update, Delete
- ✅ Negative tests — invalid data, missing fields, unauthorised requests
- ✅ Response time assertions

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| Python 3.x | Programming language |
| Requests | HTTP client library |
| pytest | Test framework |
| pytest-html | HTML test reports |

## 📁 Project Structure

```
api-testing-portfolio/
│
├── tests/
│   ├── __init__.py
│   ├── test_auth.py          # Authentication tests
│   ├── test_get_booking.py   # GET request tests
│   ├── test_create_booking.py # POST request tests
│   └── test_update_delete.py  # PUT/DELETE tests
│
├── conftest.py               # Shared fixtures (base URL, auth token)
├── requirements.txt          # Dependencies
└── README.md
```

## ⚙️ Setup & Run

### 1. Clone the repo
```bash
git clone https://github.com/kavyah44/api-testing-portfolio.git
cd api-testing-portfolio
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run all tests
```bash
pytest tests/ -v
```

### 4. Run with HTML report
```bash
pytest tests/ -v --html=reports/report.html
```

## 📸 Sample Test Output

```
tests/test_auth.py::test_generate_token PASSED
tests/test_get_booking.py::test_get_all_bookings PASSED
tests/test_get_booking.py::test_get_booking_by_id PASSED
tests/test_create_booking.py::test_create_booking_returns_201 PASSED
tests/test_create_booking.py::test_create_booking_response_schema PASSED
tests/test_update_delete.py::test_update_booking PASSED
tests/test_update_delete.py::test_delete_booking PASSED
```

## 📌 Key Concepts Demonstrated

- **Session management** — reusable auth tokens via pytest fixtures
- **Schema validation** — verifying response structure and data types
- **Negative testing** — invalid inputs, missing fields, bad auth
- **Response time assertions** — performance-aware tests
- **DRY fixtures** — shared setup with conftest.py
