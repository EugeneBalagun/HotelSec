from sqlalchemy.orm import Session
from ..repositories.lead import lead_repo
from ..schemas.lead import LeadCreate, LeadResponseMessage

class LeadService:
    def create_lead(self, db: Session, lead: LeadCreate) -> LeadResponseMessage:
        db_lead = lead_repo.create(db, lead)
        return LeadResponseMessage(
            message="Lead created successfully",
            lead_id=db_lead.id
        )

lead_service = LeadService()