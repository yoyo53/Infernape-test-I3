import pytest
from fixtures import reset_db, check_http_errors

from EmployeePage import EmployeePage
from User import User
from UserAddress import UserAddress

def test_update_adress_info(page, reset_db, check_http_errors):

    employee_page = EmployeePage(page)
    address = UserAddress("testadress1", "testadress2", "testcity", "94400")
    user = User("testname", "testesmail@email.com", address, "2017-12-12", "testjob")

    employee_page.goto_add_employee()
    employee_page.fill_employee_form(user)
    
    employee_page.update_address("address3")

    address1, address2 = employee_page.get_adresses()
    assert "address3" in address1
    assert "testadress2" in address2
