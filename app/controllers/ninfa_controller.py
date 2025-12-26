from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError, OperationalError
from app.models.ninfa_model import Ninfa
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

def get_all_ninfas_db(db: Session):
    ninfas = db.query(Ninfa).all()
    return ninfas

def get_nidadas(db: Session):
    result = db.query(Ninfa.nidada).distinct().all()
    
    return JSONResponse(content={"message": "¡Respuesta exitosa!","resultado": [{ "nidada": n[0]} for n in result]}, status_code=200)
    
def get_nidada_by_id(db: Session, id_nidada: str):
    ninfas = db.query(Ninfa).filter(Ninfa.nidada == id_nidada).order_by(Ninfa.id.asc()).all()
    
    # return ninfas
    return JSONResponse(content={"message": "¡Respuesta exitosa!","resultado": jsonable_encoder(ninfas)}, status_code=200)

def create_ninfa_list(db: Session):
    try:
        count = db.query(Ninfa).count()
        
        if count>0:
            return {"message": "La lista de ninfas ya esta cargada!"}
        
        ninfa_list = [{    "nidada": "1-2025",    "imagen": "https://res.cloudinary.com/dfmn1wvfh/image/upload/v1765512939/NinfaLutinaHembra150x150_waziwf.png",    "tipo": "Lutina",    "precio": "1,200",    "disponibilidad": "No disponible"},{    "nidada": "1-2025",    "imagen": "https://res.cloudinary.com/dfmn1wvfh/image/upload/v1765512940/NinfaPerladaHembra150x150_iswi7m.png",    "tipo": "Perlada",    "precio": "1,500",    "disponibilidad": "No disponible"},{    "nidada": "1-2025",    "imagen": "https://res.cloudinary.com/dfmn1wvfh/image/upload/v1765512941/Ancestral_Macho_150x150_tvplfe.png",    "tipo": "Ancestral",    "precio": "3,000",    "disponibilidad": "No disponible"},{    "nidada": "1-2025",    "imagen": "https://res.cloudinary.com/dfmn1wvfh/image/upload/v1765512941/Cara_blanca_hembra_150x150_zbmore.png",    "tipo": "Cara blanca",    "precio": "1,200",    "disponibilidad": "No disponible"},{    "nidada": "1-2025",    "imagen": "https://res.cloudinary.com/dfmn1wvfh/image/upload/v1765512941/Cara_pastel_Hembra_150x150_jpabwi.png",    "tipo": "Cara pastel",    "precio": "5,000",    "disponibilidad": "No disponible"},{    "nidada": "1-2025",    "imagen": "https://res.cloudinary.com/dfmn1wvfh/image/upload/v1765512940/Albina_hembra_150x150_h3vwa3.png",    "tipo": "Albina",    "precio": "6,500",    "disponibilidad": "No disponible"},{    "nidada": "1-2025",    "imagen": "https://res.cloudinary.com/dfmn1wvfh/image/upload/v1765512940/Manchada_hembra_150x150_ymoe3q.png",    "tipo": "Manchada",    "precio": "1,200",    "disponibilidad": "No disponible"},{    "nidada": "1-2025",    "imagen": "https://res.cloudinary.com/dfmn1wvfh/image/upload/v1765512940/Albinca_macho_150x150_epzv5o.png",    "tipo": "Albina",    "precio": "1,400",    "disponibilidad": "No disponible"},{    "nidada": "1-2025",    "imagen": "https://res.cloudinary.com/dfmn1wvfh/image/upload/v1765512939/Ninfa_Perlada_Macho_150x150_v9fxf4.png",    "tipo": "Perlada",    "precio": "13,500",    "disponibilidad": "No disponible"},{    "nidada": "1-2025",    "imagen": "https://res.cloudinary.com/dfmn1wvfh/image/upload/v1765512939/Ninfa_Perlada_Macho_150x150_v9fxf4.png",    "tipo": "Perlada",    "precio": "14,600",    "disponibilidad": "No disponible"},{    "nidada": "2-2025",    "imagen": "https://res.cloudinary.com/dfmn1wvfh/image/upload/v1765512940/Lutina_Macho_150x150_zu2ymj.png",    "tipo": "Lutina",    "precio": "2,410",    "disponibilidad": "No disponible"},{    "nidada": "2-2025",    "imagen": "https://res.cloudinary.com/dfmn1wvfh/image/upload/v1765512940/NinfaPerladaHembra150x150_iswi7m.png",    "tipo": "Perlada",    "precio": "6,974",    "disponibilidad": "No disponible"},{    "nidada": "2-2025",    "imagen": "https://res.cloudinary.com/dfmn1wvfh/image/upload/v1765512941/Ancestral_Macho_150x150_tvplfe.png",    "tipo": "Ancestral",    "precio": "4,670",    "disponibilidad": "No disponible"},{    "nidada": "2-2025",    "imagen": "https://res.cloudinary.com/dfmn1wvfh/image/upload/v1765512941/Cara_blanca_hembra_150x150_zbmore.png",    "tipo": "Cara blanca",    "precio": "8,745",    "disponibilidad": "No disponible"},{    "nidada": "2-2025",    "imagen": "https://res.cloudinary.com/dfmn1wvfh/image/upload/v1765512941/Cara_Blanca_Macho_150x150_r6qjxk.png",    "tipo": "Cara pastel",    "precio": "6,541",    "disponibilidad": "No disponible"},{    "nidada": "2-2025",    "imagen": "https://res.cloudinary.com/dfmn1wvfh/image/upload/v1765512940/Albina_hembra_150x150_h3vwa3.png",    "tipo": "Albina",    "precio": "3,145",    "disponibilidad": "No disponible"},{    "nidada": "2-2025",    "imagen": "https://res.cloudinary.com/dfmn1wvfh/image/upload/v1765512940/Manchada_macho_150x150_fnavqf.png",    "tipo": "Manchada",    "precio": "6,482",    "disponibilidad": "No disponible"},{    "nidada": "2-2025",    "imagen": "https://res.cloudinary.com/dfmn1wvfh/image/upload/v1765512940/Albinca_macho_150x150_epzv5o.png",    "tipo": "Albina",    "precio": "2,145",    "disponibilidad": "No disponible"},{    "nidada": "2-2025",    "imagen": "https://res.cloudinary.com/dfmn1wvfh/image/upload/v1765512939/Ninfa_Perlada_Macho_150x150_v9fxf4.png",    "tipo": "Perlada",    "precio": "3,652",    "disponibilidad": "No disponible"},{    "nidada": "3-2025",    "imagen": "https://res.cloudinary.com/dfmn1wvfh/image/upload/v1765512939/NinfaLutinaHembra150x150_waziwf.png",    "tipo": "Lutina",    "precio": "1,530",    "disponibilidad": "Disponible"},{    "nidada": "3-2025",    "imagen": "https://res.cloudinary.com/dfmn1wvfh/image/upload/v1765512940/Lutina_Macho_150x150_zu2ymj.png",    "tipo": "Lutina",    "precio": "6,941",    "disponibilidad": "Disponible"},{    "nidada": "3-2025",    "imagen": "https://res.cloudinary.com/dfmn1wvfh/image/upload/v1765512940/NinfaPerladaHembra150x150_iswi7m.png",    "tipo": "Perlada",    "precio": "3,485",    "disponibilidad": "No disponible"},{    "nidada": "3-2025",    "imagen": "https://res.cloudinary.com/dfmn1wvfh/image/upload/v1765512940/Ancestral_Hembra_150x150_zt875n.png",    "tipo": "Ancestral",    "precio": "2,684",    "disponibilidad": "Disponible"},{    "nidada": "3-2025",    "imagen": "https://res.cloudinary.com/dfmn1wvfh/image/upload/v1765512941/Cara_Blanca_Macho_150x150_r6qjxk.png",    "tipo": "Cara blanca",    "precio": "1,685",    "disponibilidad": "Disponible"},{    "nidada": "2-2025",    "imagen": "https://res.cloudinary.com/dfmn1wvfh/image/upload/v1765512941/Cara_pastel_Hembra_150x150_jpabwi.png",    "tipo": "Cara pastel",    "precio": "2,489",    "disponibilidad": "Disponible"},{    "nidada": "3-2025",    "imagen": "https://res.cloudinary.com/dfmn1wvfh/image/upload/v1765512940/Albinca_macho_150x150_epzv5o.png",    "tipo": "Albina",    "precio": "3,648",    "disponibilidad": "Disponible"},{    "nidada": "3-2025",    "imagen": "https://res.cloudinary.com/dfmn1wvfh/image/upload/v1765512940/Manchada_macho_150x150_fnavqf.png",    "tipo": "Manchada",    "precio": "6,894",    "disponibilidad": "Disponible"},{    "nidada": "3-2025",    "imagen": "https://res.cloudinary.com/dfmn1wvfh/image/upload/v1765512940/Albina_hembra_150x150_h3vwa3.png",    "tipo": "Albina",    "precio": "3,598",    "disponibilidad": "No disponible"},{    "nidada": "3-2025",    "imagen": "https://res.cloudinary.com/dfmn1wvfh/image/upload/v1765512939/Ninfa_Perlada_Macho_150x150_v9fxf4.png",    "tipo": "Perlada",    "precio": "3,456",    "disponibilidad": "Disponible"},{    "nidada": "3-2025",    "imagen": "https://res.cloudinary.com/dfmn1wvfh/image/upload/v1765512940/NinfaPerladaHembra150x150_iswi7m.png",    "tipo": "Perlada",    "precio": "1,354",    "disponibilidad": "No disponible"}];
        
        ninfas = [
            Ninfa(
                nidada=item["nidada"],
                tipo=item["tipo"],
                precio=item["precio"],
                disponibilidad=item["disponibilidad"],
                imagen=item["imagen"]
            )
            for item in ninfa_list
        ]

        db.add_all(ninfas)
        db.commit()
        return {"message": "Lista de ninfas agregada correctamente"}

    except (IntegrityError, OperationalError):
        db.rollback()
        raise Exception("Error al insertar la lista de ninfas en la BD")