from src.application.services.monthly_report_service import (
    MonthlyReportService
)


class GetMonthlyReportUseCase:

    def __init__(
        self,
        repository
    ):
        self.repository = repository

        self.report_service = (
            MonthlyReportService()
        )

    def execute(
        self,
        user_id: str,
        year: int,
        month: int
    ):

        expenses = (
            self.repository.get_by_user(
                user_id
            )
        )

        filtered_expenses = [
            expense
            for expense in expenses
            if (
                expense["created_at"].year == year
                and
                expense["created_at"].month == month
            )
        ]

        return (
            self.report_service.generate(
                filtered_expenses
            )
        )