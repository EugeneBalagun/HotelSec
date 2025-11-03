from fastapi import FastAPI
from .database import engine
from .models.lead import Lead
from .routers import lead


Lead.metadata.create_all(bind=engine)

app = FastAPI(title="Leads API")

app.include_router(lead.router)