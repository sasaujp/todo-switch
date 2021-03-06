from .db import db
from sqlalchemy_utils.types.uuid import UUIDType
from uuid import uuid4


class Task(db.Model):
    __tablename__ = 'task'
    id = db.Column(UUIDType(binary=False), primary_key=True, default=uuid4)
    name = db.Column(db.String(512))

    def to_dict(self):
        return {
            'id': self.id.hex,
            'name': self.name
        }
