class atm(object): 
    def __init__(self, atm_card_umber, pin_number):
        self.atm_card_number = atm_cardNumber
        self.pin_number = pinNumber 

    def CashWithdrawal(self):
        print("Cash Withdrawn")

    def BalanceEnquiry(self): 
        print("Balance Enquired")

    Atm=atm ("1234 5678 9012" , "9999 9999")

    print("Details of ATM Card:")
    print("ATM Card Number:", Atm.atmCardNumber)
    print("Pin Number: ", Atm.pinNumber)
    print(Atm.CashWithdrawal())
    print(Atm.BalanceEnquiry())