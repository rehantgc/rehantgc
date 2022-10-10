class Atm:
    def __init__(self):
        self.__pin = ""
        self.__balance = 0

        self.__menu()
    def __menu(self):
        user_input = int(input("""
        How wold You like to proceed
        1. press 1 to Create pin
        2. press 2 to check Balance
        3. press 3 to withdraw
        4. press 4 to deposite
        5. pess 5 to exit
        """))

        if user_input == 1:
            self.createpin()
        if user_input == 2:
            self.check_balance()
        if user_input == 3:
            self.withdraw()
        if user_input == 4:
            self.deposite()
        if user_input == 5:
            print("Thank you Have a nice Day")
            return user_input

    def createpin(slef):
        slef.__pin = int(input("Enter  to set PIN"))
        print("PIN set Successfully")

    def check_balance(self):
        temp = int(input("Please enter your pin"))
        if temp == self.__pin:
            print("your balance is", self.__balance)
        else:
            print("You Entered pin is Incorrect")

    def withdraw(self):
        temp = int(input("Please enter your pin"))
        if temp == self.__pin:
            amountw = int(input("Enter amount to withdraw"))
            if amountw < self.__balance:
                print("Take Your Money")
                self.__balance = self.__balance - amountw
                print("You have", self.__balance)
            else:
                print("Insufficient Fund")
        else:
            print("Incorrect pin")


    def deposite(self):
        temp = int(input("Please enter your pin"))
        if temp == self.__pin:
            dep = int(input("Enter amount to deposit"))
            self.__balance = self.__balance + dep
        else:
            print("incorrect Pin")
sbi = Atm

sbi.menu()

