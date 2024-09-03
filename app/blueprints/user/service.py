from .model import User
from .dto import UserCreate, UserUpdate, UserResponse
from app.utils.database import db
from app.utils.logger import logger  # This should now work correctly
from sqlalchemy.exc import IntegrityError
from pydantic import ValidationError
import uuid


class UserNotFoundError(Exception):
    def __init__(self, user_id: str, operation: str = "retrieve"):
        self.user_id = user_id
        self.operation = operation
        self.message = (
            f"User with id '{user_id}' not found during {operation} operation"
        )
        super().__init__(self.message)

    def __str__(self):
        return self.message


class UserService:
    @staticmethod
    def create_user(user_data: UserCreate) -> UserResponse:
        try:
            new_user = User(
                name=user_data.name,
                email=user_data.email,
                profile_pic=user_data.profile_pic,
            )
            db.session.add(new_user)
            db.session.commit()
            logger.info(f"Created new user: {new_user}")
            return UserResponse.model_validate(new_user)
        except IntegrityError as e:
            logger.error(f"Integrity error creating user: {str(e)}")
            db.session.rollback()
            raise ValueError("User with this email already exists")
        except Exception as e:
            logger.error(f"Error creating user: {str(e)}")
            db.session.rollback()
            raise

    @staticmethod
    def get_user(user_id: str) -> UserResponse:
        try:
            user = User.query.get(uuid.UUID(user_id))
            if user:
                logger.info(f"Retrieved user: {user}")
                return UserResponse.model_validate(user)
            logger.info(f"User not found with id: {user_id}")
            raise UserNotFoundError(user_id)
        except Exception as e:
            logger.error(f"Error retrieving user: {str(e)}")
            raise

    @staticmethod
    def update_user(user_id: str, user_data: UserUpdate) -> UserResponse:
        try:
            user = User.query.get(uuid.UUID(user_id))
            if user:
                update_data = user_data.model_dump(exclude_unset=True)
                for key, value in update_data.items():
                    setattr(user, key, value)
                db.session.commit()
                logger.info(f"Updated user: {user}")
                return UserResponse.model_validate(user)
            logger.info(f"User not found for update with id: {user_id}")
            raise UserNotFoundError(user_id, "update")
        except IntegrityError as e:
            logger.error(f"Integrity error updating user: {str(e)}")
            db.session.rollback()
            raise ValueError("User with this email already exists")
        except Exception as e:
            logger.error(f"Error updating user: {str(e)}")
            db.session.rollback()
            raise

    @staticmethod
    def delete_user(user_id: str) -> bool:
        try:
            user = User.query.get(user_id)
            if user:
                db.session.delete(user)
                db.session.commit()
                logger.info(f"Deleted user: {user}")
                return True
            logger.info(f"User not found for deletion with id: {user_id}")
            return False
        except Exception as e:
            logger.error(f"Error deleting user: {str(e)}")
            db.session.rollback()
            raise
