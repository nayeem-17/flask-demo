# Example ORM model
from app.utils.database import db
from flask_login import UserMixin
from sqlalchemy.dialects.postgresql import UUID
import uuid


class User(db.Model, UserMixin):
    __tablename__ = "user"

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    profile_pic = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f"<User id={self.id} name={self.name} email={self.email}>"

    def get_id(self):
        return str(self.id)
