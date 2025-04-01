from pages.base_page import BasePage
from playwright.sync_api import expect


class CartPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.url = "/cart.html"
        self.cart_title = self.page_title
        self.cart_item_name = "//div[@class='inventory_item_name']"
        self.cart_item_price = "//div[@class='inventory_item_price']"
        self.cart_item_description = "//div[@class='inventory_item_desc']"
        self.cart_item_button = "//div[@class='cart_button']"
        self.checkout_button = "//button[@data-test='checkout']"
        self.add_cart_from_item_name = (
            "/ancestor::a/following-sibling::div[@class='item_pricebar']/button"
        )
        self.cart_description_label = "//div[@data-test='cart-desc-label']"
        self.cart_quantity_label = " //div[@data-test='cart-quantity-label']"
        self.cart_continue_shopping_button = 'div//[@data-test="continue-shopping"]'
        self.cart_button_checkout = "//button[@data-test='checkout']"


    def default_cart_page_should_be(self):
        expect(self.page.locator(self.cart_title)).to_be_visible()
        expect(self.page.locator(self.cart_title)).to_have_text("Your Cart")
        expect(self.page.locator(self.cart_button_checkout)).to_be_visible()
        expect(self.page.locator(self.cart_button_checkout)).to_have_text("Checkout")
        expect(self.page.locator(self.cart_continue_shopping_button)).to_be_visible()
        expect(self.page.locator(self.cart_continue_shopping_button)).to_have_text("Continue Shopping")

    def assert_remove_button_is_visible(self, product_name):
        remove_button_locator = f"{self.inventory_item_name}[text()='{product_name}']{self.add_cart_from_item_name}"
        remove_button = self.page.locator(remove_button_locator)
        remove_button.wait_for(state="visible")
        expect(remove_button).to_be_visible()
        assert (
            self.page.locator(
                f"{self.inventory_item_name}[text()='{product_name}']{self.add_cart_from_item_name}"
            ).text_content()
            == self.products[0]["buttonRemoveDescription"]
        )
    
    def click_checkout_button(self):
        self.page.locator(self.cart_button_checkout).click()
        self.page.wait_for_load_state("networkidle")
