from pydantic import BaseModel
from typing import Optional

# Schema for creating a car
class CarCreate(BaseModel):
    name: str
    location: str
    price: float
    generation: int

# Schema for filtering cars
class CarFilter(BaseModel):
    name: Optional[str] = None
    location: Optional[str] = None
    min_price: Optional[float] = None
    max_price: Optional[float] = None
    min_generation: Optional[int] = None
    max_generation: Optional[int] = None

# Schema for response
class CarResponse(CarCreate):
    id: int

    class Config:
        orm_mode = True
