from pydantic import BaseModel


class CategoryCreate(BaseModel):
    name: str
    slug: str
    image: str | None = None


class CategoryResponse(BaseModel):
    id: int
    name: str
    slug: str
    image: str | None = None