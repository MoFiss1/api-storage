from db import db

class ProductModel(db.Model):
    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key=True)
    mark = db.Column(db.String(20), unique=False, nullable=False)
    model = db.Column(db.String(20), unique=False, nullable=False)
    description = db.Column(db.String(100), unique=False, nullable=False)
    upc = db.Column(db.String(10), unique=False, nullable=False)
    condition = db.Column(db.String(10), unique=False, nullable=False)
    weight = db.Column(db.Integer, unique=False, nullable=False)
    count = db.Column(db.Integer, unique=False, nullable=False)

    storage_id = db.Column(
        db.Integer, db.ForeignKey("storage.id"), unique=False, nullable=False
    )
    storage = db.relationship("StorageModel", back_populates="products")