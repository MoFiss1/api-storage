from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError

from db import db
from models import ProductModel
from schemas import ProductSchema, ProductUpdateSchema,ProductExistence

blp = Blueprint("products", __name__, description="Operations on products")


@blp.route("/product/<string:product_id>")
class Product(MethodView):
    @blp.response(200, ProductSchema)
    def get(self, product_id):
        product = ProductModel.query.get_or_404(product_id)
        return product

    def delete(self, product_id):
        product = ProductModel.query.get_or_404(product_id)
        db.session.delete(product)
        db.session.commit()
        return {"message": "product deleted."}

    @blp.arguments(ProductUpdateSchema)
    @blp.response(200, ProductSchema)
    def put(self, product_data, product_id):
        product = ProductModel.query.get_or_404(product_id)

        if product:
            product.mark = product_data["mark"]
            product.model = product_data["model"]
            product.description = product_data["description"]
            product.upc = product_data["upc"]
            product.condition = product_data["condition"]
            product.weight = product_data["weight"]
            product.count = product_data["count"]
        else:
            product = ProductModel(**product_data)

        db.session.add(product)
        db.session.commit()

        return product


@blp.route("/product")
class ProductList(MethodView):
    @blp.response(200, ProductSchema(many=True))
    def get(self):
        return ProductModel.query.all()

    @blp.arguments(ProductSchema)
    @blp.response(201, ProductSchema)
    def post(self, product_data):
        product = ProductModel(**product_data)
        try:
            db.session.add(product)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="An error occurred while inserting the product.")
        return product

@blp.route("/product/<string:product_id>/existence")
class ProductExist(MethodView):
    @blp.response(200, ProductExistence(many=True))
    def get(self, product_id):
        product = ProductModel.query.get_or_404(product_id)
        productFinal = ProductModel.query.filter_by(model=product.model)
        return productFinal