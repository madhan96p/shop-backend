class Payment:
    def __init__(self, amount):
        self.amount = amount
    
    def process_payment(self, method):
        if method == "UPI":
            print(f"Payment of Rs. {self.amount} will be processed through UPI.")
        elif method == "Debit Card":
            print(f"Payment of Rs. {self.amount} will be processed through Debit Card.")
        else:
            print(f"Unknown payment method.")
