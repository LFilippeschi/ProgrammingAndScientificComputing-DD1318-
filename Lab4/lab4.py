from datetime import date, datetime  # date.today(), datetime.now()
import json
from json import JSONEncoder

file_name = "account_infos.csv"
account_dict = {}


class AccountEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__

class Account:
    transactions = []

    def __init__(self, name, money, pin_code):
        self.name = name
        self.money = money
        self.pin_code = pin_code
        self.transactions = []

    def __str__(self):
        message = "Name: " + self.name + ", Money: " + \
            str(self.money) + ", transactions:\n" + str(self.transactions)
        return message

    def deposit(self, amount):
        self.money += amount
        self.transactions.append(datetime.now().strftime(
            "%d/%m/%Y %H:%M:%S ") + "DEPOSIT: " + str(amount))
        print("Deposit successful")

    def withdrawal(self, amount, pin):
        if self.ok_PIN(pin):
            if amount > self.money:
                print(
                    "Not enough money on the account, withdraw max amount available: " + str(self.money))
                self.transactions.append(datetime.now().strftime(
                    "%d/%m/%Y %H:%M:%S") + " WITHDRAWAL: " + str(self.money))
                self.money = 0
            else:
                self.money -= amount
                self.transactions.append(datetime.now().strftime(
                    "%d/%m/%Y %H:%M:%S") + " WITHDRAWAL: " + str(amount))
                print("Withdrawal successful")

    def display_saldo(self):
        return str(self.money)

    def ok_PIN(self, pin):
        if pin != self.pin_code:
            print("Wrong PIN")
            return False
        else:
            return True

    def change_PIN(self, old_pin, new_pin):
        if self.ok_PIN(old_pin):
            self.pin_code = new_pin
            print("Change of PIN successful")


class PremiumAccount(Account):
    def withdrawal(self, amount, pin):
        return super().withdrawal(amount, pin)

# FUNCTIONS


def get_int_input(prompt_string):
    while True:
        try:
            x = int(input(prompt_string))
            if x < 1:
                print('Enter a positive amount')
                continue
            return x
        except Exception as e:
            print('Enter a number')
            continue


def get_pin_input():
    while True:
        try:
            x = int(input("Enter Pin code, 4 digits:"))
            if x < 999 or x > 9999:
                print('Enter a valid pin')
                continue
            return x
        except Exception as e:
            print('Enter a valid pin')
            continue


def display_accounts():
    for x in account_dict:
        print(x)


def read_account_from_file(file_name):
    fr = open(file_name, 'r')
    # file_content = fr.


def menu():
    print("What would you like to do?")
    print("1 - Set up a new account")
    print("2 - Deposit")
    print("3 - Withdrawal")
    print("4 - Change Pin")
    print("5 - Display earlier transactions")
    print("7 - Display saldo")
    print("6 - Exit")


def menu_choice():
    while True:
        x = get_int_input("Your choice:")
        if x > 7:
            print("Enter a valid option")
            continue
        else:
            return x


def create_account():
    while True:
        name = input("Name:")
        if name in account_dict:
            print("Name already in use, choose another")
            continue
        break
    money = get_int_input("Money:")
    pin = get_pin_input()
    account_dict[name] = Account(name, money, pin)


def account_exist(name):
    if name in account_dict:
        return True
    else:
        print("Account doesn't exist, try again")
        return False


def select_account():
    name = input("Name:")
    if account_exist(name):
        return account_dict[name]

def init():
    fo = open('account_list.json', 'r')
    json_string = fo.read()
    fo.close()
    account_json = json.loads(json_string)
    #print(json_string)
    #print(account_json)
    json_dict = account_json
    #json_dict = dict(account_json)
    #print(json_dict)
    for x in json_dict:
        str_x = str(x)
        account_dict[str_x]= Account(str_x, json_dict[str_x]['money'], json_dict[str_x]['pin_code'])
        account_dict[str_x].transactions = json_dict[str_x]['transactions']

def close():
    json_string= json.dumps(account_dict, indent=2, cls=AccountEncoder)
    fo = open('account_list.json', 'w')
    fo.write(json_string)
    fo.close()
    print('File saved successfully!')
    quit()

def execute(choice):
    if choice == 1:
        create_account()
        return
    if choice == 2:
        account = select_account()
        if account:
            account.deposit(get_int_input("Amount:"))
        return
    if choice == 3:
        account = select_account()
        if account:
            pin = get_pin_input()
            account.withdrawal(get_int_input("Amount:"), pin)
        return
    if choice == 4:
        account = select_account()
        if account:
            old_pin = get_pin_input()
            if account.ok_PIN(old_pin):
                account.change_PIN(old_pin, get_pin_input())
        return
    if choice == 5:
        account = select_account()
        if account:
            old_pin = get_pin_input()
            if account.ok_PIN(old_pin):
                print(account.transactions)
        return
    if choice == 6:
        close()
    if choice == 7:
        account = select_account()
        if account:
            old_pin = get_pin_input()
            if account.ok_PIN(old_pin):
                print(account.display_saldo())
        return


def main():
    init()
    while True:
        menu()
        execute(menu_choice())
        print('-'*50)

    """ account_dict["Leo"]= Account('Leo', 200, 1234)
    account_dict["Kim"]= Account('Kim', 200, 1234)
    account_dict["Liz"]= Account('Liz', 200, 1234)
    display_accounts()
    account_dict["Leo"].deposit(200)

    print('how does it look like?')
    print(AccountEncoder().encode(account_dict))

    print("json formatted data")
    accountJSONData = json.dumps(account_dict, indent=4, cls=AccountEncoder)
    print(accountJSONData) """



if __name__ == "__main__":
    main()
