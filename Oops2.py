#13/08/2025
class Bank:
    def __init__(self):
        self.bal=0
        self.pin=""
        self.Menu()
    def Menu(self):
        user_input=input(''' 
        1. Press 1 for Pin Change
        2. Press 2 for Balance Enquiry
        3. Press 3 for Withdrawl
        4. Press 4 to Exit ''')
        if user_input=='1':
            self.pin_change()
        elif user_input=='2':
            self.bal_enquiry()
        elif user_input=='3':
            self.withdrwal()
        elif user_input=='4':
            exit()
            
    def pin_change(self):
        new_pin=input("Enter Your New Pin :")
        self.pin=new_pin
        new_bal=int(input("Enter amount you want to deposite : "))
        self.bal=new_bal
        self.Menu()
    def bal_enquiry(self):
        verify=input("Enter your pin :")
        if verify==self.pin:
            print("Your Balance is :",self.bal)
        else:
            print("You entered a wrong pin.... Try Again")
            self.bal_enquiry()
        self.Menu()
    def withdrwal(self):
        verify=input("Enter your pin :")
        if verify==self.pin:
            amount=int(input("Enter Amount you want to withdraw : "))
            if amount<=self.bal:
                self.bal-=amount
                print(f"You have withdrawn {amount} your reamaing balance is {self.bal}")
            else:
                print("Insufficient Balance")
        else:
            print("You entered a wrong pin.... Try Again")
            self.withdrwal()
        self.Menu()


c1=Bank()