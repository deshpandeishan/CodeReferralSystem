from code_elements import Letter, Number
from random import shuffle

get_letter = Letter()
get_number = Number()


class GenerateCode:

    def __init__(self):
        self.code = []
        self.letters = []
        self.numbers = []
        self.letters = get_letter.str_to_list()
        self.numbers = get_number.return_numbers()

    def get_code(self):
        for _ in range(3):
            for __ in range(3):
                self.code.append(self.letters)
            self.code.append(self.numbers)
            shuffle(self.code)
        return self.code
