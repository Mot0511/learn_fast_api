import uuid

from fastapi_users import schemas
from sqlalchemy import Optional, EmailStr

class UserRead(schemas.BaseUser[int]):
    id: int
    username: str
    role_id: int
    email: EmailStr
    is_active: bool = True
    is_superuser: bool = False
    is_verified: bool = False

    class Config:
            orm_mode = True

class UserCreate(schemas.BaseUserCreate):
    username: str
    email: EmailStr
    password: str
    role_id: int
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False
    is_verified: Optional[bool] = False
