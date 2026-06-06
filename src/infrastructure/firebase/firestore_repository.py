from src.domain.repositories.expense_repository import ExpenseRepository
from src.infrastructure.firebase.firebase_client import db
from dataclasses import asdict

class FirestoreExpenseRepository(ExpenseRepository):

    def __init__(self):
        self.db = db

    def save(self, expense):

        self.db.collection(
            "expenses"
        ).add(
            asdict(expense)
        )

    def get_all(self):

        docs = (
            self.db.collection(
                "expenses"
            ).stream()
        )

        return [
            doc.to_dict()
            for doc in docs
        ]

    def get_by_user(
        self,
        user_id: str
    ):

        docs = (
            self.db.collection(
                "expenses"
            )
            .where(
                "user_id",
                "==",
                user_id
            )
            .stream()
        )

        return [
            doc.to_dict()
            for doc in docs
        ]
    def get_recent_by_user(
        self,
        user_id: str,
        limit: int = 10
    ):

        docs = (
            self.db.collection("expenses")
            .where(
                "user_id",
                "==",
                user_id
            )
            .order_by(
                "created_at",
                direction="DESCENDING"
            )
            .limit(limit)
            .stream()
        )

        return [
            doc.to_dict()
            for doc in docs
        ]