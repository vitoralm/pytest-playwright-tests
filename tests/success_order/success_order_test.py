from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.checkout_complete_page import CheckoutCompletePage
from utilities.users.users import JOHN_DOE
import pytest
from qase.pytest import qase


@pytest.mark.all
@pytest.mark.smoke
@pytest.mark.test_standard_user_submit_simple_order
@qase.id(4)
@qase.title("test_standard_user_submit_simple_order")
def test_standard_user_submit_simple_order(page):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    cart_page = CartPage(page)
    checkout_page = CheckoutPage(page)
    checkout_complete_page = CheckoutCompletePage(page)
    username = JOHN_DOE.usernames["standard"]
    first_name = JOHN_DOE.first_name
    last_name = JOHN_DOE.last_name
    zip_code = JOHN_DOE.zip_code
    shipping_method = JOHN_DOE.shipping_method
    payment_method = JOHN_DOE.payment_method
    product_name = inventory_page.products[4]["name"]
    product_price = inventory_page.products[4]["price"]
    taxes = "$0.64"
    order_total = "$8.63"
    login_page.do_login(username)
    inventory_page.default_inventory_page_should_be()
    inventory_page.add_product_to_cart(product_name)
    inventory_page.assert_remove_button_is_visible(product_name)
    inventory_page.navigate_to_cart_page()
    cart_page.default_cart_page_should_be()
    cart_page.assert_remove_button_is_visible(product_name)
    cart_page.click_checkout_button()
    checkout_page.default_checkout_page_step_one_should_be()
    checkout_page.fill_your_information(first_name, last_name, zip_code)
    checkout_page.click_continue_button()
    checkout_page.default_checkout_page_step_two_should_be(
        payment_method, shipping_method, product_price, taxes, order_total
    )
    checkout_page.click_finish_order()
    checkout_complete_page.default_checkout_complete_page_should_be()
