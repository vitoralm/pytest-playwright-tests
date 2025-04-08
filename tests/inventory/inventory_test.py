from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utilities.users.users import JOHN_DOE
import pytest
from qase.pytest import qase


@pytest.mark.all
@pytest.mark.inventory
@pytest.mark.test_verify_product_details
@qase.id(7)
@qase.title("test_verify_product_details")
def test_verify_product_details(page):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    username = JOHN_DOE.usernames["standard"]
    login_page.do_login(username)
    inventory_page.default_inventory_page_should_be()
    for product in inventory_page.products:
        inventory_page.assert_product_details(product["name"], product["description"], product["price"])


@pytest.mark.all
@pytest.mark.inventory
@pytest.mark.test_add_multiple_products_to_cart
@qase.id(8)
@qase.title("test_add_multiple_products_to_cart")
def test_add_multiple_products_to_cart(page):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    username = JOHN_DOE.usernames["standard"]
    login_page.do_login(username)
    inventory_page.default_inventory_page_should_be()
    for product in inventory_page.products:
        inventory_page.add_product_to_cart(product["name"])
    inventory_page.navigate_to_cart_page()


@pytest.mark.all
@pytest.mark.inventory
@pytest.mark.test_remove_product_from_inventory_page
@qase.id(9)
@qase.title("test_remove_product_from_inventory_page")
def test_remove_product_from_inventory_page(page):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    username = JOHN_DOE.usernames["standard"]
    login_page.do_login(username)
    inventory_page.default_inventory_page_should_be()
    product_name = inventory_page.products[0]["name"]
    inventory_page.add_product_to_cart(product_name)
    inventory_page.remove_product_from_cart(product_name)


@pytest.mark.all
@pytest.mark.inventory
@pytest.mark.test_problem_user
@qase.id(18)
@qase.title("test_problem_user")
def test_problem_user(page):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    username = JOHN_DOE.usernames["problem"]
    login_page.do_login(username)
    inventory_page.default_inventory_page_should_be()


@pytest.mark.all
@pytest.mark.test_performance_glitch_user
@qase.id(19)
@qase.title("test_performance_glitch_user")
def test_performance_glitch_user(page):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    username = JOHN_DOE.usernames["performance"]
    login_page.do_login(username)
    inventory_page.default_inventory_page_should_be()


@pytest.mark.all
@pytest.mark.inventory
@pytest.mark.test_error_user
@qase.id(20)
@qase.title("test_error_user")
def test_error_user(page):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    username = JOHN_DOE.usernames["error"]
    login_page.do_login(username)
    inventory_page.default_inventory_page_should_be()


@pytest.mark.all
@pytest.mark.inventory
@pytest.mark.test_visual_user
@qase.id(21)
@qase.title("test_visual_user")
def test_visual_user(page):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    username = JOHN_DOE.usernames["visual"]
    login_page.do_login(username)
    inventory_page.default_inventory_page_should_be()
