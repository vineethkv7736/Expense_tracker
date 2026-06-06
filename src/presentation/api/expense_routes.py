from fastapi import APIRouter
from pydantic import BaseModel

from src.container import (
    add_expense_use_case,
    get_summary_use_case,
    get_recent_expenses_use_case,
    get_expenses_use_case
)

router = APIRouter()


class ExpenseRequest(BaseModel):
    user_id: str
    message: str


@router.post("/expense")
def add_expense(request: ExpenseRequest):

    return add_expense_use_case.execute(
        request.user_id,
        request.message
    )


@router.get("/expenses")
def get_expenses():

    return get_expenses_use_case.execute()


@router.get("/summary/{user_id}")
def get_summary(user_id: str):

    return get_summary_use_case.execute(
        user_id
    )


@router.get("/recent-expenses/{user_id}")
def recent_expenses(user_id: str):

    return get_recent_expenses_use_case.execute(
        user_id
    )