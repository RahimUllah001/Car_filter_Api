from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import select
from typing import List, Optional
from .database import get_db
from .models import Car
from .schemas import CarCreate, CarResponse

app = FastAPI()

# Endpoint 1: Store car data
@app.post("/cars/", response_model=CarResponse)
def create_car(car: CarCreate, db: Session = Depends(get_db)):
    new_car = Car(**car.dict())
    db.add(new_car)
    
    db.commit()
    db.refresh(new_car)
    return new_car

# Endpoint 2: Filter car data
@app.get("/cars/", response_model=List[CarResponse])
def filter_cars(
    name: Optional[str] = None,
    location: Optional[str] = None,
    min_price: Optional[float] = None,
    max_price: Optional[float] = None,
    min_generation: Optional[int] = None,
    max_generation: Optional[int] = None,
    db: Session = Depends(get_db),
):
    query = db.query(Car)
    if name:
        query = query.filter(Car.name.ilike(f"%{name}%"))
    if location:
        query = query.filter(Car.location.ilike(f"%{location}%"))
    if min_price is not None:
        query = query.filter(Car.price >= min_price)
    if max_price is not None:
        query = query.filter(Car.price <= max_price)
    if min_generation is not None:
        query = query.filter(Car.generation >= min_generation)
    if max_generation is not None:
        query = query.filter(Car.generation <= max_generation)

    result = query.all()
    return result
