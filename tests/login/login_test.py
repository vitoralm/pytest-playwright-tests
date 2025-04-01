from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
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
    assert False


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
    cart_page = CartPage(page)
    users = Users()
    product_name = inventory_page.products[4]["name"]
    login_page.do_login(users.problem_user)
    inventory_page.default_inventory_page_should_be()
    inventory_page.add_product_to_cart(product_name)
    inventory_page.assert_remove_button_is_visible(product_name)
    inventory_page.navigate_to_cart_page()
    cart_page.default_cart_page_should_be()
    cart_page.assert_remove_button_is_visible(product_name)
    cart_page.click_checkout_button
