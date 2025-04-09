from fastapi import APIRouter, Depends
from pydantic import UUID4
from sqlalchemy.orm import Session

from database.queries.user import get_user, get_user_by_company_id
from database.session import get_sync_db
from schemas import LoginSchema

router = APIRouter()

@router.get(
    "/{company_id}"
)
def get_company_users(
    company_id: UUID4,
    session: Session = Depends(get_sync_db),
):
    """
    Get an Item group by ns
    TODO: Ensure that the user is authenticated and has the right to access this endpoint.
    """
    users = get_user_by_company_id(session, company_id)
    return users


@router.post(
    "/login"
)
def login(
    user_data: LoginSchema,
    session: Session = Depends(get_sync_db),
):
    user = get_user(session, user_data.email, user_data.password)
    if not user:
         return {"message": "Invalid credentials"}, 401
    return {"message": "Login successful", "user": user.to_dict()}


