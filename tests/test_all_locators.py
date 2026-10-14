from playwright.sync_api import Page, expect
import time

def test_all_locators(page: Page):
    page.goto("https://leogcarvalho.github.io/test-automation-practice/playwright-locators.html")
    expect(page.get_by_role("button", name="Explicit Role Button")).to_be_visible()
    expect(page.get_by_role("link", name="Explicit Role Link")).to_be_visible()
    expect(page.get_by_role("img", name="robot icon")).to_be_visible()
    expect(page.get_by_role("button", name="Implicit Button")).to_be_visible()
    expect(page.get_by_role("link", name="Implicit Link")).to_be_visible()
   
   #get_by_text

    expect(page.get_by_text("Locate elements by their visible text content.", exact=True)).to_be_visible()
    expect(page.get_by_text("This text span can be located by its text.")).to_be_visible()
    expect(page.get_by_text("Locate elements by their title attribute (tooltip text).")).to_be_visible()
    expect(page.get_by_text("Form not submitted")).to_be_visible()
    


    #get_by_label
    page.get_by_label("Email Address").click()
    expect(page.get_by_label("Email Address")).to_be_visible()
    time.sleep(5)

    page.get_by_label("Accept Terms and Conditions").click()
    expect(page.get_by_label("Accept Terms and Conditions")).to_be_visible()
    time.sleep(5)
