from playwright.sync_api import sync_playwright

def test_booking_flow():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Step 1: Login
        page.goto("https://www.saucedemo.com/")
        page.fill("input[data-test='username']", "standard_user")
        page.fill("input[data-test='password']", "secret_sauce")
        page.click("input[data-test='login-button']")
        assert "inventory" in page.url

        # Step 2: Add item to cart (simulate room selection)
        page.click("button[data-test='add-to-cart-sauce-labs-backpack']")

        # Step 3: Go to cart
        page.click(".shopping_cart_link")
        assert page.locator(".cart_item").count() == 1

        # Step 4: Proceed to checkout
        page.click("button[data-test='checkout']")

        # Step 5: Enter checkout info (simulate guest details)
        page.fill("input[data-test='firstName']", "Asad")
        page.fill("input[data-test='lastName']", "Rahoo")
        page.fill("input[data-test='postalCode']", "94032")
        page.click("input[data-test='continue']")

        # Step 6: Confirm booking
        page.click("button[data-test='finish']")

        # Step 7: Verify booking confirmation
        confirmation = page.locator(".complete-header").text_content()
        assert "thank you" in confirmation.lower()

        browser.close()
