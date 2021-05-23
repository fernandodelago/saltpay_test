# ---------------------------------------
# To test use this command on prompt -> uvicorn main:app --reload
# ---------------------------------------
# importing libraries
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
def raiz():
    return {"Hello": "World"}


# creating models
class info_account(BaseModel):
    acc_number: int
    acc_owner: str
    acc_balance: float


class mvto_hist(BaseModel):
    acc_h_number: int
    acc_h_date: str
    acc_h_value: float
    acc_h_tp: str


# creating the account database
account_db = [
    info_account(acc_number=1, acc_owner="Arisha Barron", acc_balance=5.00),
    info_account(acc_number=2, acc_owner="Branden Gibson", acc_balance=0.00),
    info_account(acc_number=3, acc_owner="Rhonda Church", acc_balance=0.00),
    info_account(acc_number=4, acc_owner="Georgina Hazel", acc_balance=0.00)
]

# creating the history database
history_mvt_db = [
    mvto_hist(acc_h_number=1, acc_h_date="2021-10-01", acc_h_value=5.00, acc_h_tp="C")
]


# creating function to get information account
# @app.get("/info_account")
# def get_all_account_info():
#    """get all accounts"""
#    return account_db


@app.get("/info_account/{account_number}")
def get_account_info(account_number: int):
    """get only one account"""
    for account_item in account_db:
        if account_item.acc_number == account_number:
            return account_item
    return {"Status": 404, "Message": "Account NOT FOUND. Correct the number and try again."}


# Creating function to create account
@app.post("/info_account")
def insert_new_account(new_account: info_account):
    """insert a new account"""
    # more business rules will be insert here or maybe
    # a new function for only validate data
    if new_account.acc_balance <= 0.0:
        return {"Status": 10, "Message": "First deposit must be greater than zero."}
    else:
        account_db.append(new_account)
    return new_account


@app.post("/mvto_hist/{acc_number}{balance_value}")
def update_balance(acc_number: int, balance_value: float):
    account_db_tmp = get_account_info(acc_number)
    account_db.remove(acc_number)
    account_db.append(acc_number,account_db_tmp.acc_owner, balance_value)


# creating function to operation account (credit/debit)
@app.post("/mvto_hist/{acc_number_from}{acc_number_to}{mvt_value}")
def transfer_values(acc_number_from: int, acc_number_to: int, mvt_value: float):
    """save movements on database"""
    if acc_number_from == acc_number_to:
        return {"Status": 12, "Message": "Account destiny must be different."}

    if valida_cta_from.acc_balance >= mvt_value:
        acc_number_from.acc_balance -= mvt_value
        update_balance()
        acc_number_to.acc_balance += mvt_value
        update_balance()
        return {"Status": 0, "Message": "Transfer done."}
    else:
        return {"Status": 11, "Message": "Insufficient balance."}




# creating function to get history movement
@app.get("/mvto_hist/{account_number}")
def get_history_mvt(account_number: int):
    """get the historical movement from account"""
    for account_item in history_mvt_db:
        if account_item.acc_h_number == account_number:
            return history_mvt_db
    return {"Status": 404, "Message": "Account number NOT FOUND. Correct the number and try again."}
