from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.controllers.ninfa_controller import create_ninfa_list
from app.controllers.ninfa_controller import get_all_ninfas_db
from app.controllers.ninfa_controller import get_nidadas
from app.controllers.ninfa_controller import get_nidada_by_id


router = APIRouter(prefix="/ninfas", tags=["Ninfas"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
@router.post("/add-list")
def add_ninfa_list(db: Session = Depends(get_db)):
    return create_ninfa_list(db)

@router.get("/get-all-ninfas")
def get_list(db: Session = Depends(get_db)):
    return get_all_ninfas_db(db)

@router.get("/get-nidada", status_code=200)
def get_list_nidada(db: Session = Depends(get_db)):
    return get_nidadas(db)

@router.get("/get-one-nidada/{id_nidada}", status_code=200)
def get_nidada(id_nidada: str,db: Session = Depends(get_db)):
    return get_nidada_by_id(db, id_nidada)