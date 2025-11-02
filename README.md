# Leads API

Simple REST API built with FastAPI for creating leads with JWT authentication and PostgreSQL.

---

## ⚡ Features

- `POST /lead` — create a new lead  
  - JSON payload: `{ "name", "email", "phone" }`  
  - Validates required fields and email format  
  - Requires JWT Bearer token
  - Returns JSON: `{ "message": "Lead created successfully", "lead_id": <id> }`

---

## 🛠️ Installation & Running

1. Clone the repository:
```bash
git clone <your-repo-url>
cd HotelSec
```
Create a virtual environment and install dependencies:

```bash

python -m venv .venv
source .venv/bin/activate  # Linux/macOS
.venv\Scripts\activate     # Windows
pip install -r requirements.txt
```
Create .env file (example):

```bash
DATABASE_URL=postgresql://user:password@localhost:5432/leads_db
JWT_SECRET_KEY=supersecretkey
JWT_ALGORITHM=HS256
```
Run the service:

```bash
uvicorn app.main:app --reload
```
🧪 Testing
```bash

python -m pytest tests/test_post_lead.py
```
Checks:

HTTP 200 OK

Lead successfully created

Correct JSON response with message and lead_id


⚠️ Security
No secrets in code; all keys stored in .env

JWT Bearer token required for authentication

SQLAlchemy ORM (no raw SQL)

Proper exception handling with status codes

