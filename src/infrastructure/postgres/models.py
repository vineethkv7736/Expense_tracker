from sqlalchemy.orm import (
    declarative_base
)

from sqlalchemy import (
    Column,
    String,
    Float,
    DateTime
)

Base = declarative_base()


class ExpenseModel(Base):

    __tablename__ = "expenses"

    id = Column(
        String,
        primary_key=True
    )

    user_id = Column(
        String,
        nullable=False
    )

    item = Column(
        String,
        nullable=False
    )

    amount = Column(
        Float,
        nullable=False
    )

    category = Column(
        String,
        nullable=False
    )

    created_at = Column(
        DateTime,
        nullable=False
    )