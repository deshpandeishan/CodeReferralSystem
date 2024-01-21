from codegenerator import GenerateCode


class ReferralCode(GenerateCode):

    def __init__(self):
        super().__init__()
        self.referral_code = ""

    def generate_code(self):
        self.referral_code = self.get_code()
        return self.referral_code
