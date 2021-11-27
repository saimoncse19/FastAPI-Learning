from fastapi import FastAPI, Header, Depends, Query, status
from fastapi.exceptions import HTTPException
from typing import Tuple

app = FastAPI()


@app.get("/headers")
async def get_headers(user_agent: str = Header(None)):
    return {"user-agent": user_agent}


async def pagination(skip: int = Query(0, ge=0), limit: int = Query(10, ge=0)) -> Tuple[int, int]:
    capped_limit = min(limit, 100)
    return skip, capped_limit


@app.get("/items")
async def get_items(params: Tuple[int, int] = Depends(pagination)):
    skip, limit = params
    return {"skip": skip, "limit": limit}


# get an object or raise 404
dummy_db = {}


async def get_object_or_raise_404(post_id: int):
    try:
        return dummy_db[post_id]
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)


# class dependency

class Pagination:
    def __init__(self, max_limit: int = 100):
        self.max_limit = max_limit

    async def __call__(self, skip: int = Query(0, ge=0),
                       limit: int = Query(10, ge=0), *args, **kwargs) -> Tuple[int, int]:
        capped_limit = min(limit, self.max_limit)
        return skip, capped_limit

    async def skip_limit(self, skip: int = Query(0, ge=0), limit: int = Query(10, ge=0)) -> Tuple[int, int]:
        return skip, min(limit, self.max_limit)

    async def page_size(self, page: int = Query(1, ge=1), size: int = Query(10, ge=0)) -> Tuple[int, int]:
        return page, min(self.max_limit, size)


paginator = Pagination(max_limit=50)


@app.get("/students")
async def get_students(params: Tuple[int, int] = Depends(paginator.skip_limit)):
    skip, limit = params
    return {"skip": skip, "limit": limit}


@app.get("/teachers")
async def get_teachers(params: Tuple[int, int] = Depends(paginator.page_size)):
    page, size = params
    return {"page": page, "size": size}
