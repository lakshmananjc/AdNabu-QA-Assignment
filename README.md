# AdNabu QA Automation Assignment

## Overview

This project contains automated UI test cases for the AdNabu Shopify store using:

- Python
- Selenium WebDriver
- Pytest

The automation covers:

1. Open Shopify store
2. Enter storefront password
3. Search product
4. Open product page
5. Add product to cart
6. Verify product added successfully

---

# Project Structure

AdNabu-QA-Assignment/
│
├── tests/
│   └── test_add_to_cart.py
│
├── screenshots/
│
├── reports/
│
├── requirements.txt
├── README.md
└── .gitignore

---

# Prerequisites

Install the following before running tests:

- Python 3.10+
- Google Chrome Browser
- Git
- VS Code (recommended)

---

# Setup Instructions

## 1. Clone Repository

```bash
git clone https://github.com/lakshmananjc/AdNabu-QA-Assignment.git

2. Navigate to Project Folder
cd AdNabu-QA-Assignment

3. Create Virtual Environment
Windows
python -m venv venv

4. Activate Virtual Environment
Windows
venv\Scripts\activate

5. Install Dependencies
python -m pip install -r requirements.txt
Running Automated Tests

Run the following command:

python -m pytest tests/test_add_to_cart.py -v
Generate HTML Test Report

Install pytest-html:

pip install pytest-html

Run:

pytest tests/test_add_to_cart.py --html=reports/report.html

Generated report location:

reports/report.html
Test Scenario

The automated test performs:

Open AdNabu Shopify store
Enter storefront password
Search for "Multi-location Snowboard"
Open product page
Click "Add to cart"
Verify product added successfully
Failure Screenshots

Failure screenshots are automatically captured inside:

screenshots/
Dependencies

requirements.txt contains:

selenium
webdriver-manager
pytest
pytest-html


Author

Jayachithra