from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database.session import get_sync_db

router = APIRouter()

@router.get(
    "/"
)
def get_home(
    session: Session = Depends(get_sync_db),
):
    return {"get": "hello world"}
