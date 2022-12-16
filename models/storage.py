from db import db


class StorageModel(db.Model):
    __tablename__ = "storage"

    id = db.Column(db.Integer, primary_key=True)
    namestorage = db.Column(db.String(50), unique=True, nullable=False)
    adress = db.Column(db.String(100), unique=False, nullable=False)
    products = db.relationship("ProductModel", back_populates="storage", lazy="dynamic")