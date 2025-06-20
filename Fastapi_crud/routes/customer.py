from fastapi import APIRouter
from models.customer import Customer
from controllers import customer as controller

router = APIRouter()


@router.get("/")
def get_all_customer():
    return controller.get_all_customers()

@router.get("/{id}")
def get_customer_by_id(id: str):
    return controller.get_customer_by_id(id)
@router.post("/")
def create(customer: Customer):
    return controller.create_customer(customer)

@router.put("/{id}")
def update(id: str, customer: Customer):
    return controller.update_customer(id, customer)

@router.delete("/{id}")
def delete(id: str):
    return controller.delete_customer(id)
