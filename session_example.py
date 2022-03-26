from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    # Go to https://www.gov.uk/government/organisations/department-for-international-trade
    page.goto("https://www.gov.uk/government/organisations/department-for-international-trade")

    # Click text=Accept additional cookies
    lctr = page.locator("text=Accept additional cookies")
    lctr.click()

    # Click text=Hide this message
    page.locator("text=Hide this message").click()

    # Click [aria-label="Cookies consent manager"] >> text=Accept all cookies
    lctr1 = page.locator("[aria-label=\"Cookies consent manager\"] >> text=Accept all cookies")
    lctr1.click()

    # Click [aria-label="Close this message"]
    page.locator("[aria-label=\"Close this message\"]").click()

    # Click text=Where to export
    page.locator("text=Where to export").click()
    # expect(page).to_have_url("https://www.great.gov.uk/signup/?next=/where-to-export/")

    # Go to https://www.great.gov.uk/?utm_source=govuk&utm_medium=homepagelink&utm_campaign=EIG
    page.goto("https://www.great.gov.uk/?utm_source=govuk&utm_medium=homepagelink&utm_campaign=EIG")

    # Click text=Internationalisation Fund now open
    page.locator("text=Internationalisation Fund now open").click()
    # expect(page).to_have_url("https://www.great.gov.uk/campaigns/internationalisation-fund-for-english-businesses/")

    # Close page
    page.close()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
