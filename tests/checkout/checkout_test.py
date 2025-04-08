from pages.login_page import LoginPage
from pages.checkout_page import CheckoutPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from utilities.users.users import JOHN_DOE
import pytest
from qase.pytest import qase


@pytest.mark.all
@pytest.mark.checkout
@pytest.mark.test_submit_checkout_information_missing_data
@qase.id(13)
@qase.title("test_submit_checkout_information_missing_data")
def test_submit_checkout_information_missing_data(page):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    cart_page = CartPage(page)
    checkout_page = CheckoutPage(page)
    username = JOHN_DOE.usernames["standard"]
    first_name = JOHN_DOE.first_name
    last_name = JOHN_DOE.last_name
    zip_code = JOHN_DOE.zip_code
    login_page.do_login(username)
    inventory_page.default_inventory_page_should_be()
    inventory_page.add_product_to_cart(inventory_page.products[0]["name"])
    inventory_page.navigate_to_cart_page()
    cart_page.default_cart_page_should_be()
    cart_page.click_checkout_button()
    checkout_page.default_checkout_page_step_one_should_be()
    checkout_page.fill_your_information("", "", "")
    checkout_page.click_continue_button()
    checkout_page.assert_error_message_is_displayed()
    checkout_page.fill_your_information(first_name, "", "")
    checkout_page.click_continue_button()
    checkout_page.assert_error_message_is_displayed()
    checkout_page.fill_your_information("", last_name, "")
    checkout_page.click_continue_button()
    checkout_page.assert_error_message_is_displayed()
    checkout_page.fill_your_information("", "", zip_code)
    checkout_page.click_continue_button()
    checkout_page.assert_error_message_is_displayed()
    checkout_page.fill_your_information(first_name, last_name, zip_code)
    checkout_page.click_continue_button()
    checkout_page.default_checkout_page_step_two_should_be(
        JOHN_DOE.payment_method,
        JOHN_DOE.shipping_method,
        inventory_page.products[0]["price"],
        "$2.40",
        "$32.39",
    )


@pytest.mark.all
@pytest.mark.checkout
@pytest.mark.test_cancel_checkout
@qase.id(14)
@qase.title("test_cancel_checkout")
def test_cancel_checkout(page):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    cart_page = CartPage(page)
    checkout_page = CheckoutPage(page)
    username = JOHN_DOE.usernames["standard"]
    first_name = JOHN_DOE.first_name
    last_name = JOHN_DOE.last_name
    zip_code = JOHN_DOE.zip_code
    login_page.do_login(username)
    inventory_page.default_inventory_page_should_be()
    inventory_page.add_product_to_cart(inventory_page.products[0]["name"])
    inventory_page.navigate_to_cart_page()
    cart_page.default_cart_page_should_be()
    cart_page.click_checkout_button()
    checkout_page.default_checkout_page_step_one_should_be()
    checkout_page.fill_your_information(first_name, last_name, zip_code)
    checkout_page.click_cancel_button()
    cart_page.default_cart_page_should_be()
