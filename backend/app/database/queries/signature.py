from typing import TypeVar

from pydantic.v1 import UUID4
from sqlalchemy.orm import Session

from database import Company, User, Plan, TaskPlans, Customer, Signature, CompanyTask
from database.models.base import BaseModel
from database.queries.base import get_or_404
from exceptions.exceptions import DuplicatedData, NotFound
from schemas import SignatureSchema, CompanyTaskSchema


def get_signature_by_customer_id(db: Session, customer_id: str):
    """
    Get a signature by customer ID.
    """
    signature = db.query(Signature).filter(Signature.customer_id == customer_id).first()
    return signature


def create_signature(db: Session, signature: SignatureSchema):
    """
    Create a new signature in the database.
    """
    new_signature = Signature(customer_id=signature.customer_id,
                              plan_id=signature.plan_id,
                              company_id=signature.company_id,
                              date_start=signature.date_start,
                              date_end=signature.date_end,
                              is_notification_allowed=signature.is_notification_allowed
        )
    db.add(new_signature)
    db.flush()
    return new_signature.to_dict()

def get_signature_by_id(db: Session, signature_id: UUID4):
    """
    Get a signature by its ID.
    """
    signature = get_or_404(db, Signature, signature_id)
    return signature
