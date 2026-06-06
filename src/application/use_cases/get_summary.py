from collections import defaultdict

class GetSummaryUseCase:

    def __init__(self, repository):
        self.repository = repository

    def execute(self, user_id: str):

        expenses = self.repository.get_by_user(
            user_id
        )

        total_spent = 0
        expense_count = len(expenses)

        categories = defaultdict(float)

        for expense in expenses:

            amount = expense["amount"]

            total_spent += amount

            categories[
                expense["category"]
            ] += amount

        return {
            "total_spent": total_spent,
            "expense_count": expense_count,
            "categories": dict(categories)
        }