import pytest

@pytest.fixture
def reset_db(page):
    page.goto("/reset_db")
    proceed_button = page.locator("button:has-text('proceed')")
    proceed_button.click()

def test_add(page, reset_db):

    # Fill form
    page.goto("/add_employee")
    page.locator("#id_name").fill("testname")
    page.locator("#id_email").fill("testesmail@email.com")
    address1 = "testadress1"
    address2 = "testadress2"
    page.locator("#id_address_line1").fill(address1)
    page.locator("#id_address_line2").fill(address2)
    page.locator("#id_city").fill("testcity")
    page.locator("#id_zip_code").fill("94400")
    page.locator("#id_hiring_date").fill("2017-12-12")
    page.locator("#id_job_title").fill("testjob")
    page.get_by_role("button", name="Add").click()

    page.get_by_role("link", name="Edit").click()
    page.get_by_role("link", name="Update address").click()

    address3 = "address3"
    page.locator("#id_address_line1").fill(address3)
    page.get_by_role("button", name="Update").click()

    page.get_by_role("link", name="Update address").click()
    
    assert address3 in page.locator("#id_address_line1").input_value()
    assert address2 in page.locator("#id_address_line2").input_value()



