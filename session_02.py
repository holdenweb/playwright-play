from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    # Go to https://www.great.gov.uk/signup/?next=/where-to-export/
    page.goto("https://www.great.gov.uk/signup/?next=/where-to-export/")

    # Click input[name="email"]
    page.locator("input[name=\"email\"]").click()

    # Fill input[name="email"]
    page.locator("input[name=\"email\"]").fill("steve.holden@digital.trade.gov.uk")

    # Press Tab
    page.locator("input[name=\"email\"]").press("Tab")

    # Press Tab
    page.locator("text=UK telephone number (optional)By providing your phone number, you agree to be co >> button").press("Tab")

    # Fill input[name="phone_number"]
    page.locator("input[name=\"phone_number\"]").fill("0749 507 0156")

    # Press Tab
    page.locator("input[name=\"phone_number\"]").press("Tab")

    # Fill input[name="password"]
    page.locator("input[name=\"password\"]").fill("only once?")

    # Click text=Sign up
    page.locator("text=Sign up").click()

    # Click [placeholder="Enter code"]
    page.locator("[placeholder=\"Enter code\"]").click()

    # Fill [placeholder="Enter code"]
    page.locator("[placeholder=\"Enter code\"]").fill("22692")

    # Click text=Submit
    page.locator("text=Submit").click()

    # Click text=Continue
    page.locator("text=Continue").click()
    # expect(page).to_have_url("https://www.great.gov.uk/where-to-export/")

    # Click text=Add product
    page.locator("text=Add product").click()

    # Fill [placeholder="ie\: fresh strawberries"]
    page.locator("[placeholder=\"ie\\: fresh strawberries\"]").fill("computer software")

    # Click [aria-label="search item"]
    page.locator("[aria-label=\"search item\"]").click()

    # Click text=Save and continue
    page.locator("text=Save and continue").click()

    # Close page
    page.close()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
