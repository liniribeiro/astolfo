from fastapi import APIRouter, Depends
from pydantic import UUID4
from sqlalchemy.orm import Session

from controller.plan import create_plan_and_tasks
from database import Plan

from database.queries.base import get_or_404
from database.queries.plan import get_plan_by_company_id, create_plan
from database.queries.tasks import create_task_plans
from database.session import get_sync_db
from schemas import PlansSchema, PlanSchema

router = APIRouter()

@router.get(
    "/"
)
def get_plans(
    company_id: UUID4,
    session: Session = Depends(get_sync_db),
) -> PlansSchema:
    plans = get_plan_by_company_id(session, company_id)
    return PlansSchema(plans=[PlanSchema(**plan.to_dict()) for plan in plans])

@router.get(
    "/{plan_id}"
)
def get_plan(
    plan_id: UUID4,
    session: Session = Depends(get_sync_db),
) -> PlanSchema:
    plan = get_or_404(session, Plan, plan_id)
    return PlanSchema(**plan.to_dict())


@router.post(
    "/"
)
def save_plan(
    plan: PlanSchema,
    session: Session = Depends(get_sync_db),
) -> PlanSchema:
    new_plan = create_plan_and_tasks(session, plan)
    return PlanSchema(**new_plan.to_dict())


@router.delete(
    "/{plan_id}"
)
def delete_plan(
    plan_id: UUID4,
    session: Session = Depends(get_sync_db),
) -> dict:
    plan = get_or_404(session, Plan, plan_id)
    # TODO: delete Task_plans before delete plans
    session.delete(plan)
    return {"message": "Plan deleted successfully"}