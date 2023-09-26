from playwright.sync_api import Page
import base


def test_checkout_single_item_from_cart(page: Page):
    # Verify checkout single item from Cart page
    base.login(page, 1)
    item_name = "Sauce Labs Backpack"
    page.locator("xpath=//div[text()='" + item_name + "']/../../following-sibling::div//button[text()='Add to cart']").click()
    page.locator("xpath=//a[@class='shopping_cart_link']").click()
    page.get_by_text("Checkout").click()
    page.get_by_placeholder("First Name").fill("Test")
    page.get_by_placeholder("Last Name").fill("User")
    page.get_by_placeholder("Zip/Postal Code").fill("1234")
    page.get_by_text("Continue").click()
    assert page.locator("xpath=//span[@class='title']").inner_text() == "Checkout: Overview", base.take_screenshot(page)
    page.get_by_text("Finish").click()
    assert page.locator("xpath=//h2").inner_text() == "Thank you for your order!", base.take_screenshot(page)
    base.logout(page)


def test_checkout_multiple_items_from_cart(page: Page):
    # Verify checkout multiple items from Cart page
    base.login(page, 1)
    item_name_1 = "Sauce Labs Backpack"
    item_name_2 = "Sauce Labs Bike Light"
    item_name_3 = "Sauce Labs Bolt T-Shirt"
    page.locator("xpath=//div[text()='" + item_name_1 + "']/../../following-sibling::div//button[text()='Add to cart']").click() # add item 1 to cart
    page.locator("xpath=//a[@class='shopping_cart_link']").click() # navigate to cart
    page.get_by_text("Continue Shopping").click() # navigate back to inventory
    page.locator("xpath=//div[text()='" + item_name_2 + "']/../../following-sibling::div//button[text()='Add to cart']").click() # add item 2 to cart
    page.locator("xpath=//div[text()='" + item_name_3 + "']/../../following-sibling::div//button[text()='Add to cart']").click() # add item 3 to cart
    page.locator("xpath=//a[@class='shopping_cart_link']").click()
    page.locator("xpath=//div[text()='" + item_name_2 + "']/../following-sibling::div//button").click()  # remove item 2 from cart
    page.get_by_text("Checkout").click()
    page.get_by_placeholder("First Name").fill("Test")
    page.get_by_placeholder("Last Name").fill("User")
    page.get_by_placeholder("Zip/Postal Code").fill("1234")
    page.get_by_text("Continue").click()
    page.get_by_text("Cancel").click() # navigate back to inventory
    page.locator("xpath=//a[@class='shopping_cart_link']").click() # navigate to cart again
    assert page.locator("xpath=(//div[@class='inventory_item_name'])[1]").inner_text() == item_name_1, base.take_screenshot(page) # varify if item 1 is still in cart
    assert page.locator("xpath=(//div[@class='inventory_item_name'])[2]").inner_text() == item_name_3, base.take_screenshot(page) # varify if item 3 is still in cart
    page.get_by_text("Checkout").click()
    page.get_by_placeholder("First Name").fill("Test")
    page.get_by_placeholder("Last Name").fill("User")
    page.get_by_placeholder("Zip/Postal Code").fill("1234")
    page.get_by_text("Continue").click()
    item_1_price = float(page.locator("xpath=//div[text()='" + item_name_1 + "']/../following-sibling::div/div").inner_text()[1:])
    item_3_price = float(page.locator("xpath=//div[text()='" + item_name_3 + "']/../following-sibling::div/div").inner_text()[1:])
    total_price = item_1_price + item_3_price
    assert float(page.locator("xpath=//div[@class='summary_subtotal_label']").inner_text()[-5:]) == total_price, base.take_screenshot(page) # verify if the total without tax is correct
    page.get_by_text("Finish").click()
    assert page.locator("xpath=//h2").inner_text() == "Thank you for your order!", base.take_screenshot(page)
    page.get_by_text("Back Home").click()
    base.logout(page)




