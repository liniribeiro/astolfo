from sqlalchemy.orm import Session

from database import Company, User, Plan, TaskPlans, Customer, Signature, CompanyTask
from schemas import SignatureSchema, CompanyTaskSchema


def get_all_companies(db: Session) -> list:
    """
    Get all companies from the database.
    """
    companies = db.query(Company).all()
    return companies


def get_company_by_id(db: Session, company_id: str) -> Company | None:
    """
    Get a company by its ID from the database.
    """
    company = db.query(Company).filter(Company.id == company_id).first()
    return company


def create_company(db: Session, name: str, tenant_name: str, logo: str) -> Company:
    """
    Create a new company in the database.
    """
    new_company = Company(name=name, tenant_name=tenant_name, logo=logo)
    db.add(new_company)
    db.commit()
    db.refresh(new_company)
    return new_company

def create_user(db: Session, company_id: str, name: str, email: str, role: str, password: str) -> dict:
    """
    Create a new user in the database.
    """
    new_user = User(company_id=company_id, name=name, email=email, role=role, password=password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user.to_dict()

def get_all_users_from_company_id(db: Session, company_id: str):
    """
    Get all users from a company by its ID.
    """
    users = db.query(User).filter(User.company_id == company_id).all()
    return users


def get_user(db: Session, email: str, password: str) -> User | None:
    """
    Get a user by email and password.
    """
    user = db.query(User).filter(User.email == email, User.password == password).first()
    return user


def get_plan_by_company_id(db: Session, company_id: str):
    """
    Get all plans from a company by its ID.
    """
    plans = db.query(Plan).filter(Plan.company_id == company_id).all()
    return plans

def get_plan_by_id(db: Session, plan_id: str):
    """
    Get a plan by its ID.
    """
    plan = db.query(Plan).filter(Plan.id == plan_id).first()
    return plan

def create_plan(db: Session, title: str, description: str, price: float, days: int, company_id: str):
    """
    Create a new plan in the database.
    """
    new_plan = Plan(title=title, description=description, price=price, days=str(days), company_id=company_id)
    db.add(new_plan)
    db.commit()
    db.refresh(new_plan)
    return new_plan.to_dict()

def create_task_plans(db: Session, tasks: list):
    """
    Create new tasks in the database.
    """
    for task in tasks:
        new_task = TaskPlans(task_id=task['task_id'], plan_id=task['plan_id'])
        db.add(new_task)
    db.commit()

def create_customer(db: Session, name: str, email: str, phone: str, company_id: str):
    """
    Create a new customer in the database.
    """
    new_customer = Customer(name=name, email=email, phone=phone, company_id=company_id)
    db.add(new_customer)
    db.commit()
    db.refresh(new_customer)
    return new_customer.to_dict()

def get_customer_by_id(db: Session, customer_id: str):
    """
    Get a customer by its ID.
    """
    customer = db.query(Customer).filter(Customer.id == customer_id).first()
    return customer

def get_signature_by_customer_id(db: Session, customer_id: str):
    """
    Get a signature by customer ID.
    """
    signature = db.query(Signature).filter(Signature.customer_id == customer_id).first()
    return signature

def get_signature_by_plan_id(db: Session, plan_id: str):
    """
    Get a signature by plan ID.
    """
    signature = db.query(Signature).filter(Signature.plan_id == plan_id).first()
    return signature

def create_signature(db: Session, signature: SignatureSchema):
    """
    Create a new signature in the database.
    """
    new_signature = Signature(customer_id=signature.customer_id,
                              plan_id=signature.plan_id,
                              company_id=signature.company_id,
                              date_start=signature.date_start,
                              date_end=signature.date_end,
                              is_notification_allowed=signature.is_notification_allowed
        )
    db.add(new_signature)
    db.commit()
    db.refresh(new_signature)
    return new_signature.to_dict()

def get_signature_by_id(db: Session, signature_id: str):
    """
    Get a signature by its ID.
    """
    signature = db.query(Signature).filter(Signature.id == signature_id).first()
    return signature


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
    new_task = CompanyTask(title=task.title, description=task.description, price=task.price, company_id=task.company_id)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task.to_dict()
