from src.application.dto.expense_dto import ExpenseDTO
from src.domain.entities.expense import Expense

class AddExpenseUseCase:

    def __init__(
        self,
        ai_service,
        repository=None
    ):
        self.ai_service = ai_service
        self.repository = repository

    def execute(self, user_id: str, message: str):
        data = self.ai_service.categorize(message)

        print("DATA:")
        print(repr(data))
        
        expense_dto = ExpenseDTO(**data,user_id=user_id)
        expense = Expense(
            id=expense_dto.id,
            user_id=expense_dto.user_id,
            item=expense_dto.item,
            amount=expense_dto.amount,
            category=expense_dto.category,
            created_at=expense_dto.created_at
            )
        if self.repository:
            self.repository.save(expense)

        return expense_dto