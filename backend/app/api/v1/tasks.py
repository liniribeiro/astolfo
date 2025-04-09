from fastapi import APIRouter, Depends
from pydantic import UUID4
from sqlalchemy.orm import Session

from database import CompanyTask
from database.queries.base import get_or_404
from database.queries.tasks import create_company_task, get_by_company_id
from database.session import get_sync_db
from schemas import CompanyTaskSchema, CompanyTasksSchema

router = APIRouter()

@router.get(
    "/{task_id}"
)
def get_task_by_id(
    task_id: UUID4,
    session: Session = Depends(get_sync_db),
):
    task = get_or_404(session, CompanyTask, task_id)
    return CompanyTaskSchema(**task.to_dict())

@router.get(
    "/{company_id}"
)
def get_task_by_company_id(
    company_id: UUID4,
    session: Session = Depends(get_sync_db),
):
    task = get_by_company_id(session, company_id)
    return CompanyTasksSchema(tasks=[CompanyTaskSchema(**task.to_dict()) for task in task])

@router.post(
    "/"
)
def save_task(
    task: CompanyTaskSchema,
    session: Session = Depends(get_sync_db),
):
    new_task = create_company_task(session, task)
    return CompanyTaskSchema(**new_task.to_dict())

@router.delete(
    "/{task_id}"
)
def delete_task(
    task_id: UUID4,
    session: Session = Depends(get_sync_db),
):
    task = get_or_404(session, CompanyTask, task_id)
    session.delete(task)
    session.commit()
    return {"message": "Task deleted successfully"}
