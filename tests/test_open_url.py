from playwright.sync_api import Page, expect
import time

def test_open_url(page:Page) :
    page.goto("https://leogcarvalho.github.io/test-automation-practice/")
    expect(page).to_have_title("Test Automation Practice Page")
    page.get_by_role("radio", name="Option A").click()
    time.sleep(4)
    