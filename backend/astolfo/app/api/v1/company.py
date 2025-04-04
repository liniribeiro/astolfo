from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database.queries import get_all_companies, get_company_by_id
from database.session import get_sync_db
from schemas import CompanySchema, SetupCompanyAccountSchema
from controller.company import setup_company_account

router = APIRouter()

@router.get(
    "/"
)
def api_get_all_company(
    session: Session = Depends(get_sync_db),
):
    """
    Get an Item group by ns
    """
    companies = get_all_companies(session)
    return [CompanySchema(**company.to_dict()) for company in companies]


@router.get(
    "/{company_id}"
)
def get_by_id(
    company_id: str,
    session: Session = Depends(get_sync_db),
):
    """
    Get an Item group by ns
    """
    company = get_company_by_id(session, company_id)
    return CompanySchema(**company.to_dict())

@router.post(
    "/"
)
def create(
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
def delete(
    company_id: str,
    session: Session = Depends(get_sync_db),
):
    """
    Get an Item group by ns
    """
    company = get_company_by_id(session, company_id)
    session.delete(company)
    session.commit()
    return {"message": "Company deleted successfully"}
