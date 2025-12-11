from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.db.database import SessionLocal
from app.schemas.user_schema import UserCreate, UserUpdate, UserResponse
from app.controllers import user_controller

router = APIRouter(prefix="/users", tags=["Users"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/create", status_code=status.HTTP_201_CREATED)
def create_user(user_in: UserCreate, db: Session = Depends(get_db)):
    return user_controller.create_user(db, user_in)


@router.get("/get-all", response_model=list[UserResponse])
def list_users(db: Session = Depends(get_db)):
    users = user_controller.get_all_users(db)
    return users


@router.get("/get-one/{user_email}", response_model=UserResponse)
def get_user(user_email: str, db: Session = Depends(get_db)):
    user = user_controller.get_user_by_email(db, user_email)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user


@router.put("/update/{user_email}", response_model=UserResponse)
def update_user(user_email: str, user_in: UserUpdate, db: Session = Depends(get_db)):
    user = user_controller.update_user(db, user_email, user_in)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user


@router.delete("/delete/{user_email}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_email: str, db: Session = Depends(get_db)):
    deleted = user_controller.delete_user(db, user_email)
    if not deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return None