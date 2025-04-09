
from typing import TypeVar

from pydantic.v1 import UUID4
from sqlalchemy.orm import Session

from database import TaskPlans, Customer, Signature, CompanyTask

from schemas import  CompanyTaskSchema


def create_task_plans(db: Session, tasks: list):
    """
    Create new tasks in the database.
    """
    for task in tasks:
        new_task = TaskPlans(task_id=task['task_id'], plan_id=task['plan_id'])
        db.add(new_task)
    db.commit()


def get_company_task_by_id(db: Session, company_id: str):
    """
    Get all tasks from a company by its ID.
    """
    tasks = db.query(CompanyTask).filter(CompanyTask.company_id == company_id).all()
    return tasks


def create_company_task(db: Session, task: CompanyTaskSchema):
    """
    Create a new task in the database.
    """
    new_task = CompanyTask(title=task.title,
                           description=task.description,
                           price=task.price,
                           company_id=task.company_id,
                           total_minutes=task.total_minutes)
    db.add(new_task)
    db.flush()
    return new_task


def get_by_company_id(db: Session, company_id: str):
    """
    Get all tasks from a company by its ID.
    """
    tasks = db.query(CompanyTask).filter(CompanyTask.company_id == company_id).all()
    return tasks
