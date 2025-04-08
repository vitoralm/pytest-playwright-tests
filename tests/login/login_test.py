from pages.login_page import LoginPage
from utilities.users.users import JOHN_DOE
import pytest
from qase.pytest import qase


@pytest.mark.all
@pytest.mark.smoke
@pytest.mark.login
@pytest.mark.test_login_page_is_loaded
@qase.title("test_login_page_is_loaded")
@qase.id(6)
def test_login_page_is_loaded(page):
    login_page = LoginPage(page)
    login_page.default_login_page_should_be()


@pytest.mark.all
@pytest.mark.smoke
@pytest.mark.login
@pytest.mark.errors
@pytest.mark.test_locked_out_user_error
@qase.title("test_locked_out_user_error")
@qase.id(5)
def test_locked_out_user_error(page):
    login_page = LoginPage(page)
    username = JOHN_DOE.usernames["locked"]
    login_page.do_login(username)
    login_page.assert_login_error(login_page.texts.LOCKED_OUT_USER_ERROR)
