

from sqlalchemy import Column, DateTime, ForeignKey, Boolean, Integer, Float, String, Time
from sqlalchemy.orm import relationship

from database.models.base import BaseModel


class Company(BaseModel):
    __tablename__ = 'company'

    name = Column(String, unique=False)
    tenant_name = Column(String, nullable=False, unique=True)
    logo = Column(String)

    users = relationship("User", uselist=True, back_populates='company')
    tasks = relationship("CompanyTask", uselist=True, back_populates='company')
    plans = relationship('Plan', uselist=True, back_populates='company')

    signatures = relationship('Signature', uselist=True, backref='company')
    customers = relationship('Customer', uselist=True, backref='company')
    schedules = relationship('CompanySchedule', uselist=True, backref='company')

    def __repr__(self):
        return f'Company {self.name}'

    def to_dict(self):
        return {
            'id': str(self.id),
            'name': str(self.name),
            'tenant_name': str(self.tenant_name),
            'logo': str(self.logo) if self.logo else None
        }
