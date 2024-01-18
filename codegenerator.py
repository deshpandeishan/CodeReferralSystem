from code_elements import Letter, Number
from random import choice, shuffle

get_letter = Letter()
get_number = Number()


class GenerateCode:

    def __init__(self):
        self.code_list = []
        self.letter_list = []
        self.num_list = []
        self.code = ""
        self.letters = get_letter.str_to_list()
        self.numbers = get_number.return_numbers()

    def get_code(self):
        self.letter_list = []
        self.num_list = []
        self.code_list = []
        self.code = ""
        for _ in range(3):
            self.letter_list.append(choice(self.letters))
            self.num_list.append(choice(self.numbers))
        self.code_list.extend(self.letter_list)
        self.code_list.extend(self.num_list)
        shuffle(self.code_list)
        for _ in self.code_list:
            self.code += _
        return self.code
