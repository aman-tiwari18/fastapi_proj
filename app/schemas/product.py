from pydantic import BaseModel

class ProductCreate(BaseModel):
    name: str
    description: str | None = None
    price: float
    in_stock: bool = True

class ProductRead(BaseModel):
    id: int
    name: str
    description: str | None
    price: float
    in_stock: bool

    class Config:
        orm_mode = True
