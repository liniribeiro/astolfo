from fastapi import APIRouter, Depends
from pydantic import UUID4
from sqlalchemy.orm import Session

from database import Company
from database.queries.base import get_or_404
from database.queries.company import get_all, get_by_id, delete_company_by_id
from database.session import get_sync_db
from schemas import CompanySchema, SetupCompanyAccountSchema
from controller.company import setup_company_account

router = APIRouter()

@router.get(
    "/"
)
def get_companies(
    session: Session = Depends(get_sync_db),
):
    """
    Get an Item group by ns
    """
    companies = get_all(session)
    return [CompanySchema(**company.to_dict()) for company in companies]


@router.get(
    "/{company_id}"
)
def get_company_by_id(
    company_id: UUID4,
    session: Session = Depends(get_sync_db),
):
    """
    Get an Item group by ns
    """
    company = get_by_id(session, company_id)
    return CompanySchema(**company.to_dict())

@router.post(
    "/"
)
def save_company(
    company_account: SetupCompanyAccountSchema,
    session: Session = Depends(get_sync_db),
):
    """
    Get an Item group by ns
    """
    company = setup_company_account(session, company_account)
    return CompanySchema(**company.to_dict())

@router.delete(
    "/{company_id}"
)
def delete_company(
    company_id: UUID4,
    session: Session = Depends(get_sync_db),
):
    """
    Get an Item group by ns
    """
    delete_company_by_id(session, company_id)
    return {"message": "Company deleted successfully"}
