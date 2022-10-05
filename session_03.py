from PIL import Image
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    # Go to https://playwright.dev/python/docs/screenshots#full-page-screenshots
    page.goto("https://playwright.dev/python/docs/screenshots#full-page-screenshots")
    page.locator("#element-screenshot").screenshot(path="bit1.png")
    page.locator("#element-screenshot ~ p").screenshot(path="bit2.png")
    page.locator("#element-screenshot ~ p ~ div").screenshot(path="bit3.png")
    images = [Image.open(f"bit{c}.png") for c in '123']
    final_height = sum(image.height for image in images)
    result = Image.new('RGB', (images[0].width, final_height))
    y = 0
    for image in images:
        result.paste(image, (0, y))
        y += image.height
    assert y == final_height
    result.save('allbits.png')
    # Close page
    page.close()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
