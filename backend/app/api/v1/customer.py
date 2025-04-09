from fastapi import APIRouter, Depends
from pydantic import UUID4
from sqlalchemy.orm import Session

from database import Customer
from database.queries.base import get_or_404
from database.queries.customer import  create_customer
from database.session import get_sync_db
from schemas import CustomersSchema, CustomerSchema

router = APIRouter()

@router.get(
    "/{customer_id}"
)
def get_customer(
    customer_id: UUID4,
    session: Session = Depends(get_sync_db),
):
    customer = get_or_404(session, Customer, customer_id)
    return CustomersSchema(**customer.to_dict())

@router.post(
    "/"
)
def save_customer(
    customer: CustomerSchema,
    session: Session = Depends(get_sync_db),
):
    new_customer = create_customer(session, customer.name, customer.email, customer.phone, customer.company_id)
    return CustomersSchema(**new_customer.to_dict())

@router.delete(
    "/{customer_id}"
)
def delete_customer(
    customer_id: UUID4,
    session: Session = Depends(get_sync_db),
):
    customer = get_or_404(session, Customer, customer_id)
    if not customer:
        return {"error": "Customer not found"}
    session.delete(customer)
    session.commit()
    return {"message": "Customer deleted successfully"}
