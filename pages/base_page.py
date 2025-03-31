from utilities.texts.texts import Texts


class BasePage:
    def __init__(self, page):
        self.page = page
        self.texts = Texts()
