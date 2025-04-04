from datetime import date, datetime
from typing import Optional, List

from pydantic import BaseModel, UUID4, EmailStr, Field


class LoginSchema(BaseModel):
    email: EmailStr
    password: str

class CompanySchema(BaseModel):
    id: str
    name: str
    tenant_name: str
    logo: Optional[str] = None


class SetupCompanyAccountSchema(BaseModel):
    name: str
    tenant_name: str
    logo: Optional[str] = None
    email: str
    password: str


class PlanSchemaInput(BaseModel):
    title: Optional[str]
    description: Optional[str]
    price: Optional[float]
    days: Optional[int]
    company_id: Optional[str]
    tasks: List[UUID4]

class PlanSchemaOutput(BaseModel):
    id: Optional[str]
    title: Optional[str]
    description: Optional[str]
    price: Optional[float]
    days: Optional[int]
    tasks: Optional[List[dict]]

class PlanListSchemaOutput(BaseModel):
    plans: List[PlanSchemaOutput]


class CustomerSchemaInput(BaseModel):
    email: EmailStr
    phone: str
    name: str
    company_id: str


class CustomerSchemaOutput(BaseModel):
    id: str
    name: str
    email: EmailStr
    phone: str
    company_id: str

class CustomersSchema(BaseModel):
    customers: List[CustomerSchemaOutput]



class SignatureSchema(BaseModel):
    id: str = Field(default=None)
    customer_id: Optional[str]
    plan_id: Optional[str]
    date_start: Optional[datetime]
    date_end: Optional[datetime]
    is_notification_allowed: Optional[bool]
    company_id: Optional[str]


class SignaturesSchema(BaseModel):
    signatures: List[SignatureSchema]



class CompanyTaskSchema(BaseModel):
    id: str = Field(default=None)
    title: Optional[str]
    description: Optional[str]
    price: Optional[float]
    company_id: Optional[str]
    total_minutes: Optional[int]


class CompanyTasksSchema(BaseModel):
    tasks: List[CompanyTaskSchema]