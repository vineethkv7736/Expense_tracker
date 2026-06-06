from fastapi import APIRouter

from src.container import (
    get_monthly_report_use_case
)

router = APIRouter()


@router.get("/report/{user_id}")
def monthly_report(
    user_id: str
):
    return (
        get_monthly_report_use_case.execute(
            user_id
        )
    )