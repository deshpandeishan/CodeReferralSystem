from codegenerator import GenerateCode
from Codelist import CodeList
from user import InsertCode
from code_manager import DiscountCode


code_instance = GenerateCode()
codelist = CodeList()
insert_code = InsertCode()
discountcode = DiscountCode()

limit = 11  # This variable holds the limit value of the total discounts allowed for an event
code_list = []
for _ in range(1, limit):
    code = code_instance.get_code()
    code_list = codelist.create_list(code)

print(f"All codes:  {code_list}")

condition = True
while condition:
    user_input = insert_code.take_user_ip()
    insert_code.manage_codes(user_input, code_list)
    if user_input == "6875":
        condition = False
