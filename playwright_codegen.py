import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://i.se2.hr.dmerej.info/")
    page.get_by_role("link", name="Add new employee").click()
    page.get_by_placeholder("Name").click()
    page.get_by_placeholder("Name").fill("Test")
    page.get_by_placeholder("Name").press("Tab")
    page.get_by_placeholder("Email").fill("test@mail.com")
    page.get_by_placeholder("Email").press("Tab")
    page.locator("#id_address_line1").fill("testadress")
    page.locator("#id_address_line1").press("Tab")
    page.locator("#id_address_line2").press("Tab")
    page.get_by_placeholder("City").fill("testcity")
    page.get_by_placeholder("City").press("Tab")
    page.get_by_placeholder("Zip code").fill("57535")
    page.get_by_placeholder("Zip code").press("Tab")
    page.get_by_placeholder("Hiring date").fill("2025-01-10")
    page.get_by_placeholder("Job title").click()
    page.get_by_placeholder("Job title").fill("testjob")
    page.get_by_role("button", name="Add").click()
    page.get_by_role("link", name="Home").click()
    page.get_by_role("link", name="List employees").click()
    expect(page.locator("tbody")).to_contain_text("test@mail.com")
    expect(page.locator("tbody")).to_contain_text("Test")
    expect(page.locator("tbody")).to_match_aria_snapshot("- cell \"Test\"")
    page.get_by_role("link", name="Edit").click()
    page.get_by_role("link", name="Update basic info").click()
    page.get_by_role("navigation").click()
    page.get_by_role("link", name="Home").click()
    page.get_by_role("link", name="List employees").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
