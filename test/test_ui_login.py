from playwright.sync_api import sync_playwright

def test_valid_login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Simulated login page (replace with your frontend URL if needed)
        page.goto("https://www.saucedemo.com/")
        page.fill("input[data-test='username']", "standard_user")
        page.fill("input[data-test='password']", "secret_sauce")
        page.click("input[data-test='login-button']")

        # Assert that we reached the inventory page
        assert "inventory" in page.url
        browser.close()

def test_invalid_login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        page.goto("https://www.saucedemo.com/")
        page.fill("input[data-test='username']", "locked_out_user")
        page.fill("input[data-test='password']", "secret_sauce")
        page.click("input[data-test='login-button']")

        # Wait for error message
        page.wait_for_selector("h3[data-test='error']", timeout=5000)
        error_text = page.locator("h3[data-test='error']").text_content()
        assert "locked out" in error_text.lower()

        browser.close()
