from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def get_testroute():
    return "Public Route for ParMusic"

@router.get("/google-login")
async def google_login():
    # Nanti implementasi Google Login
    return {"message": "Login with Google initiated"}
