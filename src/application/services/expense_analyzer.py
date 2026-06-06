from collections import defaultdict


class ExpenseAnalyzer:

    def analyze(self, expenses):

        total_spent = 0

        expense_count = len(expenses)

        categories = defaultdict(float)

        largest_expense = None

        for expense in expenses:

            amount = expense["amount"]

            total_spent += amount

            categories[
                expense["category"]
            ] += amount

            if (
                largest_expense is None
                or amount >
                largest_expense["amount"]
            ):
                largest_expense = expense

        average_expense = (
            total_spent / expense_count
            if expense_count > 0
            else 0
        )

        return {
            "currency": "INR",
            "total_spent": total_spent,
            "expense_count": expense_count,
            "average_expense": average_expense,
            "largest_expense": largest_expense,
            "categories": dict(categories)
        }