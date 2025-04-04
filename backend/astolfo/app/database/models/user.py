
from sqlalchemy import Column, ForeignKey,  String, Enum
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from database.models.base import BaseModel


class Roles(Enum):
    admin = "admin"
    reader = "reader"
    scheduler = "scheduler"


class User(BaseModel):
    __tablename__ = 'user'

    name = Column(String)
    email = Column(String)
    password = Column(String)
    role = Column(String)

    company_id = Column(UUID(as_uuid=True), ForeignKey('company.id'))
    company = relationship('Company', back_populates="users")

    def __repr__(self):
        return f'User {self.name}'

    def to_dict(self):
        return {
            'id': str(self.id),
            'name': self.name,
            'role': self.role,
            'email': self.email,
            'company': self.company.to_dict() if self.company else None,
        }
