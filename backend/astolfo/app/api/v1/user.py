from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database.queries import get_all_users_from_company_id, get_user
from database.session import get_sync_db
from schemas import LoginSchema

router = APIRouter()

@router.get(
    "/{company_id}"
)
def api_get_all_users(
    company_id: str,
    session: Session = Depends(get_sync_db),
):
    """
    Get an Item group by ns
    TODO: Ensure that the user is authenticated and has the right to access this endpoint.
    """
    users = get_all_users_from_company_id(session, company_id)
    return users


@router.post(
    "/login"
)
def api_user_login(
    login: LoginSchema,
    session: Session = Depends(get_sync_db),
):
    user = get_user(session, login.email, login.password)
    if not user:
         return {"message": "Invalid credentials"}, 401
    return {"message": "Login successful", "user": user.to_dict()}


