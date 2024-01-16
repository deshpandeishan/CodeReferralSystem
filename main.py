from codegenerator import GenerateCode
import os

code_instance = GenerateCode()

code = code_instance.get_code()
print(code)

user_input = input("Enter your discount code here: ")
if user_input == code:
    print("Congratulations! You got a discount..")
    #   call an instance which provides the discounted price.
else:
    print("Entered code cannot be processed.")