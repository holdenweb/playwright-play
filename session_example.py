from playwright.sync_api import Playwright, sync_playwright, expect, TimeoutError as PWTimeoutError


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    # Go to https://www.gov.uk/government/organisations/department-for-international-trade
    page.goto(
        "https://www.gov.uk/government/organisations/department-for-international-trade",
        wait_until="domcontentloaded"
    )

    # Click text=Accept additional cookies
    lctr = page.locator("text=Accept additional cookies")
    lctr.click()

    # Click text=Hide this message
    page.locator("text=Hide this message").click()

    # Click [aria-label="Cookies consent manager"] >> text=Accept all cookies
    # Handles cookie consent management if present
    try:
        if page.locator(
            "[aria-label=\"Close this message\"]"
        ).count():
        # Click [aria-label="Close this message"]
            page.locator("[aria-label=\"Close this message\"]").click()
    except PWTimeoutError:
        pass

    # Go to https://www.great.gov.uk/?utm_source=govuk&utm_medium=homepagelink&utm_campaign=EIG
    page.goto(
        "https://www.great.gov.uk/?utm_source=govuk&utm_medium=homepagelink&utm_campaign=EIG",
        wait_until="domcontentloaded"
    )

    # expect(page).to_have_url("https://www.great.gov.uk/campaigns/internationalisation-fund-for-english-businesses/")
    loc = page.locator(".button:visible:has-text('Accept all cookies')")
    if loc.count():
        loc.click()

    # Click text=Internationalisation Fund now open
    page.locator("text=Internationalisation Fund now open").click()

    # Close page
    page.close()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
