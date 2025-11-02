# app/main.py
from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from . import models, schemas, crud, auth
from .database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Leads API")


@app.post("/lead", response_model=schemas.LeadResponseMessage)
def create_lead_endpoint(
    lead: schemas.LeadCreate,
    db: Session = Depends(get_db),
    current_user: dict = Depends(auth.get_current_user)
):
    try:
        db_lead = crud.create_lead(db, lead)
        return {"message": "Lead created successfully", "lead_id": db_lead.id}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
