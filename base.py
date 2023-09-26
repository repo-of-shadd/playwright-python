from playwright.sync_api import Page
import time


def take_screenshot(page: Page):
    # Take Screenshot
    page.screenshot(path="./img/ss/" + time.ctime().replace(':', '').replace(' ', '_') + ".png")


def login(page: Page, user):
    # Page navigation
    page.goto(url="https://www.saucedemo.com/")
    # Log in with Standard User
    username = page.locator("xpath=//div[@id='login_credentials']").inner_text().split('\n')[user]
    password = page.locator("xpath=//div[@class='login_password']").inner_text().split('\n')[1]
    page.locator("xpath=//input[@placeholder='Username']").fill(value=username)
    page.locator("xpath=//input[@placeholder='Password']").fill(value=password)
    page.locator("xpath=//input[@id='login-button']").click()


def logout(page: Page):
    # Log out
    page.locator("xpath=//button[@id='react-burger-menu-btn']").click()
    page.locator("xpath=//a[text()='Logout']").click()
