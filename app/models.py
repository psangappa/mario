from datetime import datetime
from app import db, ma


class ApiData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    n = db.Column(db.Integer)
    grid = db.Column(db.Text)
    url = db.Column(db.Text)
    remote_address = db.Column(db.String(30))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'{self.n}*{self.n} Matrix'


class ApiDataSchema(ma.Schema):
    class Meta:
        fields = ('id', 'n', 'grid', 'url', 'remote_address', 'timestamp')
