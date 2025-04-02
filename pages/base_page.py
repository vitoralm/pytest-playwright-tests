from utilities.texts.texts import Texts
from retry import retry
from playwright.sync_api import TimeoutError


class BasePage:
    def __init__(self, page):
        self.page = page
        self.texts = Texts()
        self.base_url = "https://www.saucedemo.com"
        self.cart_button = '//a[@data-test="shopping-cart-link"]'
        self.page_title = "//span[@data-test='title']"
        self.inventory_item_name = "//div[@data-test='inventory-item-name']"
        self.inventory_item_price = "//div[@data-test='inventory-item-price']"
        self.inventory_item_description = '//div[@data-test="inventory-item-desc"]'

        self.products = [
            {
                "name": "Sauce Labs Backpack",
                "price": "$29.99",
                "description": "carry.allTheThings() with the sleek, streamlined Sly Pack that melds uncompromising style with unequaled laptop and tablet protection.",
                "buttonAddToCartDescription": "Add to cart",
                "buttonRemoveDescription": "Remove",
            },
            {
                "name": "Sauce Labs Bike Light",
                "price": "$9.99",
                "description": "A red light isn't the desired state in testing but it sure helps when riding your bike at night. Water-resistant with 3 lighting modes, 1 AAA battery included.",
                "buttonAddToCartDescription": "Add to cart",
                "buttonRemoveDescription": "Remove",
            },
            {
                "name": "Sauce Labs Bolt T-Shirt",
                "price": "$15.99",
                "description": "Get your testing superhero on with the Sauce Labs bolt T-shirt. From American Apparel, 100% ringspun combed cotton, heather gray with red bolt.",
                "buttonAddToCartDescription": "Add to cart",
                "buttonRemoveDescription": "Remove",
            },
            {
                "name": "Sauce Labs Fleece Jacket",
                "price": "$49.99",
                "description": "It's not every day that you come across a midweight quarter-zip fleece jacket capable of handling everything from a relaxing day outdoors to a busy day at the office.",
                "buttonAddToCartDescription": "Add to cart",
                "buttonRemoveDescription": "Remove",
            },
            {
                "name": "Sauce Labs Onesie",
                "price": "$7.99",
                "description": "Rib snap infant onesie for the junior automation engineer in development. Reinforced 3-snap bottom closure, two-needle hemmed sleeved and bottom won't unravel.",
                "buttonAddToCartDescription": "Add to cart",
                "buttonRemoveDescription": "Remove",
            },
            {
                "name": "Test.allTheThings() T-Shirt (Red)",
                "price": "$15.99",
                "description": "This classic Sauce Labs t-shirt is perfect to wear when cozying up to your keyboard to automate a few tests. Super-soft and comfy ringspun combed cotton.",
                "buttonAddToCartDescription": "Add to cart",
                "buttonRemoveDescription": "Remove",
            },
        ]

    def get_element_locator_by_index(self, locator_xpath, index):
        """
        Returns the locator for the element at the given index.
        """
        # xpathindex begins from 1
        if isinstance(index, int):
            index += 1

        return_locator = "({})[{}]".format(locator_xpath, index)
        return return_locator

    def navigate_to_cart_page(self):
        """
        Clicks the cart button.
        """
        self.page.locator(self.cart_button).click()
        self.page.wait_for_load_state("networkidle")
        self.page.wait_for_timeout(1000)
        assert self.page.url == f"{self.base_url}/cart.html"

    @retry(TimeoutError, tries=3, delay=1)
    def click_element(self, locator, until_disappears=False):
        """
        Clicks the element specified by the locator.
        """
        self.page.locator(locator).click()
        self.page.wait_for_load_state("networkidle")

        if until_disappears:
            self.page.locator(locator).wait_for(state="detached")
