from sqlalchemy.orm import Session
from ..models.lead import Lead
from ..schemas.lead import LeadCreate

class LeadRepository:
    def create(self, db: Session, lead: LeadCreate) -> Lead:
        db_lead = Lead(name=lead.name, email=lead.email, phone=lead.phone)
        db.add(db_lead)
        db.commit()
        db.refresh(db_lead)
        return db_lead

lead_repo = LeadRepository()