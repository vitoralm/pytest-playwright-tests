from utilities.texts.texts import Texts


class BasePage:
    def __init__(self, page):
        self.page = page
        self.texts = Texts()
        self.base_url = "https://www.saucedemo.com"

    def get_element_locator_by_index(self, locator_xpath, index):
        """
        Returns the locator for the element at the given index.
        """
        # xpathindex begins from 1
        if isinstance(index, int):
            index += 1

        return_locator = "({})[{}]".format(locator_xpath, index)
        return return_locator
