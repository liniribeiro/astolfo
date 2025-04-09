from typing import TypeVar

from pydantic import UUID4
from sqlalchemy.orm import Session

from database import Company, User, Plan, TaskPlans, Customer, Signature, CompanyTask
from database.models.base import BaseModel
from exceptions.exceptions import NotFound

ModelType = TypeVar("ModelType", bound=BaseModel)

def get_or_404(db: Session, model: type[ModelType], model_id: UUID4):
    """
    Get an object by its ID or raise a 404 error if not found.
    """
    obj = db.query(model).filter(model.id == str(model_id)).first()
    if not obj:
        raise NotFound("Object not found")
    return obj