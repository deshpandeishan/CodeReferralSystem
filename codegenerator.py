from code_elements import Letter, Number
from random import choice, shuffle

get_letter = Letter()
get_number = Number()


class GenerateCode:

    def __init__(self):
        self.code = ""
        self.letters = get_letter.str_to_list()
        self.numbers = get_number.return_numbers()

    def get_code(self):
        self.code = ""
        combined_list = []
        for _ in range(3):
            combined_list.append(choice(self.letters))
            combined_list.append(choice(self.numbers))
        shuffle(combined_list)
        self.code = ''.join(combined_list)
        return self.code
