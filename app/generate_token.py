import jwt
import os
from dotenv import load_dotenv

load_dotenv()

secret = os.getenv("JWT_SECRET_KEY")
algo = os.getenv("JWT_ALGORITHM", "HS256")

payload = {"sub": "testuser", "user_id": 1}
token = jwt.encode(payload, secret, algorithm=algo)
print(token)