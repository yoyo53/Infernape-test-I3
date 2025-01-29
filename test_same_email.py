from EmployeePage import EmployeePage
from fixtures import reset_db, check_http_errors


def test_add_employee_with_same_email(page, reset_db, check_http_errors):
    employee_page = EmployeePage(page)
    
    employee_page.goto_add_employee()
    employee_page.fill_employee_form(
        "Hugo", "hugotest@mail.com", "adress1", "adress2", 
        "city", "3333", "2020-05-05", "JobTitle"
    )
    
    assert employee_page.employee_exists("hugotest@mail.com")
    
    page.get_by_role("link", name="Home").click()
    employee_page.goto_add_employee()
    employee_page.fill_employee_form(
        "hugo2", "hugotest@mail.com", "adress1", "adress2", 
        "city", "3333", "2020-05-05", "Job bidon"
    )
    
    assert not employee_page.employee_exists("hugo2")