from pages.login_page import LoginPage
from utilities.users.users import Users
import pytest
import time


@pytest.mark.all
@pytest.mark.smoke
@pytest.mark.login
def test_login_page_title_is_loaded(page):
    login_page = LoginPage(page)
    login_page.default_login_page_should_be()
    time.sleep(3)
    assert 1 == 2, "dummy assertion"


@pytest.mark.all
@pytest.mark.smoke
@pytest.mark.login
@pytest.mark.errors
def test_locked_out_user_error(page):
    login_page = LoginPage(page)
    users = Users()
    login_page.do_login(users.locked_user)
    login_page.assert_login_error(login_page.texts.LOCKED_OUT_USER_ERROR)
    time.sleep(3)
