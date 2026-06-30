from app.models.user import User as UserModel
from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate, UserUptade

class UserService:
    def get_all_users(db: Session):
        return db.query(UserModel).all()
    def get_user_by_id(db: Session, user_id: int):
        return db.query(UserModel).filter(UserModel.id == user_id).first()
        
    def create_user(db: Session, user: UserCreate):
            db_user = UserModel(**user.dict())
            db.add(db_user)
            db.commit()
            db.refresh(db_user)
            return db_user

    def uptade_user(db: Session, user_id: int, user: UserUptade):
        db_user = db.query(UserModel).filter(UserModel.id == user_id).first()
        if db_user:
            for key, value in user.dict(exclude_unset=True).items():
                setattr(db_user, key, value)
                db.commit()
                db.refresh(db_user)
                return db_user

    def delete_user(db: Session, user_id: int):
        db_user = db.query(UserModel).filter(UserModel.id == user_id).first()
        if db_user:
            db.delete(db_user)
            db.commit()
            return db_user