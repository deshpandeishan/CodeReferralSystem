class Discount:

    def __init__(self):
        self.org_price = 300
        self.allowed_discount = 50
        self.received_discount = 0

    def calculate_discount(self):
        self.received_discount = (self.allowed_discount/100) * self.org_price
        return round(self.received_discount)
