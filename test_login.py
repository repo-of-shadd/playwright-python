from playwright.sync_api import Page
import pytest
import base


def test_page_navigation(page: Page):
    # Page navigation
    page.goto(url="https://www.saucedemo.com/")
    assert page.title() == "Swag Labs", base.take_screenshot(page)


def test_empty_login(page: Page):
    # Click login button without providing any input
    page.goto(url="https://www.saucedemo.com/")
    page.locator("xpath=//input[@id='login-button']").click()
    assert page.locator("xpath=//h3").inner_text() == "Epic sadface: Username is required", base.take_screenshot(page)


def test_navigate_to_inventory_without_logging_in(page: Page):
    # Navigate to /inventory.html without logging in
    page.goto(url="https://www.saucedemo.com/inventory.html")
    error_message = "Epic sadface: You can only access '/inventory.html' when you are logged in."
    assert page.locator("xpath=//h3").inner_text() == error_message, base.take_screenshot(page)


def test_login_with_standard_user(page: Page):
    # Log in with standard user
    page.goto(url="https://www.saucedemo.com/")
    username = page.locator("xpath=//div[@id='login_credentials']").inner_text().split('\n')[1]
    password = page.locator("xpath=//div[@class='login_password']").inner_text().split('\n')[1]
    page.locator("xpath=//input[@placeholder='Username']").fill(value=username)
    page.locator("xpath=//input[@placeholder='Password']").fill(value=password)
    page.locator("xpath=//input[@id='login-button']").click()
    assert page.locator("xpath=//div[@class='header_label']/div").inner_text() == "Swag Labs", base.take_screenshot(page)


def test_login_with_locked_out_user(page: Page):
    # Log in with locked out user
    page.goto(url="https://www.saucedemo.com/")
    username = page.locator("xpath=//div[@id='login_credentials']").inner_text().split('\n')[2]
    password = page.locator("xpath=//div[@class='login_password']").inner_text().split('\n')[1]
    page.locator("xpath=//input[@placeholder='Username']").fill(value=username)
    page.locator("xpath=//input[@placeholder='Password']").fill(value=password)
    page.locator("xpath=//input[@id='login-button']").click()
    error_message = "Epic sadface: Sorry, this user has been locked out."
    assert page.locator("xpath=//h3").inner_text() == error_message, base.take_screenshot(page)


def test_login_with_performance_glitch_user(page: Page):
    # Log in with performance glitch user
    page.goto(url="https://www.saucedemo.com/")
    username = page.locator("xpath=//div[@id='login_credentials']").inner_text().split('\n')[4]
    password = page.locator("xpath=//div[@class='login_password']").inner_text().split('\n')[1]
    page.locator("xpath=//input[@placeholder='Username']").fill(value=username)
    page.locator("xpath=//input[@placeholder='Password']").fill(value=password)
    page.locator("xpath=//input[@id='login-button']").click()
    assert page.locator("xpath=//div[@class='header_label']/div").inner_text() == "Swag Labs", base.take_screenshot(page)

