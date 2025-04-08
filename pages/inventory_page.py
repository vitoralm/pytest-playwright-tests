from pages.base_page import BasePage
from playwright.sync_api import expect


class InventoryPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.page = page
        self.url = "/inventory.html"
        self.inventory_title = self.page_title
        self.inventory_sorting = "//select[@data-test='product-sort-container']"
        self.inventory_item_button = "//div[@data-test='inventory-item']//button"
        self.add_cart_from_item_name = (
            "/ancestor::div[@class='inventory_item_label']/following-sibling::div[@class='pricebar']/button"
        )

    def default_inventory_page_should_be(self):
        self.page.wait_for_load_state("networkidle")
        self.page.locator(self.inventory_title).wait_for(state="visible")
        assert self.page.title() == self.texts.APP_TITLE
        assert self.page.url == f"{self.base_url}{self.url}"
        expect(self.page.locator(self.inventory_title)).to_be_visible()
        expect(self.page.locator(self.inventory_title)).to_have_text("Products")
        assert self.page.locator(self.inventory_sorting).is_visible(), "Sorting dropdown is not visible"
        selected_text = self.page.evaluate(
            """() => {
                const select = document.querySelector('[data-test="product-sort-container"]');
                return select.selectedOptions[0].text;
            }"""
        )
        assert selected_text == "Name (A to Z)", f"Expected 'Name (A to Z)', but got '{selected_text}'"
        for index, product in enumerate(self.products):
            expect(self.page.locator(self.get_product_by_name(product["name"]))).to_be_visible()
            item_price_locator = self.get_element_locator_by_index(self.inventory_item_price, index)
            assert (
                self.page.locator(item_price_locator).text_content() == product["price"]
            ), "expected {} but got {}".format(product["price"], self.page.locator(item_price_locator).text_content())
            item_description_locator = '{}[normalize-space()="{}"]'.format(
                self.inventory_item_description, product["description"]
            )
            expect(self.page.locator(item_description_locator)).to_be_visible()
            assert (
                self.page.locator(
                    self.get_element_locator_by_index(f"{self.inventory_item_button}", index)
                ).text_content()
                == product["buttonAddToCartDescription"]
            )

    def add_product_to_cart(self, product_name):
        self.click_element(f"{self.inventory_item_name}[text()='{product_name}']{self.add_cart_from_item_name}")

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

    def assert_product_details(self, product_name, product_description, product_price):
        item_name_locator = self.get_product_by_name(product_name)
        item_description_locator = self.get_product_locators_by_name(
            product_name, self.inventory_item_label, self.inventory_item_description
        )
        item_price_locator = self.get_product_locators_by_name(
            product_name, self.inventory_item_card, self.inventory_item_price
        )
        expect(self.page.locator(item_name_locator)).to_be_visible()
        expect(self.page.locator(item_description_locator)).to_be_visible()
        expect(self.page.locator(item_price_locator)).to_be_visible()
        assert product_description == self.page.locator(item_description_locator).text_content()
        assert product_price == self.page.locator(item_price_locator).text_content()

    def remove_product_from_cart(self, product_name):
        remove_button_locator = f"{self.get_product_by_name(product_name)}{self.add_cart_from_item_name}"
        self.click_element(remove_button_locator)
