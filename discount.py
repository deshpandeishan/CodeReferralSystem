class DiscountCode:

    def __init__(self):
        self.used_codes_dict = []

    # This function is supposed to be triggered when a discount coupon code is used.
    def insert_used_code(self, key, used_code):
        self.used_codes_dict[key] = used_code
        return self.used_codes_dict
