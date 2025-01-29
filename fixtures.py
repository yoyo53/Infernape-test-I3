import pytest

@pytest.fixture
def reset_db(page):
    page.goto("/reset_db")
    page.locator("button:has-text('proceed')").click()

@pytest.fixture
def check_http_errors(page):
    def check_response(response):
        if response.status >= 400:
            pytest.fail(f"HTTP error {response.status} on {response.url}")
    page.on("response", check_response)
