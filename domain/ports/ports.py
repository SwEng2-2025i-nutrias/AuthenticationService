from abc import ABC, abstractmethod
from ..entities.user import User

# Input port for the domain layer of the application.
class AuthInputPort(ABC):
    @abstractmethod
    def register_user(self, id:str, email:str, password_hash:str, name:str, role:str, created_at:str, last_login_at:str|None=None) -> User:
        pass

    @abstractmethod
    def login_user(self, email:str, password_hash:str) -> User:
        pass

# Output port for the domain layer of the application.
class AuthOutputPort(ABC):
    @abstractmethod
    def save_user(self, user: User) -> None:
        """
        Saves the user to the database or any other storage.
        """
        pass

    @abstractmethod
    def get_user_by_email(self, email: str) -> User | None:
        """
        Retrieves a user by their email.
        Returns None if the user does not exist.
        """
        pass

    @abstractmethod
    def update_user(self, user: User) -> None:
        """
        Updates the user in the database or any other storage.
        """
        pass 