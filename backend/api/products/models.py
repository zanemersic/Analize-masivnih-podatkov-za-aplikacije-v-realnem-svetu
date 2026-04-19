from typing import Optional
from pydantic import BaseModel, Field

class NutritionPer100g(BaseModel):
    calories_kcal: Optional[float] = None
    protein_g: Optional[float] = None
    carbohydrates_g: Optional[float] = None
    sugars_g: Optional[float] = None
    fat_g: Optional[float] = None
    saturated_fat_g: Optional[float] = None
    fiber_g: Optional[float] = None
    salt_g: Optional[float] = None

class ProductSource(BaseModel):
    name: Optional[str] = None
    url: Optional[str] = None

class RawProductIn(BaseModel):
    name: str
    brand: Optional[str] = None
    barcode: Optional[str] = None
    quantity: Optional[str] = None
    source: Optional[ProductSource] = None
    nutrition_per_100g: NutritionPer100g

class ProductOut(BaseModel):
    id: Optional[str] = None
    name: str
    brand: Optional[str] = None
    barcode: Optional[str] = None
    quantity: Optional[str] = None
    nutrition_per_100g: NutritionPer100g
    source: Optional[ProductSource] = None
