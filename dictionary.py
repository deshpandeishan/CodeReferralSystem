class CodeDictionary:

    def __init__(self):
        self.code_dict = {}

    def create_dictionary(self, key, value):
        self.code_dict[key] = value
        return self.code_dict
