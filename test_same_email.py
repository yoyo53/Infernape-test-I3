# import re
# from playwright.sync_api import Playwright, sync_playwright, expect
import pytest


@pytest.fixture
def reset_db(page):
    page.goto("/reset_db")
    proceed_button = page.locator("button:has-text('proceed')")
    proceed_button.click()

def test_add_employee_with_same_email(page, reset_db):
    page.goto("https://i.se2.hr.dmerej.info/")
    page.get_by_role("link", name="Add new employee").click()
    page.get_by_placeholder("Name").click()
    page.get_by_placeholder("Name").fill("Hugo")
    page.get_by_placeholder("Name").press("Tab")
    page.get_by_placeholder("Email").fill("hugotest@mail.com")
    page.get_by_placeholder("Email").press("Tab")
    page.locator("#id_address_line1").fill("adress1")
    page.locator("#id_address_line1").press("Tab")
    page.locator("#id_address_line2").fill("adress2")
    page.locator("#id_address_line2").press("Tab")
    page.get_by_placeholder("City").fill("city")
    page.get_by_placeholder("City").press("Tab")
    page.get_by_placeholder("Zip code").fill("3333")
    page.get_by_placeholder("Zip code").press("Tab")
    page.get_by_placeholder("Hiring date").fill("2020-05-05")
    page.get_by_placeholder("Job title").click()
    page.get_by_placeholder("Job title").fill("JobTitle")
    page.get_by_placeholder("Job title").press("Tab")
    page.get_by_role("button", name="Add").click()
    assert page.locator("tbody").inner_text().find("hugotest@mail.com") != -1
    page.get_by_role("link", name="Home").click()
    page.get_by_role("link", name="Add new employee").click()
    page.get_by_placeholder("Name").click()
    page.get_by_placeholder("Name").fill("hugo2")
    page.get_by_placeholder("Name").press("Tab")
    page.get_by_placeholder("Email").fill("hugotest@mail.com")
    page.get_by_placeholder("Email").press("Tab")
    page.locator("#id_address_line1").fill("adress1")
    page.locator("#id_address_line1").press("Tab")
    page.locator("#id_address_line2").fill("adress2")
    page.locator("#id_address_line2").press("Tab")
    page.get_by_placeholder("City").fill("city")
    page.get_by_placeholder("City").press("Tab")
    page.get_by_placeholder("Zip code").fill("3333")
    page.get_by_placeholder("Zip code").press("Tab")
    page.get_by_placeholder("Hiring date").fill("2020-05-05")
    page.get_by_placeholder("Job title").click()
    page.get_by_placeholder("Job title").fill("Job bidon")
    page.get_by_role("button", name="Add").click()
    assert page.locator("tbody").inner_text().find("hugo2") == -1
