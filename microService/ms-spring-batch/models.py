from db import db
from datetime import datetime

db = db()

class Debt(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.String(50), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    due_date = db.Column(db.Date, nullable=False)
    contact_method = db.Column(db.String(50), nullable=False)
