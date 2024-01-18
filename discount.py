class DiscountCode:

    def __init__(self):
        self.used_codes_list = []

    # This function is supposed to be triggered when a discount coupon code is used.
    def insert_used_code(self, used_code):
        self.used_codes_list.append(used_code)
        return self.used_codes_list
