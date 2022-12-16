from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from db import db
from models import StorageModel
from flask.views import MethodView
from flask_smorest import abort,Blueprint
from schemas import StorageSchema

blp=Blueprint("storage",__name__,description="Operations on storage")

@blp.route("/storage/<int:storage_id>")
class Storage(MethodView):
    @blp.response(200, StorageSchema)
    def get(self, storage_id):
        storage = StorageModel.query.get_or_404(storage_id)
        return storage

@blp.route("/storage")
class StorageList(MethodView):
    @blp.response(200, StorageSchema(many=True))
    def get(self):
        return StorageModel.query.all()

    @blp.arguments(StorageSchema)
    @blp.response(201, StorageSchema)
    def post(self, storage_data):
        storage = StorageModel(**storage_data)
        try:
            db.session.add(storage)
            db.session.commit()
        except IntegrityError:
            abort(
                400,
                message="A storage with that name already exists.",
            )
        except SQLAlchemyError:
            abort(500, message="An error occurred creating the storage.")

        return storage