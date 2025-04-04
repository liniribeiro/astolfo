
from sqlalchemy import Column, String, Float, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from database.models.base import BaseModel


class Plan(BaseModel):
    __tablename__ = 'plan'

    title = Column(String)
    description = Column(String)
    price = Column(Float)
    days = Column(String)

    company_id = Column(UUID(as_uuid=True), ForeignKey('company.id'))
    company = relationship('Company', back_populates="plans")

    tasks = relationship('TaskPlans')
    signatures = relationship('Signature', uselist=True, backref='plan')

    def to_dict(self):
        return {
            'id': str(self.id),
            'title': self.title,
            'description': self.description,
            'price': self.price,
            'days': self.days,
            'tasks': [{'id': str(task_plans.task.id), 'title': task_plans.task.title} for task_plans in self.tasks if len(self.tasks) > 0]
        }
