from playwright.sync_api import Page
import base


def test_add_item_to_cart_from_item_details(page: Page):
    # Verify Add to cart from Item Details page
    base.login(page, 1)
    item_name = "Sauce Labs Backpack"
    page.locator("xpath=//div[@class='inventory_item_name' and text()='" + item_name + "']").click() # navigate to item details
    page.locator("xpath=//div[text()='" + item_name + "']/following-sibling::button[text()='Add to cart']").click()
    assert page.locator("xpath=//div[@id='shopping_cart_container']//span").inner_text() == "1", base.take_screenshot(page)  # checking if cart badge has appeared
    page.locator("xpath=//a[@class='shopping_cart_link']").click()
    assert page.locator("xpath=//div[@class='inventory_item_name']").inner_text() == item_name, base.take_screenshot(page)  # navigate to cart page to check if item is there
    page.locator("xpath=//div[text()='" + item_name + "']/../following-sibling::div//button").click() # remove item from cart
    base.logout(page)