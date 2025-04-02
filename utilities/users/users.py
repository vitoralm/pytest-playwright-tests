class User:
    def __init__(self, first_name, last_name, zip_code):
        self.usernames = {
            "standard": "standard_user",
            "locked": "locked_out_user",
            "problem": "problem_user",
            "performance": "performance_glitch_user",
            "error": "error_user",
            "visual": "visual_user",
        }
        self.first_name = first_name
        self.last_name = last_name
        self.zip_code = zip_code
        self.payment_method = "SauceCard #31337"
        self.shipping_method = "Free Pony Express Delivery!"


JOHN_DOE = User("John", "Doe", "12345")
