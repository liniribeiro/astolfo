from typing import TypeVar

from pydantic.v1 import UUID4
from sqlalchemy.orm import Session

from database import Company, User, Plan, TaskPlans, Customer, Signature, CompanyTask
from database.models.base import BaseModel
from database.queries.base import get_or_404
from exceptions.exceptions import DuplicatedData, NotFound
from schemas import SignatureSchema, CompanyTaskSchema


def get_plan_by_company_id(db: Session, company_id: str):
    """
    Get all plans from a company by its ID.
    """
    plans = db.query(Plan).filter(Plan.company_id == company_id).all()
    return plans

def get_plan_by_id(db: Session, plan_id: UUID4):
    """
    Get a plan by its ID.
    """
    plan = get_or_404(db, Plan, plan_id)
    return plan

def create_plan(db: Session, title: str, description: str, price: float, days: int, company_id: str):
    """
    Create a new plan in the database.
    """
    new_plan = Plan(title=title, description=description, price=price, days=str(days), company_id=company_id)
    db.add(new_plan)
    db.flush()
    return new_plan