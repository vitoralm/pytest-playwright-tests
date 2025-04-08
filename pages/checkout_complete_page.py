from pages.base_page import BasePage
from playwright.sync_api import expect


class CheckoutCompletePage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.checkout_complete_title = self.page_title
        self.complete_header = "//*[@data-test='complete-header']"
        self.complete_text = "//div[@data-test='complete-text']"
        self.back_home_button = "//button[@data-test='back-to-products']"

    def default_checkout_complete_page_should_be(self):
        expect(self.page.locator(self.checkout_complete_title)).to_be_visible()
        expect(self.page.locator(self.checkout_complete_title)).to_have_text(self.texts.CHECKOUT_COMPLETE_PAGE_TITLE)
        expect(self.page.locator(self.complete_header)).to_be_visible()
        expect(self.page.locator(self.complete_text)).to_be_visible()
        assert self.page.locator(self.complete_header).text_content() == self.texts.CHECKOUT_COMPLETE_TITLE
        assert self.page.locator(self.complete_text).text_content() == self.texts.CHECKOUT_COMPLETE_TEXT
        expect(self.page.locator(self.back_home_button)).to_be_visible()
        expect(self.page.locator(self.back_home_button)).to_have_text(self.texts.CHECKOUT_COMPLETE_BACK_HOME_BUTTON)
