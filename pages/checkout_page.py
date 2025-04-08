from pages.base_page import BasePage
from playwright.sync_api import expect


class CheckoutPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.url_step_one = "/checkout-step-one.html"
        self.checkout_title = self.page_title
        self.checkout_first_name = "//input[@data-test='firstName']"
        self.checkout_last_name = "//input[@data-test='lastName']"
        self.checkout_zip_code = "//input[@data-test='postalCode']"
        self.checkout_continue_button = "//input[@data-test='continue']"
        self.checkout_cancel_button = "//button[@data-test='cancel']"

        # Step two locators
        self.cart_item = "//div[@class='cart_item']"  # keeping class since it's a container
        self.cart_item_quantity = "//div[@class='cart_quantity']"  # keeping class since quantity is static
        self.summary_payment_label = "//div[@data-test='payment-info-label']"
        self.summary_shipping_label = "//div[@data-test='shipping-info-label']"
        self.summary_subtotal_label = "//div[@data-test='subtotal-label']"
        self.summary_tax_label = "//div[@data-test='tax-label']"
        self.price_total_label = "//div[@data-test='total-info-label']"
        self.order_total_label = "//div[@data-test='total-label']"
        self.shipping_info_value = "//div[@data-test='shipping-info-value']"
        self.payment_info_value = "//div[@data-test='payment-info-value']"
        self.checkout_finish_button = "//button[@data-test='finish']"
        self.checkout_step_two_title = "Checkout: Overview"

    def default_checkout_page_step_one_should_be(self):
        self.page.wait_for_load_state("networkidle")
        self.page.locator(self.checkout_title).wait_for(state="visible")
        assert self.page.title() == self.texts.APP_TITLE
        assert self.page.url == f"{self.base_url}{self.url_step_one}"
        expect(self.page.locator(self.checkout_title)).to_be_visible()
        expect(self.page.locator(self.checkout_title)).to_have_text("Checkout: Your Information")
        expect(self.page.locator(self.checkout_first_name)).to_be_visible()
        expect(self.page.locator(self.checkout_last_name)).to_be_visible()
        expect(self.page.locator(self.checkout_zip_code)).to_be_visible()
        expect(self.page.locator(self.checkout_continue_button)).to_be_visible()
        expect(self.page.locator(self.checkout_continue_button)).to_have_text("Continue")
        expect(self.page.locator(self.checkout_cancel_button)).to_be_visible()
        expect(self.page.locator(self.checkout_cancel_button)).to_have_text("Cancel")

    def default_checkout_page_step_two_should_be(
        self, payment_info_value, shipping_info_value, item_total, taxes, order_total
    ):
        """Validates the checkout step two page elements and content"""
        self.url_step_two = "/checkout-step-two.html"
        self.page.wait_for_load_state("networkidle")
        self.page.locator(self.checkout_title).wait_for(state="visible")

        # Verify page basics
        assert self.page.title() == self.texts.APP_TITLE
        assert self.page.url == f"{self.base_url}{self.url_step_two}"

        # Verify checkout title
        expect(self.page.locator(self.checkout_title)).to_be_visible()
        expect(self.page.locator(self.checkout_title)).to_have_text(self.checkout_step_two_title)

        # Verify cart items exist and quantities shown
        cart_items = self.page.locator(self.cart_item).all()
        for item in cart_items:
            item_name = item.locator(self.inventory_item_name).text_content()
            item_price = item.locator(self.inventory_item_price).text_content()

            # Find matching product and verify
            matching_product = next(
                (product for product in self.products if product["name"] == item_name),
                None,
            )

            assert matching_product is not None, f"Product {item_name} not found in products list"
            assert item_price == matching_product["price"]

            # Verify item details
            expect(item.locator(self.cart_item_quantity)).to_be_visible()
            expect(item.locator(self.inventory_item_description)).to_be_visible()
            expect(item.locator(self.inventory_item_description)).to_have_text(matching_product["description"])

        # Verify summary labels
        expect(self.page.locator(self.summary_payment_label)).to_be_visible()
        expect(self.page.locator(self.summary_payment_label)).to_have_text(self.texts.PAYMENT_INFORMATION)
        assert self.page.locator(self.payment_info_value).text_content() == payment_info_value

        expect(self.page.locator(self.summary_shipping_label)).to_be_visible()
        expect(self.page.locator(self.summary_shipping_label)).to_have_text(self.texts.SHIPPING_INFORMATION)
        assert self.page.locator(self.shipping_info_value).text_content() == shipping_info_value

        expect(self.page.locator(self.summary_subtotal_label)).to_be_visible()
        assert self.page.locator(self.summary_subtotal_label).text_content() == self.texts.ITEM_TOTAL_VALUE.format(
            item_total
        )
        expect(self.page.locator(self.summary_tax_label)).to_be_visible()
        expect(self.page.locator(self.summary_tax_label)).to_have_text(self.texts.TAX_VALUE.format(taxes))

        expect(self.page.locator(self.order_total_label)).to_be_visible()
        expect(self.page.locator(self.order_total_label)).to_have_text(self.texts.ORDER_TOTAL_VALUE.format(order_total))

        # Verify footer buttons
        expect(self.page.locator(self.checkout_cancel_button)).to_be_visible()
        expect(self.page.locator(self.checkout_cancel_button)).to_have_text(self.texts.CANCEL)

        expect(self.page.locator(self.checkout_finish_button)).to_be_visible()
        expect(self.page.locator(self.checkout_finish_button)).to_have_text(self.texts.FINISH)

    def fill_your_information(self, first_name, last_name, zip_code):
        self.page.locator(self.checkout_first_name).fill(first_name)
        self.page.locator(self.checkout_last_name).fill(last_name)
        self.page.locator(self.checkout_zip_code).fill(zip_code)

    def click_continue_button(self):
        self.click_element(self.checkout_continue_button)

    def click_cancel_button(self):
        self.click_element(self.checkout_cancel_button)

    def click_finish_order(self):
        self.click_element(self.checkout_finish_button)

    def assert_error_message_is_displayed(self):
        error_message_locator = "//h3[@data-test='error']"
        expect(self.page.locator(error_message_locator)).to_be_visible()
