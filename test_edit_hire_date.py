def test_update_hiring_date(page):
    # Make sure db is empty
    page.goto("/reset_db")
    proceed_button = page.locator("button:has-text('proceed')")
    proceed_button.click()

    # Create an employee
    page.goto("/add_employee")
    name_input = page.locator('input[name="name"]')
    name_input.fill("Test")
    email_input = page.locator('input[name="email"]')
    email_input.fill("test@mail.com")
    address_input = page.locator('input[name="address_line1"]')
    address_input.fill("testadress")
    city_input = page.locator('input[name="city"]')
    city_input.fill("testcity")
    zip_code_input = page.locator('input[name="zip_code"]')
    zip_code_input.fill("57535")
    hiring_date_input = page.locator('input[name="hiring_date"]')
    hiring_date_input.fill("2025-01-10")
    job_title_input = page.locator('input[name="job_title"]')
    job_title_input.fill("testjob")
    page.click("text='Add'")

    # Goto the employee list
    page.goto("/employees")
    page.locator("td:has-text('test@mail.com')").locator("xpath=ancestor::tr").locator("text='Edit'").click()

    # Check the hiring date
    assert page.is_visible(f"p:has-text('Hired on Jan. 10, 2025')")

    # Update the hiring date
    page.click("text='Update contract'")
    hiring_date_input = page.locator('input[name="hiring_date"]')

    # remove readonly attribute
    hiring_date_input.evaluate('(element) => element.removeAttribute("readonly")')
    hiring_date_input.fill("2025-01-11")
    page.click("text='Update'")

    # Check the hiring date
    assert page.is_visible(f"p:has-text('Hired on Jan. 10, 2025')")

