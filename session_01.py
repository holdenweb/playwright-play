from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    # Go to https://www.gov.uk/government/organisations/department-for-international-trade
    page.goto("https://www.gov.uk/government/organisations/department-for-international-trade")

    # Click text=Accept additional cookies
    page.locator("text=Accept additional cookies").click()

    # Click text=Hide this message
    page.locator("text=Hide this message").click()

    # Click text=great.gov.uk: support for exporters and inward investors
    page.locator("text=great.gov.uk: support for exporters and inward investors").click()
    # expect(page).to_have_url("https://www.great.gov.uk/?utm_source=govuk&utm_medium=homepagelink&utm_campaign=EIG")

    # Click [aria-label="Cookies consent manager"] >> text=Accept all cookies
    page.locator("[aria-label=\"Cookies consent manager\"] >> text=Accept all cookies").click()

    # Click text=Where to export
    page.locator("text=Where to export").click()
    #expect(page).to_have_url("https://www.great.gov.uk/signup/?next=/where-to-export/")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
