from fastapi import APIRouter
from pydantic import BaseModel

from src.container import (
    analyze_expenses_use_case
)

router = APIRouter()


class AnalysisRequest(BaseModel):
    user_id: str
    question: str


@router.post("/analyze")
def analyze(
    request: AnalysisRequest
):

    return {
        "result":
        analyze_expenses_use_case.execute(
            request.user_id,
            request.question
        )
    }