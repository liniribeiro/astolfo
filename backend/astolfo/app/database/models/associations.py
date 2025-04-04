
from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from database.models.base import BaseModel


class TaskPlans(BaseModel):
    __tablename__ = 'task_plans'

    plan_id = Column(UUID(as_uuid=True), ForeignKey('plan.id'), primary_key=True)
    task = relationship("CompanyTask")
    task_id = Column(UUID(as_uuid=True), ForeignKey('company_task.id'), primary_key=True)
