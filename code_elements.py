from string import ascii_uppercase


class Letter:

    def __init__(self):
        self.letter_str = ascii_uppercase
        self.letter_list = []

    def str_to_list(self):
        for element in self.letter_str:
            self.letter_list.append(element)
        return self.letter_list


class Number:

    def __init__(self):
        self.number_list = []

    def return_numbers(self):
        for _ in range(0, 11):
            _ = str(_)
            self.number_list.append(_)
        return self.number_list
