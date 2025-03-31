from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utilities.users.users import Users
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


@pytest.mark.all
@pytest.mark.smoke
@pytest.mark.login
@pytest.mark.errors
@pytest.mark.test_locked_out_user_error
def test_locked_out_user_error(page):
    login_page = LoginPage(page)
    users = Users()
    login_page.do_login(users.locked_user)
    login_page.assert_login_error(login_page.texts.LOCKED_OUT_USER_ERROR)


@pytest.mark.all
@pytest.mark.smoke
@pytest.mark.login
@pytest.mark.test_standard_user
def test_standard_user(page):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    users = Users()
    login_page.do_login(users.problem_user)
    inventory_page.default_inventory_page_should_be()
