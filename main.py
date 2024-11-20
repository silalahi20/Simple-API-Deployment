# # main.py
# import uvicorn
# from fastapi import FastAPI, Depends, HTTPException, Security
# from fastapi.security.api_key import APIKeyHeader, APIKey
# import os
# from dotenv import load_dotenv

# load_dotenv()


# app = FastAPI()

# # Tentukan header untuk API key
# API_KEY_NAME = "X-API-Key"

# # Ambil API key dari variabel lingkungan
# API_KEY = os.getenv("MY_SECRET_API_KEY")
# api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)

# # Fungsi untuk memverifikasi API key
# async def get_api_key(api_key_header: str = Security(api_key_header)):
#     if api_key_header == API_KEY:
#         return api_key_header
#     else:
#         raise HTTPException(
#             status_code=403, detail="Could not validate API key"
#         )

# @app.get("/")
# async def root(api_key: APIKey = Depends(get_api_key)):
#     return {"message": "Hello from FastAPI!. This is Simple API Deployment by Josia 18222075"}

# if __name__ == "__main__":
#     uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

from fastapi import FastAPI, Depends
from routers import secure, public
from auth import get_user

app = FastAPI()

app.include_router(
    public.router,
    prefix="/api/v1/public"
)
app.include_router(
    secure.router,
    prefix="/api/v1/secure",
    dependencies=[Depends(get_user)]
)
@app.get("/")
async def root():
    return {"message": "This is Simple API Deployment for ParMusic with Authentication by Josia 1822075"}
