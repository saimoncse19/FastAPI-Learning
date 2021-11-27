from fastapi import HTTPException, Header, status, FastAPI, Depends
from typing import Optional


async def auth(token: Optional[str] = Header(None)) -> None:
    if not token or token != "dummy_token":
        raise HTTPException(status.HTTP_403_FORBIDDEN)


app = FastAPI()


@app.get("/protected", dependencies=[Depends(auth)])
async def protected():
    return {"message": "This is a protected route"}
