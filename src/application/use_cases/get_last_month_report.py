from src.application.services.date_filter_service import (
    DateFilterService
)

from src.application.services.monthly_report_service import (
    MonthlyReportService
)


class GetLastMonthReportUseCase:

    def __init__(
        self,
        repository
    ):
        self.repository = repository

        self.date_filter = (
            DateFilterService()
        )

        self.report_service = (
            MonthlyReportService()
        )

    def execute(
        self,
        user_id: str
    ):

        expenses = (
            self.repository.get_by_user(
                user_id
            )
        )

        last_month_expenses = (
            self.date_filter.last_month(
                expenses
            )
        )

        return (
            self.report_service.generate(
                last_month_expenses
            )
        )