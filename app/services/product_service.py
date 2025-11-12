from sqlalchemy.orm import Session
from app.models.product import Product
from app.schemas.product import ProductCreate

class ProductService:
    def __init__(self, db: Session):
        self.db = db

    def list_products(self):
        return self.db.query(Product).all()

    def create_product(self, product_in: ProductCreate):
        p = Product(**product_in.dict())
        self.db.add(p)
        self.db.commit()
        self.db.refresh(p)
        return p

    def get_product(self, product_id: int):
        return self.db.query(Product).filter(Product.id == product_id).first()
