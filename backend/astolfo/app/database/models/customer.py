
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from database.models.base import BaseModel


class Customer(BaseModel):
    __tablename__ = 'customer'

    name = Column(String)
    email = Column(String, unique=True)
    phone = Column(String, unique=True)
    company_id = Column(UUID(as_uuid=True), ForeignKey('company.id'), nullable=False)

    schedules = relationship('CompanySchedule', uselist=True, backref='customer')
    signatures = relationship('Signature', uselist=True, backref='customer')

    def __repr__(self):
        return f'Customer {self.name}'

    def to_dict(self):
        return {
            'id': str(self.id),
            'email': self.email,
            'phone': self.phone,
            'name': self.name,
            'company_id': str(self.company_id)
        }
