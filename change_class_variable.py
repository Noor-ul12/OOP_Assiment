

class Bank():
    Bank_name = "Bank Al Habib"
    
    @classmethod
    def change_name(cls, name):
        cls.Bank_name = name

bank1 = Bank()              # class object

print(bank1.Bank_name)      # before changing the varible

Bank.change_name("State Bank of Pakistan")

print(bank1.Bank_name)      # After change varible


