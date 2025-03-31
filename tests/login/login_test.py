from pages.login_page import LoginPage
import pytest
import time


@pytest.mark.all
@pytest.mark.smoke
@pytest.mark.login
def test_login_page_title_is_loaded(page):
    login_page = LoginPage(page)
    login_page.default_login_page_should_be()
    time.sleep(3)
    assert 1 == 2
