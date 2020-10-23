

import lab4
from tkinter import *

class Application(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()

    # ---------- THIS IS WHERE ALL THE GUI ITEMS ARE CREATED ---------
    def create_widgets(self):
        # create a label and entry for name
        Label(self,
              text="Name:"
              ).grid(row=0, column=0, sticky=W)
        self.name_ent = Entry(self)
        self.name_ent.grid(row=0, column=1, sticky=W)

        # create a label and entry for name
        Label(self,
              text="PIN code:"
              ).grid(row=2, column=0, sticky=W)
        self.pin_ent = Entry(self)
        self.pin_ent.grid(row=2, column=1, sticky=W)

        Label(self,
              text="Amount:"
              ).grid(row=3, column=0, sticky=W)
        self.amount_ent = Entry(self)
        self.amount_ent.grid(row=3, column=1, sticky=W)

        # create VIP check button
        self.is_vip = BooleanVar()
        Checkbutton(self,
                    text="Person is a VIP",
                    variable=self.is_vip
                    ).grid(row=1, column=1, sticky=W)

        # create buttons for for adding persons and running simulator
        self.bttn_add = Button(self,
                               text="Create Account",
                               command=self.bttn_create_account)
        self.bttn_add.grid(row=0, column=2, sticky=W)

        self.bttn_sim = Button(self,
                            text="Withdrawal",
                            command=self.bttn_withdrawal)
        self.bttn_sim.grid(row=1, column=2, sticky=W)

        self.bttn_dep = Button(self,
                               text="Deposit",
                               command=self.bttn_deposit)
        self.bttn_dep.grid(row=2, column=2, sticky=W)

        self.bttn_chPIN = Button(self,
                               text="Change PIN",
                               command=self.bttn_change_PIN)
        self.bttn_chPIN.grid(row=3, column=2, sticky=W)

        self.bttn_view_t = Button(self,
                                 text="View Transactions",
                                 command=self.bttn_view_transactions)
        self.bttn_view_t.grid(row=4, column=2, sticky=W)

        # create text field
        self.output_txt = Text(self, width=55, height=10, wrap=WORD)
        self.output_txt.grid(row=6, column=0, columnspan=2)

    # ---------- SOME HELPING FUNCTIONS ---------

    def get_name_pin(self):
        try:
            self.name = self.name_ent.get()
            if len(self.name) == 0:
                raise ValueError("empty name")
            self.pin = int(self.pin_ent.get())
        except ValueError as error:
            self.output_txt.delete(0.0, END)
            self.output_txt.insert(0.0, "PIN needs to be an integer and name cannot be empty!")
            return False
        else:
            return True

    def get_name_pin_amount(self):
        if self.get_name_pin() == False:
            return False
        else:
            try:
                self.amount = int(self.amount_ent.get())
            except ValueError as error:
                self.output_txt.delete(0.0, END)
                self.output_txt.insert(0.0, "Amount needs to be an integer!")
                return False
            else:
                return True

    # ---------- THIS IS THE FUNCTIONS EXECUTED BY THE GUI ITEMS  ---------

    def bttn_create_account(self):
        if self.get_name_pin_amount() == True:
            if self.is_vip.get():
                lab4.account_dict[self.name] = lab4.PremiumAccount(self.name, self.amount, self.pin)
            else:
                lab4.account_dict[self.name] = lab4.Account(self.name, self.amount, self.pin)
            self.output_txt.delete(0.0, END)
            self.output_txt.insert(0.0, self.name + " has a new account...")

    def bttn_withdrawal(self):
        if self.get_name_pin_amount() == True:
            if self.name in lab4.account_dict:
                result = lab4.account_dict[self.name].withdrawal(self.amount, self.pin)
            else:
                result = self.name + " does not have an account with us, would you like to create one?"
            self.output_txt.delete(0.0, END)
            self.output_txt.insert(0.0, result)

    def bttn_deposit(self):
        if self.get_name_pin_amount() == True:
            if self.name in lab4.account_dict:
                result = lab4.account_dict[self.name].deposit(self.amount)
            else:
                result = self.name + " does not have an account with us, would you like to create one?"
            self.output_txt.delete(0.0, END)
            self.output_txt.insert(0.0, result)


    def bttn_change_PIN(self):
        old_pin = self.pin
        if self.get_name_pin() == True:
            if self.name in lab4.account_dict:
                result = lab4.account_dict[self.name].change_PIN(old_pin, self.pin)
            else:
                result = self.name + " does not have an account with us, would you like to create one?"
            self.output_txt.delete(0.0, END)
            self.output_txt.insert(0.0, result)


    def bttn_view_transactions(self):
        if self.get_name_pin() == True:
            if self.name in lab4.account_dict:
                if lab4.account_dict[self.name].ok_PIN(self.pin):
                    result = lab4.account_dict[self.name]
                else:
                    result = "Wrong PIN"
            else:
                result = self.name + " does not have an account with us, would you like to create one?"
            self.output_txt.delete(0.0, END)
            self.output_txt.insert(0.0, result)


 # ---------- SETTING UP THE MAIN WINDOW ---------


root = Tk()
root.title("The Mega-Bank")
root.geometry("700x300")
my_app = Application(root)
root.mainloop()





