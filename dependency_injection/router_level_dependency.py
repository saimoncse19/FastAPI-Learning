from .dummy_protected_routes import auth, app
from fastapi import APIRouter, Depends

commission_router = APIRouter(dependencies=[Depends(auth)])


@commission_router.get("/auto-commission/{name}")
async def auto_commission(name: str):
    return {"auto-commission": name}


@commission_router.get("/royalty/{amount}")
async def royalty_commission(amount: int):
    return {"royalty": amount}


app.include_router(commission_router, prefix="/commission")
