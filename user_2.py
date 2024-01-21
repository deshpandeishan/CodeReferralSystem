from discount import DiscountCode

discount_code = DiscountCode()


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
                print("Discount granted!")
                print(f"Used codes list:    {self.used_code_list}")
        else:
            print("Error! Invalid code")
