from sqlalchemy.orm import Session

from database import Plan, TaskPlans, CompanyTask
from schemas import PlanSchema


def create_plan_and_tasks(
    db: Session,
    plan: PlanSchema,
):
    """
    Create a new plan and its associated tasks in the database.
    """
    # Create the plan
    # validate if task_ids exist before creating the plan
    task_ids_not_found = []
    for task_id in plan.tasks:
        task = db.query(CompanyTask).filter(CompanyTask.id == task_id).first()
        if not task:
            task_ids_not_found.append(task_id)
    if task_ids_not_found:
        raise ValueError(f"Task IDs not found: {task_ids_not_found}")

    new_plan = Plan(
        title=plan.title,
        description=plan.description,
        price=plan.price,
        days=str(plan.days), #TODO: convert db field to int
        company_id=plan.company_id
    )
    db.add(new_plan)
    db.flush()

    # Create the tasks associated with the plan
    for task_id in  plan.tasks:
        new_task = TaskPlans(
            task_id=task_id,
            plan_id=new_plan.id
        )
        db.add(new_task)

    db.commit()
    db.refresh(new_plan)
    return new_plan
