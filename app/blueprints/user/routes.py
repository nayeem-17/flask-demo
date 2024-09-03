from . import user
from .controller import UserController


@user.route("/", methods=["POST"])
def create_user():
    return UserController.create_user()


@user.route("/<string:user_id>", methods=["GET"])
def get_user(user_id):
    return UserController.get_user(user_id)


@user.route("/<string:user_id>", methods=["PUT"])
def update_user(user_id):
    return UserController.update_user(user_id)


@user.route("/<string:user_id>", methods=["DELETE"])
def delete_user(user_id):
    return UserController.delete_user(user_id)
