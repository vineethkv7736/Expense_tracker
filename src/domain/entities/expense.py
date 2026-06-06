from dataclasses import dataclass
from datetime import datetime

@dataclass
class Expense:
    id: str
    user_id: str
    item: str
    amount: float
    category: str
    created_at: datetime