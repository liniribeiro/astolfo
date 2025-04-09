
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

    signatures = relationship('Signature', uselist=True, backref='plan')

    tasks = relationship('TaskPlans', back_populates='plan', uselist=True)

    def to_dict(self):
        return {
            'id': str(self.id),
            'title': self.title,
            'description': self.description,
            'price': self.price,
            'days': self.days,
            "company_id": str(self.company_id),
            'tasks':[
                    {'id': str(tp.task.id), 'title': tp.task.title}
                    for tp in self.tasks if tp.task
            ]
        }
