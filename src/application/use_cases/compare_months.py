from datetime import datetime

from src.application.services.date_filter_service import (
    DateFilterService
)

from src.application.services.monthly_report_service import (
    MonthlyReportService
)

from src.application.services.monthly_comparison_service import (
    MonthlyComparisonService
)


class CompareMonthsUseCase:

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

        self.comparison_service = (
            MonthlyComparisonService()
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

        current_month = (
            self.date_filter.current_month(
                expenses
            )
        )

        last_month = (
            self.date_filter.last_month(
                expenses
            )
        )

        current_report = (
            self.report_service.generate(
                current_month
            )
        )

        previous_report = (
            self.report_service.generate(
                last_month
            )
        )

        return (
            self.comparison_service.compare(
                current_report,
                previous_report
            )
        )