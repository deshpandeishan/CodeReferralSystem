from discount import DiscountCode

discount_code = DiscountCode()


class InsertCode:

    def __init__(self):
        self.user_code = 0
        self.user_input = ''

    # take_ui means take user input
    def take_ui(self):
        user_input = input("Enter your discount coupon code here:   ")
        return user_input

    def manage_codes(self):
        user_code = self.take_ui()
        # if user_code in :
        #     pass
