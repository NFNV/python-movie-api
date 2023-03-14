from pydantic import BaseModel, Field
from typing import Optional

class Movie(BaseModel):
    id: Optional[int] = None
    title: str = Field(..., min_length=3, max_length=50)
    overview: str = Field(..., min_length=3, max_length=150)
    year: int = Field(..., le=2023)
    rating: float = Field(..., ge=1, le=10)
    category: str = Field(..., min_length=3, max_length=15)

    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "title": "My movie",
                "overview": "My description",
                "year": 2023,
                "rating": 7.0,
                "category": "action"
            }
        }