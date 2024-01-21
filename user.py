from code_manager import DiscountCode
from discount import Discount

discount_code = DiscountCode()
discount = Discount()

class InsertCode:

    def __init__(self):
        self.user_input = ''
        self.used_code_list = []

    # take_ui means take user input
    def take_user_ip(self):
        self.user_input = input("Enter your discount coupon code here:   ")
        return self.user_input

    def manage_codes(self, user_input, code_list):
        if user_input in code_list:
            if user_input in self.used_code_list:
                print("Error! This code has been used by someone else!")
            else:
                self.used_code_list.extend(discount_code.insert_used_code(user_input))
                print(f"Your discounted price is:    {discount.calculate_discount()}")
        else:
            print("Error! Invalid code")
