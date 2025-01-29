import pytest
from fixtures import reset_db, check_http_errors

from EmployeePage import EmployeePage

def test_add(page, reset_db, check_http_errors):

    zip_code_overflow = "99999999999999999999999999999999999999"

    employee_page = EmployeePage(page)
    employee_page.goto_add_employee()
    employee_page.fill_employee_form(
        "testname", "testesmail@email.com", "testadress1", "testadress2", 
        "testcity", zip_code_overflow, "2017-12-12", "testjob"
    )
    
    employee_page.update_address("address3")
    
    assert employee_page.get_zip_code() == zip_code_overflow

