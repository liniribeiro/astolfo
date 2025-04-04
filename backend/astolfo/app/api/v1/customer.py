from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database.queries import get_customer_by_id, create_customer
from database.session import get_sync_db
from schemas import CustomersSchema, CustomerSchemaInput

router = APIRouter()

@router.get(
    "/{customer_id}"
)
def api_get_customer_by_id(
    customer_id: str,
    session: Session = Depends(get_sync_db),
):
    customer = get_customer_by_id(session, customer_id)
    return CustomersSchema(**customer.to_dict())

@router.post(
    "/"
)
def api_create_customer(
    customer: CustomerSchemaInput,
    session: Session = Depends(get_sync_db),
):
    new_customer = create_customer(session, customer.name, customer.email, customer.phone, customer.company_id)
    return CustomersSchema(**new_customer.to_dict())

@router.delete(
    "/{customer_id}"
)
def api_delete_customer(
    customer_id: str,
    session: Session = Depends(get_sync_db),
):
    customer = get_customer_by_id(session, customer_id)
    if not customer:
        return {"error": "Customer not found"}
    session.delete(customer)
    session.commit()
    return {"message": "Customer deleted successfully"}
