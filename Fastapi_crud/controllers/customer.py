from fastapi import HTTPException
from models.customer import Customer
from doa.connectionManager import customers



# customers is defined in models/customer.py
def get_all_customers():
    return customers

def get_customer_by_id(id: str):
    for c in customers:
        if c.id == id:
            return c
    raise HTTPException(status_code=404, detail="Customer not found")

def create_customer(customer: Customer):
    if any(c.id == customer.id for c in customers):
        raise HTTPException(status_code=400, detail="Customer ID already exists")
    customers.append(customer)
    return {"message": "Customer created"}

def update_customer(id: str, new_customer: Customer):
    for idx, c in enumerate(customers):
        if c.id == id:
            customers[idx] = new_customer
            return {"message": "Customer updated"}
    raise HTTPException(status_code=404, detail="Customer not found")

def delete_customer(id: str):
    for idx, c in enumerate(customers):
        if c.id == id:
            customers.pop(idx)
            return {"message": "Customer deleted"}
    raise HTTPException(status_code=404, detail="Customer not found")
