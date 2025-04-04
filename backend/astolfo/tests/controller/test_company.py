from unittest.mock import MagicMock, patch

import pytest
from sqlalchemy.orm import Session

from controller.company import setup_company_account
from database import Company
from exceptions.exceptions import CreateError
from schemas import SetupCompanyAccountSchema


@pytest.fixture
def db_session():
    return MagicMock(spec=Session)

@pytest.fixture
def company_account():
    return SetupCompanyAccountSchema(
        name="Test Company",
        tenant_name="test_tenant",
        logo="test_logo.png",
        email="admin@test.com",
        password="password123"
    )

@patch("controller.company.create_company")
@patch("controller.company.create_user")
def test_setup_company_account_success(create_user_mock, create_company_mock, db_session, company_account):
    # Arrange
    create_company_mock.return_value = Company(id="test_company_id")
    create_user_mock.return_value = True

    # Act
    result = setup_company_account(db_session, company_account)

    # Assert
    create_company_mock.assert_called_once_with(
        db_session,
        company_account.name,
        company_account.tenant_name,
        company_account.logo
    )
    create_user_mock.assert_called_once_with(
        db_session,
        "test_company_id",
        "admin",
        company_account.email,
        "admin",
        company_account.password
    )
    assert result.id == "test_company_id"

@patch("controller.company.create_company")
@patch("controller.company.create_user")
def test_setup_company_account_create_user_failure(create_user_mock, create_company_mock, db_session, company_account):
    # Arrange
    create_company_mock.return_value = Company(id="test_company_id")
    create_user_mock.return_value = False

    # Act & Assert
    with pytest.raises(CreateError):
        setup_company_account(db_session, company_account)

    create_company_mock.assert_called_once_with(
        db_session,
        company_account.name,
        company_account.tenant_name,
        company_account.logo
    )
    create_user_mock.assert_called_once_with(
        db_session,
        "test_company_id",
        "admin",
        company_account.email,
        "admin",
        company_account.password
    )