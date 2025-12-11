from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError, OperationalError
from app.models.user_model import User
from app.schemas.user_schema import UserCreate, UserUpdate
from app.exceptions.custom_exceptions import (UserAlreadyExistsException, GenericDBError)
from fastapi.responses import JSONResponse

def get_all_users(db: Session) -> list[User]:
    return db.query(User).all()

def get_user_by_email(db: Session, email: str) -> User | None:
    return db.query(User).filter(User.email == email).first()

def create_user(db: Session, user_in: UserCreate) -> User:
    try:
        existing = db.query(User).filter(User.email == user_in.email).first()
        if existing:
            raise UserAlreadyExistsException(user_in.email)
        
        user = User(
            name=user_in.name,
            email=user_in.email,
            message=user_in.message,
        )
        
        db.add(user)
        db.commit()
        db.refresh(user)
        
        return JSONResponse(content={"message": "¡Respuesta exitosa!"}, status_code=201)
    except (IntegrityError, OperationalError):
        # Excepciones para conexion a bd y escritura
        db.rollback()
        message = "An integrity or value error occurred."
        
        return user_in
        # raise GenericDBError(message)

def update_user(db: Session, user_email: str, user_in: UserUpdate) -> User | None:
    user = get_user_by_email(db, user_email)
    if not user:
        return None

    if user_in.name is not None:
        user.name = user_in.name
    if user_in.email is not None:
        user.email = user_in.email
    if user_in.message is not None:
        user.message = user_in.message

    db.commit()
    db.refresh(user)
    return user

def delete_user(db: Session, user_email: str) -> bool:
    user = get_user_by_email(db, user_email)
    if not user:
        return False

    db.delete(user)
    db.commit()
    return True
