from pydantic import UUID4
from sqlalchemy.orm import Session

from database import Company
from database.queries.base import get_or_404
from exceptions.exceptions import DuplicatedData


def get_all(db: Session) -> list:
    """
    Get all companies from the database.
    """
    companies = db.query(Company).all()
    return companies


def get_by_id(db: Session, company_id: UUID4) -> Company | None:
    """
    Get a company by its ID from the database.
    """
    company = get_or_404(db, Company, company_id)
    return company


def create_company(db: Session, name: str, tenant_name: str, logo: str) -> Company:
    """
    Create a new company in the database.
    """

    existing_company = db.query(Company).filter(Company.tenant_name == tenant_name).first()
    if existing_company:
        raise DuplicatedData("Company with this tenant name already exists.")

    new_company = Company(name=name, tenant_name=tenant_name, logo=logo)
    db.add(new_company)
    db.flush()
    return new_company


def delete_company_by_id(db: Session, company_id: UUID4):
    """
    Delete a company by its ID.
    """
    company = get_or_404(db, Company, company_id)
    db.delete(company)
    db.flush()