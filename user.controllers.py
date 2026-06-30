from fastapi import APIRouter, Depens, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.user import UserCreate, UserUptade, UserOut
from app.services.user import user_service

router = APIRouter(prefix="/users", tags=["users"])
@router.get("/", response_model=list[UserOut])
def get_all_users(db: Session = Depens(get_db)):
    return user_service.get_all_users(db)

@router.get("/{user_id}", response_model=UserOut)
def get_user_by_id(user_id: int, db: Session = Depens(get_db)):
    user = user_service.get_user_by_id(db, user_id)
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user

@router.post("/", response_model=UserOut, status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreate, db: Session 0 = Depends(get_db)):
    return user_service.create_user(db, user)

@router.put("/{user_id}", response_model=UserOut)
def uptade_user(user_id: int, user : UserUptade, db: Session = Depens(get_db)):
    uptaded_user = user_service.uptade_user(db, user_id, user)
    if not uptade_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= "User not found:")
    return uptaded_user

@router.delete("/{user_id}", response_model=UserOut)
def delete_user(user_id: int, db: Session = Depens(get_db)):
    deleted_user = user_service.delete_user(db, user_id)
    if not deleted_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return deleted_user

