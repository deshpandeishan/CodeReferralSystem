from code_elements import Letter, Number
from random import choice, shuffle

get_letter = Letter()
get_number = Number()


class GenerateCode:

    def __init__(self):
        self.code = []
        self.letter_list = []
        self.num_list = []
        self.code_str = ""
        self.letters = get_letter.str_to_list()
        self.numbers = get_number.return_numbers()

    def get_code(self):
        for _ in range(3):
            self.letter_list.append(choice(self.letters))
            self.num_list.append(choice(self.numbers))
        self.code.extend(self.letter_list)
        self.code.extend(self.num_list)
        shuffle(self.code)
        for _ in self.code:
            self.code_str += _
        return self.code_str
