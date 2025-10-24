# tests/test_e2e.py

import pytest
from playwright.sync_api import Page, expect

# We use 'page' and 'base_url' which are special
# fixtures provided by the pytest-playwright plugin.
# 'base_url' must be provided when running the test.

def test_add_operation_in_browser(page: Page, base_url: str):
    # 1. Go to the homepage of the app
    page.goto(base_url)

    # 2. Find the input fields and fill them out
    page.fill("input#num1", "10")
    page.fill("input#num2", "20")

    # 3. Click the "Add" button
    page.click("button#add-button")

    # 4. Find the result element and check its text
    result_element = page.locator("h2#result-text")
    
    # expect() will wait for the text to appear
    expect(result_element).to_have_text("Result: 30.0")

def test_divide_by_zero_in_browser(page: Page, base_url: str):
    # 1. Go to the homepage
    page.goto(base_url)

    # 2. Fill in numbers for division by zero
    page.fill("input#num1", "10")
    page.fill("input#num2", "0")

    # 3. Click the "Divide" button
    page.click("button#divide-button")

    # 4. Find the result element and check for the error message
    result_element = page.locator("h2#result-text")
    expect(result_element).to_have_text("Error: Cannot divide by zero")