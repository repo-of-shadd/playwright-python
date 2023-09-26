from playwright.sync_api import Page
import base


def test_inventory_page_title(page: Page):
    # Navigate to Inventory page and verify page title
    base.login(page, 1)
    assert page.title() == "Swag Labs", base.take_screenshot(page)
    base.logout(page)


def test_item_page_navigation_by_item_name(page: Page):
    # Navigate to Item Details page by clicking specific Item Name
    base.login(page, 1)
    item_name = "Sauce Labs Backpack"
    page.locator("xpath=//div[@class='inventory_item_name' and text()='" + item_name + "']").click()
    # page.wait_for_timeout(1000)
    assert page.locator("xpath=//div[@class='inventory_details_name large_size']").inner_text() == item_name, base.take_screenshot(page)
    base.logout(page)


def test_item_page_navigation_by_item_img(page: Page):
    # Navigate to Item Details page by clicking specific Item Image
    base.login(page, 1)
    item_name = "Sauce Labs Backpack"
    page.locator("xpath=//img[@alt='" + item_name + "']").click()
    assert page.locator("xpath=//div[@class='inventory_details_name large_size']").inner_text() == item_name, base.take_screenshot(page)
    base.logout(page)


def test_add_to_cart_from_inventory(page: Page):
    # Add specific item to cart from Inventory
    base.login(page, 1)
    item_name = "Sauce Labs Backpack"
    page.locator("xpath=//div[text()='" + item_name + "']/../../following-sibling::div//button[text()='Add to cart']").click()
    assert page.locator("xpath=//div[@id='shopping_cart_container']//span").inner_text() == "1", base.take_screenshot(page) # checking if cart badge has appeared
    page.locator("xpath=//a[@class='shopping_cart_link']").click()
    assert page.locator("xpath=//div[@class='inventory_item_name']").inner_text() == item_name, base.take_screenshot(page) # navigate to cart page to check if item is there
    page.locator("xpath=//div[text()='" + item_name + "']/../following-sibling::div//button").click() # remove item from cart
    base.logout(page)


def test_inventory_sorting(page: Page):
    # Verify the sorting functionality in Inventory Page
    base.login(page, 1)
    alphabatically_1st_item = "Sauce Labs Backpack"
    alphabatically_last_item = "Test.allTheThings() T-Shirt (Red)"
    lowest_priced_item = "Sauce Labs Onesie"
    highest_priced_item = "Sauce Labs Fleece Jacket"
    page.locator("xpath=//select[@class='product_sort_container']").select_option("hilo")
    assert page.locator("xpath=(//div[@class='inventory_item_description'])[1]//div[@class='inventory_item_name']").inner_text() == highest_priced_item, base.take_screenshot(page)
    page.locator("xpath=//select[@class='product_sort_container']").select_option("lohi")
    assert page.locator("xpath=(//div[@class='inventory_item_description'])[1]//div[@class='inventory_item_name']").inner_text() == lowest_priced_item, base.take_screenshot(page)
    page.locator("xpath=//select[@class='product_sort_container']").select_option("za")
    assert page.locator("xpath=(//div[@class='inventory_item_description'])[1]//div[@class='inventory_item_name']").inner_text() == alphabatically_last_item, base.take_screenshot(page)
    page.locator("xpath=//select[@class='product_sort_container']").select_option("az")
    assert page.locator("xpath=(//div[@class='inventory_item_description'])[1]//div[@class='inventory_item_name']").inner_text() == alphabatically_1st_item, base.take_screenshot(page)
    base.logout(page)
