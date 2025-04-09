
from typing import TypeVar

from pydantic.v1 import UUID4
from sqlalchemy.orm import Session

from database import Company, User, Plan, TaskPlans, Customer, Signature, CompanyTask
from database.models.base import BaseModel
from database.queries.base import get_or_404
from exceptions.exceptions import DuplicatedData, NotFound
from schemas import SignatureSchema, CompanyTaskSchema


def create_customer(db: Session, name: str, email: str, phone: str, company_id: str):
    """
    Create a new customer in the database.
    """
    new_customer = Customer(name=name, email=email, phone=phone, company_id=company_id)
    db.add(new_customer)
    db.flush()
    return new_customer.to_dict()
