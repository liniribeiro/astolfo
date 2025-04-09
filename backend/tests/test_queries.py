# test_queries.py
from datetime import datetime

import pytest
from unittest.mock import MagicMock
from sqlalchemy.orm import Session

from database.queries import (
    get_all_companies, get_company_by_id, create_company, create_user,
    get_all_users_from_company_id, get_user, get_plan_by_company_id,
    get_plan_by_id, create_plan, create_task_plans, create_customer,
    get_customer_by_id, get_signature_by_customer_id,
    create_signature, get_signature_by_id, get_company_task_by_id, create_company_task, delete_company
)
from database import Company, User, Plan, Customer, Signature, CompanyTask
from schemas import SignatureSchema, CompanyTaskSchema

@pytest.fixture
def db_session():
    return MagicMock(spec=Session)

def test_get_all_companies(db_session):
    db_session.query().all.return_value = [Company(id="1"), Company(id="2")]
    companies = get_all_companies(db_session)
    assert len(companies) == 2

def test_get_company_by_id(db_session):
    db_session.query().filter().first.return_value = Company(id="1")
    company = get_company_by_id(db_session, "1")
    assert company.id == "1"


def test_create_user(db_session):
    db_session.add.return_value = None
    db_session.commit.return_value = None
    db_session.refresh.return_value = None
    new_user = create_user(db_session, "1", "Test User", "test@example.com", "admin", "password")
    assert new_user["name"] == "Test User"

def test_get_all_users_from_company_id(db_session):
    db_session.query().filter().all.return_value = [User(id="1"), User(id="2")]
    users = get_all_users_from_company_id(db_session, "1")
    assert len(users) == 2

def test_get_user(db_session):
    db_session.query().filter().first.return_value = User(id="1")
    user = get_user(db_session, "test@example.com", "password")
    assert user.id == "1"

def test_get_plan_by_company_id(db_session):
    db_session.query().filter().all.return_value = [Plan(id="1"), Plan(id="2")]
    plans = get_plan_by_company_id(db_session, "1")
    assert len(plans) == 2

def test_get_plan_by_id(db_session):
    db_session.query().filter().first.return_value = Plan(id="1")
    plan = get_plan_by_id(db_session, "1")
    assert plan.id == "1"

def test_create_plan(db_session):
    db_session.add.return_value = None
    db_session.commit.return_value = None
    db_session.refresh.return_value = None
    new_plan = create_plan(db_session, "Test Plan", "Description", 100.0, 30, "1")
    assert new_plan["title"] == "Test Plan"

def test_create_task_plans(db_session):
    db_session.add.return_value = None
    db_session.commit.return_value = None
    tasks = [{"task_id": "1", "plan_id": "1"}, {"task_id": "2", "plan_id": "1"}]
    create_task_plans(db_session, tasks)
    assert db_session.add.call_count == 2

def test_create_customer(db_session):
    db_session.add.return_value = None
    db_session.commit.return_value = None
    db_session.refresh.return_value = None
    new_customer = create_customer(db_session, "Test Customer", "test@example.com", "1234567890", "1")
    assert new_customer["name"] == "Test Customer"

def test_get_customer_by_id(db_session):
    db_session.query().filter().first.return_value = Customer(id="1")
    customer = get_customer_by_id(db_session, "1")
    assert customer.id == "1"

def test_get_signature_by_customer_id(db_session):
    db_session.query().filter().first.return_value = Signature(id="1")
    signature = get_signature_by_customer_id(db_session, "1")
    assert signature.id == "1"


def test_create_signature(db_session):
    db_session.add.return_value = None
    db_session.commit.return_value = None
    db_session.refresh.return_value = None
    signature_schema = SignatureSchema(
        customer_id="1", plan_id="1", company_id="1", date_start=datetime.strptime("2023-01-01", "%Y-%m-%d") ,
        date_end=datetime.strptime("2023-12-31", "%Y-%m-%d"), is_notification_allowed=True
    )
    new_signature = create_signature(db_session, signature_schema)
    assert new_signature["customer_id"] == "1"

def test_get_signature_by_id(db_session):
    db_session.query().filter().first.return_value = Signature(id="1")
    signature = get_signature_by_id(db_session, "1")
    assert signature.id == "1"

def test_get_company_task_by_id(db_session):
    db_session.query().filter().all.return_value = [CompanyTask(id="1"), CompanyTask(id="2")]
    tasks = get_company_task_by_id(db_session, "1")
    assert len(tasks) == 2

def test_create_company_task(db_session):
    db_session.add.return_value = None
    db_session.commit.return_value = None
    db_session.refresh.return_value = None
    task_schema = CompanyTaskSchema(
        title="Test Task", description="Description", price=100.0, company_id="1", total_minutes=60
    )
    new_task = create_company_task(db_session, task_schema)
    assert new_task["title"] == "Test Task"