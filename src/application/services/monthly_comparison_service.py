class MonthlyComparisonService:

    def compare(
        self,
        current_report,
        previous_report
    ):

        current_total = (
            current_report["total_spent"]
        )

        previous_total = (
            previous_report["total_spent"]
        )

        difference = (
            current_total -
            previous_total
        )

        if previous_total == 0:

            percentage_change = None

        else:

            percentage_change = (
                difference /
                previous_total
            ) * 100

        return {
            "current_total": current_total,
            "previous_total": previous_total,
            "difference": difference,
            "percentage_change": percentage_change,
            "current_transactions": (
                current_report[
                    "transaction_count"
                ]
            ),
            "previous_transactions": (
                previous_report[
                    "transaction_count"
                ]
            )
        }