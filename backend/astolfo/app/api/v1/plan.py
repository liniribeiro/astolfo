from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database.queries import get_plan_by_company_id, get_plan_by_id, create_plan, create_task_plans
from database.session import get_sync_db
from schemas import PlanListSchemaOutput, PlanSchemaOutput, PlanSchemaInput

router = APIRouter()

@router.get(
    "/{company_id}"
)
def api_get_plan_from_company_id(
    company_id: str,
    session: Session = Depends(get_sync_db),
) -> PlanListSchemaOutput:
    plans = get_plan_by_company_id(session, company_id)
    return PlanListSchemaOutput(plans=[PlanSchemaOutput(**plan.to_dict()) for plan in plans])

@router.get(
    "/{plan_id}"
)
def api_get_plan_by_id(
    plan_id: str,
    session: Session = Depends(get_sync_db),
) -> PlanSchemaOutput:
    plan = get_plan_by_id(session, plan_id)
    return PlanSchemaOutput(**plan.to_dict())

@router.post(
    "/"
)
def api_create_plan(
    plan: PlanSchemaInput,
    session: Session = Depends(get_sync_db),
) -> PlanSchemaOutput:
    new_plan = create_plan(session, plan.title, plan.description, plan.price, plan.days, plan.company_id)
    create_task_plans(session, plan.tasks)
    return PlanSchemaOutput(**new_plan.to_dict())
