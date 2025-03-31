from pages.base_page import BasePage
from playwright.sync_api import expect


class InventoryPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.page = page
        self.url = "/inventory.html"
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
        self.inventory_title = "//span[@data-test='title']"
        self.inventory_sorting = "//select[@data-test='product-sort-container']"
        self.inventory_item_name = "//div[@data-test='inventory-item-name']"
        self.inventory_item_price = "//div[@data-test='inventory-item-price']"
        self.inventory_item_description = "//div[@data-test='inventory-item-desc']"
        self.inventory_item_button = "//div[@data-test='inventory-item']//button"

    def default_inventory_page_should_be(self):
        self.page.wait_for_load_state("networkidle")
        self.page.locator(self.inventory_title).wait_for(state="visible")
        assert self.page.title() == "Swag Labs"
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
            expect(self.page.locator(f"{self.inventory_item_name}[text()='{product['name']}']")).to_be_visible()
            assert (
                self.page.locator(self.get_element_locator_by_index(self.inventory_item_price, index)).text_content()
                == product["price"]
            )
            expect(
                self.page.locator(f'{self.inventory_item_description}[normalize-space()="{product['description']}"]')
            ).to_be_visible()
            assert (
                self.page.locator(
                    self.get_element_locator_by_index(f"{self.inventory_item_button}", index)
                ).text_content()
                == product["buttonAddToCartDescription"]
            )
