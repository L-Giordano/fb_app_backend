from abc import ABC, abstractmethod

from src.user.domain.user_model import User


class IUserRepository(ABC):
    @abstractmethod
    def get(self, user_id: int) -> User:
        pass

    @abstractmethod
    def get_all(self) -> list[User]:
        pass

    @abstractmethod
    def save(self, user: User) -> User:
        pass
