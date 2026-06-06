from abc import ABC, abstractmethod

class ExpenseRepository(ABC):

    @abstractmethod
    def save(self, expense):
        pass

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def get_by_user(self, user_id: str):
        pass

    @abstractmethod
    def get_recent_by_user(
        self,
        user_id: str,
        limit: int = 10
    ):
        pass