from datetime import date, datetime
from typing import Optional, List

from pydantic import BaseModel, UUID4, EmailStr, Field


class LoginSchema(BaseModel):
    email: EmailStr
    password: str

class CompanySchema(BaseModel):
    id: UUID4
    name: str
    tenant_name: str
    logo: Optional[str] = None


class SetupCompanyAccountSchema(BaseModel):
    name: str
    tenant_name: str
    logo: Optional[str] = None
    email: EmailStr
    password: str

class PlanSchema(BaseModel):
    id: UUID4 = Field(default=None)
    company_id: UUID4
    title: str = Field(min_length=3, max_length=50)
    description: str = Field(default=None, min_length=3, max_length=50)
    price: float
    days: int
    tasks: list = Field(default=None)

class PlansSchema(BaseModel):
    plans: List[PlanSchema]



class CustomerSchema(BaseModel):
    id: UUID4 = Field(default=None)
    name: str
    email: EmailStr
    phone: str
    company_id: UUID4

class CustomersSchema(BaseModel):
    customers: List[CustomerSchema]


class SignatureSchema(BaseModel):
    id: UUID4 = Field(default=None)
    customer_id: UUID4
    plan_id: UUID4
    company_id: UUID4
    date_start: Optional[datetime]
    date_end: Optional[datetime]
    is_notification_allowed: Optional[bool]



class SignaturesSchema(BaseModel):
    signatures: List[SignatureSchema]


class CompanyTaskSchema(BaseModel):
    id: UUID4 = Field(default=None)
    title: str = Field(min_length=3, max_length=50)
    description: str = Field(default=None, min_length=3, max_length=50)
    price: float
    company_id: UUID4
    total_minutes: int


class CompanyTasksSchema(BaseModel):
    tasks: List[CompanyTaskSchema]