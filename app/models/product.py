from sqlalchemy import Column, Integer, String, Float, Boolean
from app.db.base import Base

class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False, index=True)
    description = Column(String(255), nullable=True)
    price = Column(Float, nullable=False)
    in_stock = Column(Boolean, default=True)
