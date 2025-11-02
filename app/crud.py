from sqlalchemy.orm import Session
from . import models, schemas

def create_lead(db: Session, lead: schemas.LeadCreate) -> models.Lead:
    db_lead = models.Lead(name=lead.name, email=lead.email, phone=lead.phone)
    db.add(db_lead)
    db.commit()
    db.refresh(db_lead)
    return db_lead
