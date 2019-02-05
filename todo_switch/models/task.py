from .db import db


class Task(db.Model):
    __tablename__ = 'task'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(512))

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name
        }
