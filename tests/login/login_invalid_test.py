from pages.login_page import LoginPage
import pytest
from qase.pytest import qase
from utilities.users.users import JOHN_DOE


@pytest.mark.all
@pytest.mark.login
@pytest.mark.errors
@pytest.mark.test_invalid_username_login
@qase.title("test_invalid_username_login")
@qase.id(15)
def test_invalid_username_login(page):
    login_page = LoginPage(page)
    login_page.do_login("invalid_username")
    login_page.assert_login_error(login_page.texts.INVALID_CREDENTIALS_ERROR)


@pytest.mark.all
@pytest.mark.login
@pytest.mark.errors
@pytest.mark.test_invalid_password_login
@qase.title("test_invalid_password_login")
@qase.id(16)
def test_invalid_password_login(page):
    login_page = LoginPage(page)
    username = JOHN_DOE.usernames["standard"]
    login_page.do_login(username=username, password="invalid_password")
    login_page.assert_login_error(login_page.texts.INVALID_CREDENTIALS_ERROR)


@pytest.mark.all
@pytest.mark.login
@pytest.mark.errors
@pytest.mark.test_invalid_username_password_login
@qase.title("test_invalid_username_password_login")
@qase.id(17)
def test_invalid_username_password_login(page):
    login_page = LoginPage(page)
    login_page.do_login("invalid_username", "invalid_password")
    login_page.assert_login_error(login_page.texts.INVALID_CREDENTIALS_ERROR)
