

from sqlalchemy import Column, DateTime, ForeignKey, Boolean, Integer, Float, String, Time
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from database.models.base import BaseModel


class CompanyTask(BaseModel):
    __tablename__ = 'company_task'

    total_minutes = Column(Integer)
    price = Column(Float)
    title = Column(String)
    description = Column(String)

    company_id = Column(UUID(as_uuid=True), ForeignKey('company.id'), nullable=False)
    company = relationship('Company', back_populates="tasks")

    schedules = relationship('CompanySchedule', uselist=True, backref='company_task')

    def __repr__(self):
        return f'Signature {self.name}'

    def to_dict(self):
        return {
            'id': str(self.id),
            'total_minutes': str(self.total_minutes),
            'price': str(self.price),
            'title': self.title,
            'description': self.description,
            'company_id': str(self.company_id)
        }
