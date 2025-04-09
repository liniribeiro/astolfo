

from sqlalchemy import Column, DateTime, ForeignKey, Time
from sqlalchemy.dialects.postgresql import UUID

from database.models.base import BaseModel


class CompanySchedule(BaseModel):
    __tablename__ = 'company_schedule'

    customer_id = Column(UUID(as_uuid=True), ForeignKey('customer.id'), nullable=False)
    task_id = Column(UUID(as_uuid=True), ForeignKey('company_task.id'), nullable=False)
    company_id = Column(UUID(as_uuid=True), ForeignKey('company.id'), nullable=False)

    date = Column(DateTime, nullable=False)
    hour = Column(Time, nullable=False)

    def __repr__(self):
        return f'Signature {self.name}'

    def to_dict(self):
        return {
            'id': str(self.id),
            'customer_id': str(self.customer_id)
        }
