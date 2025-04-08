from pages.login_page import LoginPage
from pages.cart_page import CartPage
from pages.inventory_page import InventoryPage
from utilities.users.users import JOHN_DOE
import pytest
from qase.pytest import qase


@pytest.mark.all
@pytest.mark.cart
@pytest.mark.test_verify_product_details_on_cart_page
@qase.id(10)
@qase.title("test_verify_product_details_on_cart_page")
def test_verify_product_details_on_cart_page(page):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    cart_page = CartPage(page)
    username = JOHN_DOE.usernames["standard"]
    login_page.do_login(username)
    inventory_page.default_inventory_page_should_be()
    product_name = inventory_page.products[0]["name"]
    inventory_page.add_product_to_cart(product_name)
    inventory_page.navigate_to_cart_page()
    cart_page.default_cart_page_should_be()
    cart_page.assert_product_details(product_name)


@pytest.mark.all
@pytest.mark.cart
@pytest.mark.test_remove_product_from_cart_page
@qase.id(11)
@qase.title("test_remove_product_from_cart_page")
def test_remove_product_from_cart_page(page):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    cart_page = CartPage(page)
    username = JOHN_DOE.usernames["standard"]
    login_page.do_login(username)
    inventory_page.default_inventory_page_should_be()
    product_name = inventory_page.products[0]["name"]
    inventory_page.add_product_to_cart(product_name)
    inventory_page.navigate_to_cart_page()
    cart_page.default_cart_page_should_be()
    cart_page.remove_product_from_cart(product_name)
    # TODO: Add assertion to verify that the product is removed from the cart


@pytest.mark.all
@pytest.mark.cart
@pytest.mark.test_update_product_quantities
@qase.id(12)
@qase.title("test_update_product_quantities")
def test_update_product_quantities(page):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    cart_page = CartPage(page)
    username = JOHN_DOE.usernames["standard"]
    login_page.do_login(username)
    inventory_page.default_inventory_page_should_be()
    product_name = inventory_page.products[0]["name"]
    inventory_page.add_product_to_cart(product_name)
    inventory_page.navigate_to_cart_page()
    cart_page.default_cart_page_should_be()
    # TODO: Add code to update product quantities
    # TODO: Add assertion to verify that the cart total is updated correctly
