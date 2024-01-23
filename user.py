from code_manager import DiscountCode
from discount import Discount
from codegenerator import GenerateCode
from Codelist import CodeList
from refer_code import ReferralCode
from sample_data import data

discount_code = DiscountCode()
discount = Discount()
code_generator = GenerateCode()
codelist = CodeList()

sub_dict = []
for item in data:
    sub_dict.append(item)


class InsertCode(ReferralCode):

    def __init__(self):
        super().__init__()
        self.user_input = ''
        self.code_list = []
        self.used_code_list = []
        self.id_list = []
        self.sub_dict = sub_dict

    def take_user_ip(self):
        self.user_input = input("Enter your discount coupon code here:   ")
        return self.user_input

    def manage_codes(self, user_input, code_list):
        if user_input in code_list:
            if user_input in self.used_code_list:
                print("Error! This code has been used by someone else!")
            else:
                user_id = input("Enter your unique id:  ")
                if user_id in self.sub_dict:
                    self.used_code_list.extend(discount_code.insert_used_code(user_input))
                    print(f"Your discounted price is:    {discount.calculate_discount()}")
                    refer = input("Type '1' for referring to the friend else type '0':    ")
                    if refer == '1':
                        referCode = self.generate_code()
                        self.code_list.append(referCode)
                        print(f"Your referral code:    {referCode}")
                        return self.code_list
                else:
                    print("Error! You are not eligible for the discount offer!")
        else:
            print("Error! Invalid code")


class CallCodeGenerator(InsertCode):

    def __init__(self):
        super().__init__()
        self.limit = 50
        self.code_str = ""
        self.condition = True

    def call_code(self):
        for _ in range(0, self.limit):
            self.code_str = code_generator.get_code()
            self.code_list.append(self.code_str)
        print(self.code_list)

    def task(self):
        while self.condition:
            user_input = self.take_user_ip()
            self.manage_codes(user_input, self.code_list)
            if user_input == "6875":
                self.condition = False
