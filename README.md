# 🚀 Python Request API Automation Framework

![Python](https://img.shields.io/badge/Python-3.12+-blue.svg)
![Pytest](https://img.shields.io/badge/Pytest-9.x-green.svg)
![Requests](https://img.shields.io/badge/Requests-HTTP-orange.svg)
![Allure](https://img.shields.io/badge/Allure-Report-red.svg)
![License](https://img.shields.io/badge/License-MIT-blue.svg)

A scalable, production-ready REST API Automation Framework built using **Python**, **Pytest**, and **Requests**.

The framework is designed following industry best practices and can easily scale for **microservice-based applications** such as Ride Sharing, Courier, Banking, E-commerce, etc.

---

# ✨ Features

- REST API Automation
- Generic API Client
- Environment Configuration
- Centralized Endpoint Management
- Data Driven Testing (DDT)
- Pytest Fixtures
- JSON Test Data
- Logging
- HTML Report
- Allure Report
- Smoke / Sanity / Regression Suite
- Assertion Helpers
- Reusable Architecture
- Easy to Extend

---

# 🛠 Technology Stack

| Tool | Purpose |
|------|----------|
| Python | Programming Language |
| Pytest | Test Runner |
| Requests | REST API Client |
| Pytest HTML | HTML Reporting |
| Allure | Advanced Reporting |
| Logging | API Logging |
| JSON | Test Data |
| Git | Version Control |

---

# 📂 Project Structure

```text
python-request-api-automation
│
├── config
│   ├── __init__.py
│   ├── settings.py
│   ├── end_points.py
│   └── http_methods.py
│
├── logs
│   └── api.log
│
├── reports
│
├── allure-results
│
├── allure-report
│
├── testdata
│   └── booking
│       ├── auth_payload.json
│       ├── create_booking.json
│       └── update_booking_payload.json
│
├── tests
│   ├── booking
│   ├── auth
│   └── scenarios
│
├── utils
│   ├── logger.py
│   ├── json_loader.py
│   └── booking_assertion_helper.py
│
├── api_client.py
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md
```

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/<your_username>/python-request-api-automation.git

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

# 📦 Required Python Packages

```bash
pip install pytest
pip install requests
pip install pytest-html
pip install allure-pytest
pip install python-dotenv
```

---

# 📦 requirements.txt

```text
requests
pytest
pytest-html
allure-pytest
python-dotenv
```

Install all dependencies

```bash
pip install -r requirements.txt
```

---

# ☕ Java Requirement

Allure requires Java.

Verify Java installation

```bash
java -version
```

---

# 📊 Install Allure Command Line

> Installing `allure-pytest` is **not enough**.  
> You also need the **Allure Command Line**.

Official Releases

https://github.com/allure-framework/allure2/releases

Verify Installation

```bash
allure --version
```

---

# ⚙ Configuration

Base URL is stored inside

```text
config/settings.py
```

Example

```python
BASE_URL = "https://restful-booker.herokuapp.com"
```

---

# 🌐 Endpoint Management

All endpoints are maintained in one place.

```python
class EndPoint:

    AUTH="/auth"

    BOOKING="/booking"
```

Advantages

- Easy Maintenance
- No Hardcoded URLs
- Reusable

---

# 🌐 HTTP Methods

```python
class HttpMethod:

    GET="GET"

    POST="POST"

    PUT="PUT"

    PATCH="PATCH"

    DELETE="DELETE"
```

---

# 🚀 Generic API Client

Framework uses one generic request function.

```python
response = client.request(
    method=HttpMethod.GET,
    endpoint=EndPoint.BOOKING
)
```

Benefits

- Less Code
- Reusable
- Easy Maintenance

---

# 📁 Data Driven Testing (DDT)

Test data is stored in JSON.

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

Load JSON

```python
from utils.json_loader import load_json

payload = load_json("testdata/booking/create_booking.json")
```

---

# 🧩 Pytest Fixtures

Reusable objects are managed using fixtures.

Example

```python
@pytest.fixture(scope="session")
def client():

    return ApiClient()
```

Authentication

```python
@pytest.fixture(scope="session")
def auth_token():

    ...
```

Benefits

- Cleaner Tests
- Reusable Objects
- No Duplicate Login

---

# 📝 Logging

Every API request is automatically logged.

Location

```text
logs/api.log
```

Logged Information

- HTTP Method
- URL
- Headers
- Query Parameters
- Payload
- Status Code
- Response Body

Example

```text
REQUEST METHOD : POST

URL : https://....

HEADERS : ...

PAYLOAD : ...

STATUS : 200

RESPONSE : ...
```

---

# 🧪 Test Suites

Pytest markers are used to organize execution.

Example

```python
@pytest.mark.smoke
@pytest.mark.booking
def test_create_booking():
```

```python
@pytest.mark.sanity
@pytest.mark.booking
def test_update_booking():
```

```python
@pytest.mark.regression
@pytest.mark.booking
def test_delete_booking():
```

---

# ▶ Running Tests

## Run All Tests

```bash
pytest
```

---

## Run Specific File

```bash
pytest tests/test_create_booking.py
```

---

## Verbose Mode

```bash
pytest -v
```

---

## Show Print Statements

```bash
pytest -v -s
```

---

# 🏷 Running Test Suites

## Smoke

```bash
pytest -m smoke
```

---

## Sanity

```bash
pytest -m sanity
```

---

## Regression

```bash
pytest -m regression
```

---

## Booking Service

```bash
pytest -m booking
```

---

## Smoke OR Sanity

```bash
pytest -m "smoke or sanity"
```

---

## Smoke AND Booking

```bash
pytest -m "smoke and booking"
```

---

## Exclude Regression

```bash
pytest -m "not regression"
```

---

# 📊 HTML Report

Generate HTML Report

```bash
pytest \
--html=reports/report.html \
--self-contained-html
```

---

## HTML Report + Smoke Suite

```bash
pytest \
-m smoke \
--html=reports/report.html \
--self-contained-html
```

---

## HTML Report + Sanity Suite

```bash
pytest \
-m sanity \
--html=reports/report.html \
--self-contained-html
```

---

# 🚀 Allure Report

## Generate Result Files

```bash
pytest --alluredir=allure-results
```

---

## Smoke Suite

```bash
pytest \
-m smoke \
--alluredir=allure-results
```

---

## Sanity Suite

```bash
pytest \
-m sanity \
--alluredir=allure-results
```

---

## Smoke OR Sanity

```bash
pytest \
-m "smoke or sanity" \
--alluredir=allure-results
```

---

## Booking Smoke Tests

```bash
pytest \
-m "smoke and booking" \
--alluredir=allure-results
```

---

## Generate Allure Report

```bash
allure generate allure-results -o allure-report --clean
```

---

## Open Report

```bash
allure open allure-report
```

---

## Generate & Open Automatically

```bash
allure serve allure-results
```

---

# 📋 Complete Workflow

Run Smoke Suite

```bash
pytest \
-m smoke \
--alluredir=allure-results
```

Generate Report

```bash
allure generate allure-results -o allure-report --clean
```

Open Report

```bash
allure open allure-report
```

Or simply

```bash
allure serve allure-results
```

---

# 🧪 Assertions

Assertions are centralized.

Example

```python
BookingAssertion.verify_booking(
    response,
    payload
)
```

Benefits

- Reusable
- Less Duplicate Code
- Cleaner Tests

---

# 📚 APIs Covered

- Authentication
- Get All Bookings
- Get Booking By ID
- Create Booking
- Update Booking

---

# 🏗 Framework Architecture

```text
                 Test Case
                     │
                     ▼
               Pytest Fixture
                     │
                     ▼
                API Client
                     │
                     ▼
                 Requests
                     │
                     ▼
                  REST API
```

---

# 🚀 Future Improvements

- Service Layer
- Base Service
- Token Manager
- JSON Schema Validation
- Retry Mechanism
- Custom Exceptions
- Response Time Validation
- Parallel Execution
- Multi Environment Support
- Docker
- Jenkins
- GitHub Actions
- Slack Notification
- Report History

---

# ✅ Best Practices Followed

- Generic API Client
- Single Responsibility Principle
- Centralized Endpoints
- Environment Configuration
- Data Driven Testing
- Pytest Fixtures
- Logging
- HTML Report
- Allure Report
- Marker Based Execution
- Assertion Helpers

---

# 👨‍💻 Author

**Shobuj Das**

QA Automation Engineer

- Python
- API Automation
- REST API
- Pytest
- Requests
- Performance Testing

---

# ⭐ Support

If you found this project useful, please consider giving it a ⭐ on GitHub.

Happy Testing! 🚀