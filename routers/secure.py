# from fastapi import APIRouter, Depends
# from auth import get_user

# router = APIRouter()

# @router.get("/")
# async def get_testroute(user: dict = Depends(get_user)):
#     return user
from fastapi import APIRouter, Depends
from auth import get_user, get_current_user

router = APIRouter()

@router.get("/")
async def get_testroute(user: dict = Depends(get_user)):
    return user

@router.get("/userid")
async def get_user_id(user: dict = Depends(get_user)):
    return {"user_id": user["name"]}

