from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.db.database import Base, engine
from app.views.user_view import router as user_router
from app.views.ninfa_view import router as ninfa_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="FastAPI MVC + MySQL", version="1.0.0")

# Lista de orígenes permitidos
origins = [
    "http://localhost:3000",   # React local
    "http://127.0.0.1:3000",
    "http://localhost:5173",   # Vite
    "http://127.0.0.1:5173",
    "http://127.0.0.1:54807",
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,          
    allow_credentials=True,
    allow_methods=["*"],            
    allow_headers=["*"],            
)

app.include_router(user_router, prefix="/api/v1")
app.include_router(ninfa_router, prefix="/api/v1")
