

from sqlalchemy import Column, DateTime, ForeignKey, Boolean
from sqlalchemy.dialects.postgresql import UUID

from database.models.base import BaseModel


class Signature(BaseModel):
    __tablename__ = 'signature'

    company_id = Column(UUID(as_uuid=True), ForeignKey('company.id'), nullable=False)
    customer_id = Column(UUID(as_uuid=True), ForeignKey('customer.id'), nullable=False)
    plan_id = Column(UUID(as_uuid=True), ForeignKey('plan.id'), nullable=False)

    date_start = Column(DateTime, nullable=False)
    date_end = Column(DateTime, nullable=False)

    is_notification_allowed = Column(Boolean)

    def __repr__(self):
        return f'Signature {self.name}'

    def to_dict(self):
        return {
            'id': str(self.id),
            'customer_id': str(self.customer_id),
            'plan_id': str(self.plan_id),
            'date_start': self.date_start,
            'date_end': self.date_end,
            'is_notification_allowed': self.is_notification_allowed
        }
