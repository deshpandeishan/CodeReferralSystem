from codegenerator import GenerateCode
from discount import Discount

code_instance = GenerateCode()
discount = Discount()

code = code_instance.get_code()
print(code)
print(discount.check_condition())
