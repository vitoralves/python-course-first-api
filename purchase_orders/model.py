from db import db


class PurchaseOrderModel(db.Model):
    __tablename__ = 'purchase_order'

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(500), nullable=False)

    def __init__(self, description):
        self.description = description
