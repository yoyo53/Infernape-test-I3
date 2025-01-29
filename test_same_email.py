from EmployeePage import EmployeePage
from User import User
from fixtures import reset_db, check_http_errors


def test_add_employee_with_same_email(page, reset_db, check_http_errors):
    employee_page = EmployeePage(page)
    user1 = User("Hugo", "hugotest@mail.com", "adress1", "adress2", "city", "3333", "2020-05-05", "JobTitle")
    user2 = User("hugo2", "hugotest@mail.com", "adress1", "adress2", "city", "3333", "2020-05-05", "Job bidon")

    employee_page.goto_add_employee()
    employee_page.fill_employee_form(user1)
    
    assert employee_page.employee_exists(user1.get_email())
    
    page.get_by_role("link", name="Home").click()
    employee_page.goto_add_employee()
    employee_page.fill_employee_form(user2)
    
    assert not employee_page.employee_exists(user2.get_email())