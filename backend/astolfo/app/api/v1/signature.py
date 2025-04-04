from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database.queries import get_signature_by_id, create_signature
from database.session import get_sync_db
from schemas import SignatureSchema

router = APIRouter()

@router.get(
    "/{signature_id}"
)
def api_get_signature_by_id(
    signature_id: str,
    session: Session = Depends(get_sync_db),
):
    customer = get_signature_by_id(session, signature_id)
    return SignatureSchema(**customer.to_dict())

@router.post(
    "/"
)
def api_create_signature(
    signature: SignatureSchema,
    session: Session = Depends(get_sync_db),
):
    new_signature = create_signature(session, signature)
    return SignatureSchema(**new_signature.to_dict())

@router.delete(
    "/{signature_id}"
)
def api_delete_signature(
    signature_id: str,
    session: Session = Depends(get_sync_db),
):
    signature = get_signature_by_id(session, signature_id)
    if not signature:
        return {"error": "Signature not found"}
    session.delete(signature)
    session.commit()
    return {"message": "Signature deleted successfully"}
