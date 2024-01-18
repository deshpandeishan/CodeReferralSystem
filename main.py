from codegenerator import GenerateCode
from dictionary import CodeList
from user_2 import InsertCode


code_instance = GenerateCode()
dictionary = CodeList()
insert_code = InsertCode()

limit = 11  # This variable holds the limit value of the total discounts allowed
code_list = []
for key in range(1, limit):
    code = code_instance.get_code()
    code_list = dictionary.create_list(code)

print(code_list)

user_input = insert_code.take_ui()
insert_code.manage_codes(user_input, code_list)
