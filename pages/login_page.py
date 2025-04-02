from playwright.sync_api import expect
from pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.logo_div = 'div[class="login_logo"]'
        self.password_input = 'input[id="password"]'
        self.username_input = 'input[id="user-name"]'
        self.login_button = 'input[id="login-button"]'
        self.login_credentials = 'div[id="login_credentials"]'
        self.login_password = 'div[data-test="login-password"]'

    def default_login_page_should_be(self):
        assert self.page.title() == self.texts.APP_TITLE
        expect(self.page.locator(self.logo_div, has_text=self.texts.APP_TITLE)).to_be_visible()
        expect(self.page.locator(self.password_input)).to_be_visible()
        expect(self.page.locator(self.username_input)).to_be_visible()
        expect(self.page.locator(self.login_button)).to_be_visible()
        expect(self.page.locator(self.login_credentials)).to_be_visible()
        expect(self.page.locator(self.login_credentials)).to_have_text(self.texts.LOGIN_USERNAME_HELPER)
        expect(self.page.locator(self.login_password)).to_be_visible()
        expect(self.page.locator(self.login_password)).to_have_text(self.texts.LOGIN_PASSWORD_HELPER)

    def do_login(self, username, password="secret_sauce"):
        self.fill_input_username(username)
        self.fill_input_password(password)
        self.click_login_button()

    def fill_input_username(self, username):
        username_input = self.page.locator(self.username_input)
        username_input.fill(username)

    def fill_input_password(self, password="secret_sauce"):
        username_input = self.page.locator(self.password_input)
        username_input.fill(password)

    def click_login_button(self):
        login_button = self.page.locator(self.login_button)
        login_button.click()

    def assert_login_error(self, login_error):
        error_message = self.page.locator('h3[data-test="error"]')
        expect(error_message).to_be_visible()
        expect(error_message).to_have_text(login_error)
