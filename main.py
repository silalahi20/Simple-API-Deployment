# from fastapi import FastAPI, Depends
# from routers import secure, public
# from auth import get_user

# app = FastAPI()

# app.include_router(
#     public.router,
#     prefix="/api/v1/public"
# )
# app.include_router(
#     secure.router,
#     prefix="/api/v1/secure",
#     dependencies=[Depends(get_user)]
# )
# @app.get("/")
# async def root():
#     return {"message": "This is Simple API Deployment for ParMusic with Authentication by Josia 1822075"}
from fastapi import FastAPI, Depends
from routers import secure, public, auth_routes
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
app.include_router(
    auth_routes.router,
    prefix="/api/v1/auth"
)

@app.get("/")
async def root():
    return {"message": "This is Simple API Deployment for ParMusic with Authentication by Josia 1822075"}
