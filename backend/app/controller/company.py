from sqlalchemy.orm import Session

from database import Company
from database.models.user import Roles
from database.queries.company import create_company
from database.queries.user import create_user

from exceptions.exceptions import CreateError
from schemas import SetupCompanyAccountSchema


def setup_company_account(db: Session, company_account: SetupCompanyAccountSchema) -> Company:
    """
    Setup a company account with the given details.
    """
    # Create a new company instance
    new_company = create_company(db,
                                 company_account.name,
                                 company_account.tenant_name,
                                 company_account.logo)

    admin_name = company_account.email.split('@')[0]
    # Create a new admin user instance
    new_admin_user = create_user(
        db,
        new_company.id,
        admin_name,
        company_account.email,
        Roles.admin,
        company_account.password
    )
    if not new_admin_user:
        raise CreateError('Error creating admin user', 500)

    return new_company

