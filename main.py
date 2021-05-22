# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# importing libraries
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
def raiz():
    return {"Ola": "Mundo"}


# creating models
class info_account(BaseModel):
    acc_number: int
    acc_owner: str
    acc_balance: float


class info_history_mvmt_acc(BaseModel):
    acc_h_number: int
    acc_h_date: str
    acc_h_value: float


# creating the database
account_db = [
    info_account(acc_number=1, acc_owner="Arisha Barron", acc_balance=0.00),
    info_account(acc_number=2, acc_owner="Branden Gibson", acc_balance=0.00),
    info_account(acc_number=3, acc_owner="Rhonda Church", acc_balance=0.00),
    info_account(acc_number=4, acc_owner="Georgina Hazel", acc_balance=0.00)
]

# creating function to transfer values


# creating function to get information account
@app.get("/info_account")
def get_all_account_info():
    """get all accounts"""
    return account_db


@app.get("/info_account/{account_number}")
def get_account_info(account_number: int):
    """get only one account"""
    for account_item in account_db:
        if account_item.acc_number == account_number:
            return account_item
        pass
    return {"Status": 404, "Message" : "Account NOT FOUND. Correct the number and try again."}


# Creating function to create account
@app.post("/info_account")
def insert_new_account(new_account: info_account):
    """insert a new account"""
    # more business rules will be insert here or maybe
    # a new function for only validade data
    account_db.append(new_account)
    return new_account

# creating function to operation account (credit/debit)

# creating function to get history movement

# Press the green button in the gutter to run the script.
# if __name__ == '__main__':

#    print_hi('PyCharm')


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
