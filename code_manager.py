class DiscountCode:

    # This method is supposed to be triggered when an unused discount coupon code is used.
    def insert_used_code(self, used_code):
        used_codes_list = []
        used_codes_list.append(used_code)
        return used_codes_list
