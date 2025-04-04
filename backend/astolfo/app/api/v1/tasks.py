from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database.queries import get_company_task_by_id, create_company_task
from database.session import get_sync_db
from schemas import CompanyTaskSchema

router = APIRouter()

@router.get(
    "/{task_id}"
)
def api_get_task_by_id(
    task_id: str,
    session: Session = Depends(get_sync_db),
):
    task = get_company_task_by_id(session, task_id)
    return CompanyTaskSchema(**task.to_dict())

@router.post(
    "/"
)
def api_create_signature(
    task: CompanyTaskSchema,
    session: Session = Depends(get_sync_db),
):
    new_task = create_company_task(session, task)
    return CompanyTaskSchema(**new_task.to_dict())

@router.delete(
    "/{task_id}"
)
def api_delete_task(
    task_id: str,
    session: Session = Depends(get_sync_db),
):
    task = get_company_task_by_id(session, task_id)
    if not task:
        return {"error": "Task not found"}
    session.delete(task)
    session.commit()
    return {"message": "Task deleted successfully"}
