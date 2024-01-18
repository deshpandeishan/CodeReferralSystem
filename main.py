from codegenerator import GenerateCode
from dictionary import CodeDictionary


code_instance = GenerateCode()
dictionary = CodeDictionary()
limit = 11  # This variable holds the limit value of the total discounts allowed
code_dict = {}
for key in range(1, limit):
    code = code_instance.get_code()
    code_dict = dictionary.create_dictionary(key, code)

print(code_dict)
