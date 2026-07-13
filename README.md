# Python Request API Automation Framework

A scalable, production-ready REST API automation framework built with **Python**, **Pytest**, and **Requests**.

The framework follows industry best practices and is designed to support **microservice-based applications** by keeping APIs organized, reusable, and maintainable.

---

# Features

- REST API Automation
- Generic API Client
- Environment Configuration
- Centralized Endpoint Management
- Data Driven Testing (DDT)
- JSON Test Data
- Pytest Fixtures
- Custom Assertion Helpers
- Logging
- HTML Reporting (pytest-html)
- Allure Reporting
- Smoke / Sanity / Regression Test Suites
- Easy to Extend for Microservices

---

# Tech Stack

| Tool | Purpose |
|------|----------|
| Python | Programming Language |
| Pytest | Test Framework |
| Requests | HTTP Client |
| Pytest HTML | HTML Report |
| Allure | Advanced Test Reporting |
| Logging | Request & Response Logging |
| JSON | Test Data |
| Git | Version Control |

---

# Project Structure

```text
python-request-api-automation/
│
├── config/
│   ├── end_points.py
│   ├── http_methods.py
│   ├── settings.py
│   └── __init__.py
│
├── logs/
│   └── api.log
│
├── reports/
│
├── testdata/
│   └── booking/
│       ├── auth_payload.json
│       ├── create_booking.json
│       └── update_booking_payload.json
│
├── tests/
│   ├── test_get_all_bookings.py
│   ├── test_get_booking_by_id.py
│   ├── test_create_booking.py
│   └── test_update_booking.py
│
├── utils/
│   ├── json_loader.py
│   ├── booking_assertion_helper.py
│   └── logger.py
│
├── api_client.py
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md
```

---

# Installation

## Clone Repository

```bash
git clone <repository-url>

cd python-request-api-automation
```

---

## Create Virtual Environment

### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Python Packages

Install manually if required.

```bash
pip install pytest
pip install requests
pip install pytest-html
pip install allure-pytest
pip install python-dotenv
```

---

# Install Allure Command Line

> **Note**
>
> `allure-pytest` only generates the result files.
>
> To generate the HTML report, install the **Allure Command Line**.

Official Download:

https://github.com/allure-framework/allure2/releases

After installation verify:

```bash
allure --version
```

---

# Configuration

Base URL is stored in

```text
config/settings.py
```

Example

```python
BASE_URL = "https://restful-booker.herokuapp.com"
```

---

# Endpoint Management

Endpoints are maintained in one place.

```python
class EndPoint:

    AUTH = "/auth"
    BOOKING = "/booking"
```

This prevents hardcoding URLs throughout the framework.

---

# HTTP Methods

```python
class HttpMethod:

    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    PATCH = "PATCH"
    DELETE = "DELETE"
```

---

# API Client

The framework uses a single generic request method.

```python
response = client.request(
    method=HttpMethod.GET,
    endpoint=EndPoint.BOOKING
)
```

Advantages

- No duplicate code
- Easy maintenance
- Reusable across all services

---

# Data Driven Testing (DDT)

Test data is stored in JSON files.

Example

```json
[
    {
        "firstname":"Jim",
        "lastname":"Brown"
    },
    {
        "firstname":"John",
        "lastname":"Doe"
    }
]
```

Loaded using

```python
from utils.json_loader import load_json

payload = load_json("testdata/booking/create_booking.json")
```

---

# Fixtures

Shared objects are managed using Pytest Fixtures.

Example

```python
@pytest.fixture(scope="session")
def client():
    return ApiClient()
```

Authentication token

```python
@pytest.fixture(scope="session")
def auth_token(client):
    ...
```

Benefits

- No duplicate login
- Cleaner tests
- Reusable objects

---

# Logging

Every API request and response is automatically logged.

Location

```text
logs/api.log
```

Logged Information

- Request URL
- Method
- Headers
- Payload
- Response Status
- Response Body

---

# Test Suites

Pytest Markers

```python
@pytest.mark.smoke

@pytest.mark.sanity

@pytest.mark.regression

@pytest.mark.booking
```

Run Smoke Suite

```bash
pytest -m smoke
```

Run Sanity Suite

```bash
pytest -m sanity
```

Run Regression Suite

```bash
pytest -m regression
```

Run Booking Tests

```bash
pytest -m booking
```

---

# Running Tests

Run all tests

```bash
pytest
```

Verbose mode

```bash
pytest -v
```

With console output

```bash
pytest -v -s
```

Run single test

```bash
pytest tests/test_create_booking.py -v -s
```

---

# HTML Report

Generate report

```bash
pytest --html=reports/report.html --self-contained-html
```

Timestamp Example

Linux

```bash
timestamp=$(date +"%Y-%m-%d_%H-%M-%S")

pytest \
--html="reports/report_$timestamp.html" \
--self-contained-html
```

Windows PowerShell

```powershell
$timestamp = Get-Date -Format "yyyy-MM-dd_HH-mm-ss"

pytest `
--html="reports/report_$timestamp.html" `
--self-contained-html
```

---

# Allure Report

Generate Result

```bash
pytest --alluredir=allure-results
```

Generate Report

```bash
allure generate allure-results -o allure-report --clean
```

Open Report

```bash
allure open allure-report
```

Or

```bash
allure serve allure-results
```

---

# Assertion Helper

Assertions are centralized.

Example

```python
BookingAssertion.verify_booking(response, payload)
```

Benefits

- Less duplicate assertions
- Better maintainability

---

# Current APIs Covered

- Authentication
- Get All Bookings
- Get Booking by ID
- Create Booking
- Update Booking

---

# Framework Design

```text
Test
    │
    ▼
Fixture
    │
    ▼
API Client
    │
    ▼
Requests Library
    │
    ▼
REST API
```

---

# Future Improvements

- Booking Service Layer
- Base Service
- Token Manager
- Schema Validation
- Response Time Validation
- Retry Mechanism
- Custom Exceptions
- Parallel Execution
- CI/CD Integration
- Docker Support
- Jenkins Integration
- GitHub Actions
- Slack Notifications

---

# Best Practices Followed

- Single Responsibility Principle
- Reusable API Client
- Centralized Endpoints
- External Test Data
- Data Driven Testing
- Pytest Fixtures
- Logging
- Reporting
- Marker Based Execution

---

# Author

**Shobuj Das**

QA Automation Engineer

Python | API Automation | Pytest | Requests | REST API | Performance Testing
