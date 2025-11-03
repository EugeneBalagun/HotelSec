from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..database import get_db
from ..schemas.lead import LeadCreate, LeadResponseMessage
from ..services.lead import lead_service
from ..auth import get_current_user

router = APIRouter()

@router.post("/lead", response_model=LeadResponseMessage)
def create_lead_endpoint(
    lead: LeadCreate,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    try:
        return lead_service.create_lead(db, lead)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))