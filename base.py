from playwright.sync_api import Page
import time


def take_screenshot(page: Page):
    # Take Screenshot
    page.screenshot(path="./img/ss/" + time.ctime().replace(':', '').replace(' ', '_') + ".png")