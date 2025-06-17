from fastapi import FastAPI
from routes import customer

app = FastAPI()
app.include_router(customer.router, prefix="/customers", tags=["Customers"])
