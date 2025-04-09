from fastapi import APIRouter, Depends
from pydantic import UUID4
from sqlalchemy.orm import Session

from database import Signature

from database.queries.base import get_or_404
from database.queries.signature import create_signature
from database.session import get_sync_db
from schemas import SignatureSchema

router = APIRouter()

@router.get(
    "/{signature_id}"
)
def get_signature(
    signature_id: UUID4,
    session: Session = Depends(get_sync_db),
):
    customer = get_or_404(session, Signature, signature_id)
    return SignatureSchema(**customer.to_dict())

@router.post(
    "/"
)
def save_signature(
    signature: SignatureSchema,
    session: Session = Depends(get_sync_db),
):
    new_signature = create_signature(session, signature)
    return SignatureSchema(**new_signature.to_dict())

@router.delete(
    "/{signature_id}"
)
def delete_signature(
    signature_id: UUID4,
    session: Session = Depends(get_sync_db),
):
    signature = get_or_404(session, Signature, signature_id)
    session.delete(signature)
    session.commit()
    return {"message": "Signature deleted successfully"}
