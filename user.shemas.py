from pydantic import BaseModel, EmailStr
from typing import Optional
# базовые поля
class ItemBase(BaseModel):
    name: str 
    description: Optional[str] = None
    price: float

    class Cofing:
        from_attributes = True

# Схема для создания (ID еще нет)
class ItemCreate(ItemBase):
    pass

# Схема для обновления (все поля опциональны)
class ItemUpdate(ItemBase):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
# Схема, которая используется для ответа (ID уже есть)
class ItemResponse(ItemBase):
    id: int
    name: str
    email: EmailStr
    age: int | None = None
    
    class Config:
        from_attributes = True #для превращения ORM-объекта в схему
