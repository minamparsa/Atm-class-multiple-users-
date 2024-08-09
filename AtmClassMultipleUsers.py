class ATM:  
    def __init__(self, balance=0, pin=0):  
        self.balance = balance  
        self.pin = pin  

    def check_balance(self):  
        return self.balance  

    def withdraw(self, amount):  
        if amount > self.balance:  
            return "Insufficient funds."  
        else:  
            self.balance -= amount  
            return f"Withdrawal successful. Current balance: {self.balance}"  

    def deposit(self, amount):  
        self.balance += amount  
        return f"Deposit successful. Current balance: {self.balance}"  

    def change_pin(self, new_pin):  
        self.pin = new_pin  
        return "PIN changed successfully."  


def main():  
    # Initializing multiple ATM instances for different users.  
    users = {  
        'User1': ATM(1000, 1234),  
        'User2': ATM(2000, 5678),  
        'User3': ATM(1500, 9101)  
    }  

    while True:  
        print("Welcome to the ATM machine.")  
        user_id = input("Please enter your user ID (User1, User2, User3) or type 'exit' to quit: ")  

        if user_id.lower() == 'exit':  
            break  
        elif user_id not in users:  
            print("Invalid user ID. Please try again.")  
            continue  

        atm = users[user_id]  
        pin = int(input("Please enter your PIN: "))  
        
        if pin != atm.pin:  
            print("Incorrect PIN. Session ended.")  
            continue  
            
        print("PIN accepted. You can now use the ATM services.")  
        
        while True:  
            print("\nMenu:")  
            print("1. Check Balance")  
            print("2. Withdraw")  
            print("3. Deposit")  
            print("4. Change PIN")  
            print("5. Logout")  

            option = int(input("\nEnter your choice: "))  
            
            if option == 1:  
                print("Current balance:", atm.check_balance())  

            elif option == 2:  
                amount = float(input("Enter the amount to withdraw: "))  
                print(atm.withdraw(amount))  

            elif option == 3:  
                amount = float(input("Enter the amount to deposit: "))  
                print(atm.deposit(amount))  

            elif option == 4:  
                new_pin = int(input("Enter your new PIN: "))  
                print(atm.change_pin(new_pin))  

            elif option == 5:  
                print("Logging out.")  
                break  

            else:  
                print("Invalid option. Please try again.")  

if __name__ == "__main__":  
    main()