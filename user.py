from code_manager import DiscountCode
from discount import Discount
from codegenerator import GenerateCode
from Codelist import CodeList

discount_code = DiscountCode()
discount = Discount()
code_generator = GenerateCode()  # Corrected variable name
codelist = CodeList()


class InsertCode:

    def __init__(self):
        self.user_input = ''
        self.used_code_list = []

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
                refer = int(input("Type '1' for referring to the friend else type '0':    "))
                if refer == 1:
                    pass    # Add method to display any code except the used code.
        else:
            print("Error! Invalid code")


class CallCodeGenerator(InsertCode):

    def __init__(self):
        super().__init__()
        self.limit = 11
        self.code_list = []
        self.code_str = ""
        self.condition = True

    def call_code(self):
        for _ in range(0, self.limit):
            self.code_str = code_generator.get_code()  # Corrected method call
            self.code_list.append(self.code_str)
        print(self.code_list)

    def task(self):
        while self.condition:
            user_input = self.take_user_ip()
            self.manage_codes(user_input, self.code_list)
            if user_input == "6875":
                self.condition = False
