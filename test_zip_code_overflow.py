import pytest
from fixtures import reset_db

def test_add(page, reset_db):

    def check_response(response):
        if response.status >= 400:
            pytest.fail(f"HTTP error {response.status} on {response.url}")
        
    page.on("response", check_response)

    # Fill form
    page.goto("/add_employee")
    page.locator("#id_name").fill("testname")
    page.locator("#id_email").fill("testesmail@email.com")
    address1 = "testadress1"
    address2 = "testadress2"
    page.locator("#id_address_line1").fill(address1)
    page.locator("#id_address_line2").fill(address2)
    page.locator("#id_city").fill("testcity")
    big_zip_code = "999999999999999999999999999999999999999999"
    page.locator("#id_zip_code").fill(big_zip_code)
    page.locator("#id_hiring_date").fill("2017-12-12")
    page.locator("#id_job_title").fill("testjob")
    page.get_by_role("button", name="Add").click()

    assert "testname" in page.locator("td:has-text('testname')").inner_text()