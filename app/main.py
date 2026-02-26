from fastapi import FastAPI, HTTPException
from pydantic import BaseModel,validator
from decimal import Decimal
from typing import Literal
import uuid
import time

# accepts a structured payment request, validates the data automatically, assigns it a unique traceable ID, and returns a confirmation
app= FastAPI()#creates the app instance


class PaymentRequest(BaseModel):
    sender_account: str
    receiver_account: str
    amount: Decimal
    currency: Literal["USD","EUR","GBP"] 

    @validator("amount")
    def amount_must_be_positive(cls, v):
        if v<=0:
            raise ValueError("Amount must be greater than zero")
        return v #makes sure there is no negative amount

transactions = {}

@app.post("/process-payment")
def process_payment(payment: PaymentRequest):
    timestamp=time.time
    transaction_id = str(uuid.uuid4()) #generates uid for every call
    transactions[transaction_id]= {
        "status": "processed",
        "timestamp": timestamp,
        "payment": payment.dict()
    }
    return {
        "transaction_id": transaction_id,
        "status": "processed",
        "timestamp": timestamp
    }#returns the call's uid, status of call and timestamp


@app.get("/transaction/{transaction_id}")
def get_transaction(transaction_id: str):
    if transaction_id not in transactions:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return transactions[transaction_id]