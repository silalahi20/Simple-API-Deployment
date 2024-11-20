from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def get_testroute():
    return "Public Route for ParMusic"
