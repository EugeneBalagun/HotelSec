import jwt
from dotenv import load_dotenv
import os

load_dotenv()
secret = os.getenv("JWT_SECRET_KEY")
algo = os.getenv("JWT_ALGORITHM", "HS256")

payload = {"user_id": 1, "email": "test@example.com"}
token = jwt.encode(payload, secret, algorithm=algo)
print(token)
