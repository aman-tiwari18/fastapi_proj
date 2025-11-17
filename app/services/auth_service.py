from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate
from app.utils.security import hash_password, verify_password, create_access_token

class AuthService:
    def __init__(self, db: Session):
        self.db = db

    def get_user_by_email(self, email: str):
        return self.db.query(User).filter(User.email == email).first()

    def create_user(self, user_in: UserCreate):
        user = User(
            email=user_in.email,
            full_name=user_in.full_name,
            hashed_password=user_in.password
        )
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def authenticate(self, email: str, password: str):
        user = self.get_user_by_email(email)
        if not user: 
            return None
        if not verify_password(password, user.hashed_password):
            return None
        return user

    def create_token_for_user(self, user):
        return create_access_token(subject=user.id)
