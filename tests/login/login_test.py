from pages.login_page import LoginPage
from utilities.users.users import JOHN_DOE
import pytest
import time


@pytest.mark.all
@pytest.mark.smoke
@pytest.mark.login
@pytest.mark.test_login_page_is_loaded
def test_login_page_is_loaded(page):
    login_page = LoginPage(page)
    login_page.default_login_page_should_be()
    time.sleep(3)
    assert False


@pytest.mark.all
@pytest.mark.smoke
@pytest.mark.login
@pytest.mark.errors
@pytest.mark.test_locked_out_user_error
def test_locked_out_user_error(page):
    login_page = LoginPage(page)
    username = JOHN_DOE.usernames["locked"]
    login_page.do_login(username)
    login_page.assert_login_error(login_page.texts.LOCKED_OUT_USER_ERROR)

