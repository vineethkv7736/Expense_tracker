from collections import defaultdict


class MonthlyReportService:

    def generate(
        self,
        expenses
    ):

        total_spent = 0

        largest_expense = None

        category_totals = defaultdict(float)

        category_items = defaultdict(list)

        for expense in expenses:

            amount = expense["amount"]

            total_spent += amount

            category_totals[
                expense["category"]
            ] += amount

            category_items[
                expense["category"]
            ].append(
                {
                    "item": expense["item"],
                    "amount": amount
                }
            )

            if (
                largest_expense is None
                or
                amount >
                largest_expense["amount"]
            ):
                largest_expense = expense

        top_category = None

        if category_totals:

            category_name = max(
                category_totals,
                key=category_totals.get
            )

            top_category = {
                "name": category_name,
                "amount": category_totals[
                    category_name
                ]
            }

        return {
            "total_spent": total_spent,
            "transaction_count": len(
                expenses
            ),
            "largest_expense": largest_expense,
            "top_category": top_category,
            "categories": dict(
                category_items
            )
        }