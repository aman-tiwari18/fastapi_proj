from fastapi import FastAPI
from app.routers import auth, products

# Import SQLAlchemy Base + engine
from app.db.base import Base, engine

# VERY IMPORTANT — Import all models so SQLAlchemy knows them
from app.models import user, product  # adjust names as per your files

app = FastAPI(title="Demo FastAPI App")

# Create DB tables on startup
@app.on_event("startup")
def on_startup():
    print("Creating tables if not exist...")
    Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
app.include_router(products.router)
