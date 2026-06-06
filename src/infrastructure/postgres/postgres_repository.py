from src.infrastructure.postgres.database import (
    SessionLocal
)

from src.infrastructure.postgres.models import (
    ExpenseModel
)


class PostgresExpenseRepository:

    def save(
        self,
        expense
    ):

        db = SessionLocal()

        try:

            db.add(
                ExpenseModel(
                    id=expense.id,
                    user_id=expense.user_id,
                    item=expense.item,
                    amount=expense.amount,
                    category=expense.category,
                    created_at=expense.created_at
                )
            )

            db.commit()

        finally:

            db.close()

    def get_all(self):

        db = SessionLocal()

        try:

            expenses = (
                db.query(
                    ExpenseModel
                ).all()
            )

            return [
                self._to_dict(e)
                for e in expenses
            ]

        finally:

            db.close()

    def get_by_user(
        self,
        user_id: str
    ):

        db = SessionLocal()

        try:

            expenses = (
                db.query(
                    ExpenseModel
                )
                .filter(
                    ExpenseModel.user_id == user_id
                )
                .all()
            )

            return [
                self._to_dict(e)
                for e in expenses
            ]

        finally:

            db.close()

    def get_recent_by_user(
        self,
        user_id: str,
        limit: int = 10
    ):

        db = SessionLocal()

        try:

            expenses = (
                db.query(
                    ExpenseModel
                )
                .filter(
                    ExpenseModel.user_id == user_id
                )
                .order_by(
                    ExpenseModel.created_at.desc()
                )
                .limit(limit)
                .all()
            )

            return [
                self._to_dict(e)
                for e in expenses
            ]

        finally:

            db.close()

    def _to_dict(
        self,
        expense
    ):

        return {
            "id": expense.id,
            "user_id": expense.user_id,
            "item": expense.item,
            "amount": expense.amount,
            "category": expense.category,
            "created_at": expense.created_at
        }