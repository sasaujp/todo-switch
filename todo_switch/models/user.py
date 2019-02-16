from .db import db
from sqlalchemy_utils.types import UUIDType, EmailType
from uuid import uuid4


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(UUIDType(binary=False), primary_key=True, default=uuid4)
    email = db.Column(EmailType, unique=True, nullable=False)
    password = db.Column(db.String(512), nullable=False)
    name = db.Column(db.String(512))

    def to_dict(self):
        return {
            'id': self.id.hex,
            'name': self.name
        }
