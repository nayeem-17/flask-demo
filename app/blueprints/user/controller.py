from flask import jsonify, request
from .service import UserService
from .dto import UserCreate, UserUpdate
from app.utils.logger import logger
from pydantic import ValidationError


class UserController:
    @staticmethod
    def create_user():
        try:
            user_data = UserCreate(**request.json)
            logger.info(f"the user data is {user_data}")
            new_user = UserService.create_user(user_data)
            return jsonify(new_user.dict()), 201
        except ValidationError as e:
            logger.error(f"Validation error in create_user: {str(e)}")
            return jsonify({"error": str(e)}), 400
        except ValueError as e:
            logger.error(f"Value error in create_user: {str(e)}")
            return jsonify({"error": str(e)}), 400
        except Exception as e:
            logger.error(f"Controller error in create_user: {str(e)}")
            return jsonify({"error": "Failed to create user"}), 500

    @staticmethod
    def get_user(user_id):
        try:
            user = UserService.get_user(user_id)
            if user:
                return jsonify(user.dict()), 200
            return jsonify({"message": "User not found"}), 404
        except Exception as e:
            logger.error(f"Controller error in get_user: {str(e)}")
            return jsonify({"error": "Failed to retrieve user"}), 500

    @staticmethod
    def update_user(user_id):
        try:
            user_data = UserUpdate(**request.json)
            updated_user = UserService.update_user(user_id, user_data)
            if updated_user:
                return jsonify(updated_user.dict()), 200
            return jsonify({"message": "User not found"}), 404
        except ValidationError as e:
            logger.error(f"Validation error in update_user: {str(e)}")
            return jsonify({"error": str(e)}), 400
        except ValueError as e:
            logger.error(f"Value error in update_user: {str(e)}")
            return jsonify({"error": str(e)}), 400
        except Exception as e:
            logger.error(f"Controller error in update_user: {str(e)}")
            return jsonify({"error": "Failed to update user"}), 500

    @staticmethod
    def delete_user(user_id):
        try:
            if UserService.delete_user(user_id):
                return jsonify({"message": "User deleted successfully"}), 200
            return jsonify({"message": "User not found"}), 404
        except Exception as e:
            logger.error(f"Controller error in delete_user: {str(e)}")
            return jsonify({"error": "Failed to delete user"}), 500
