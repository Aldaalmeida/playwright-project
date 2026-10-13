from playwright.sync_api import Page, expect
import time

def test_login_successful(page: Page) -> None:
    page.goto("https://leogcarvalho.github.io/test-automation-practice/")
    page.get_by_role("textbox", name="Username: (admin)").click()
    page.get_by_role("textbox", name="Username: (admin)").fill("admin")
    page.get_by_role("textbox", name="Username: (admin)").press("Enter")
    page.get_by_role("textbox", name="Password: (1234)").fill("1234")
    page.get_by_role("textbox", name="Password: (1234)").press("Enter")
    page.get_by_role("button", name="Login").click()
    expect(page.get_by_text("Login successful!")).to_be_visible()
    time.sleep(4)
    