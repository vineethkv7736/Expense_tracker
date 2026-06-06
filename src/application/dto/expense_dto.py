from uuid import uuid4
from pydantic import BaseModel,Field
from datetime import datetime, UTC

class ExpenseDTO(BaseModel):
    id: str = Field(
        default_factory=lambda: str(uuid4())
    )
    user_id: str = "default_user"
    item: str
    amount: float
    category: str
    created_at: datetime = Field(
        default_factory=lambda: datetime.now(UTC)
    )