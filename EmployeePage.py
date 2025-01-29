import pytest
from User import User

class EmployeePage:
    def __init__(self, page):
        self.page = page
    
    def goto_add_employee(self):
        self.page.goto("/add_employee")
    
    def fill_employee_form(self, user):
        self.page.locator("#id_name").fill(user.get_name())
        self.page.locator("#id_email").fill(user.get_email())
        self.page.locator("#id_address_line1").fill(user.get_address1())
        self.page.locator("#id_address_line2").fill(user.get_address2())
        self.page.locator("#id_city").fill(user.get_city())
        self.page.locator("#id_zip_code").fill(user.get_zip_code())
        self.page.locator("#id_hiring_date").fill(user.get_hiring_date())
        self.page.locator("#id_job_title").fill(user.get_job_title())
        self.page.get_by_role("button", name="Add").click()
    
    def update_address(self, new_address):
        self.page.get_by_role("link", name="Edit").click()
        self.page.get_by_role("link", name="Update address").click()
        self.page.locator("#id_address_line1").fill(new_address)
        self.page.get_by_role("button", name="Update").click()
        self.page.get_by_role("link", name="Update address").click()

    def employee_exists(self, email):
        return email in self.page.locator("tbody").inner_text()
    
    def get_adresses(self):
        return self.page.locator("#id_address_line1").input_value(), self.page.locator("#id_address_line2").input_value()
    
    def get_zip_code(self):
        return self.page.locator("#id_zip_code").input_value()