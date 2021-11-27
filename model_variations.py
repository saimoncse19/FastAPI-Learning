from pydantic import BaseModel, EmailStr


class Author(BaseModel):
    name: str
    email: EmailStr


class PostBase(BaseModel):
    title: str
    content: str
    author: Author
    
    def summary(self) -> str:
        return f"{self.content[:150]}"


class PostCreate(PostBase):
    pass


class PostPublic(PostBase):
    id: int


class PostDB(PostBase):
    id: int
    view_count: int


