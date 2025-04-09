from sqlalchemy.orm import Session

from database import User


def create_user(db: Session, company_id: str, name: str, email: str, role: str, password: str) -> dict:
    """
    Create a new user in the database.
    """
    new_user = User(company_id=company_id, name=name, email=email, role=role, password=password)
    db.add(new_user)
    db.flush()
    return new_user.to_dict()

def get_user_by_company_id(db: Session, company_id: str):
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
