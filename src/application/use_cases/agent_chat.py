from datetime import datetime
from src.application.services.intent_service import (
    IntentService
)
from src.application.services.report_formatter import (
    ReportFormatter
)

from src.application.services.category_analysis_service import (
    CategoryAnalysisService
)

class AgentChatUseCase:

    def __init__(
        self,
        ai_service,
        get_monthly_report_use_case,
        get_last_month_report_use_case,
        get_summary_use_case,
        get_recent_expenses_use_case,
        compare_months_use_case
    ):

        self.ai_service = ai_service

        self.intent_service = (
            IntentService()
        )

        self.report_formatter = (
            ReportFormatter()
        )

        self.get_monthly_report = (
            get_monthly_report_use_case
        )

        self.get_last_month_report = (
            get_last_month_report_use_case
        )

        self.get_summary = (
            get_summary_use_case
        )

        self.get_recent = (
            get_recent_expenses_use_case
        )

        self.compare_months = (
            compare_months_use_case
        )

        self.category_analysis = (
            CategoryAnalysisService()
        )

    def execute(
        self,
        user_id: str,
        question: str
    ):

        intent = (
            self.intent_service.detect(
                question
            )
        )
        if intent == "last_month_report":

            report = (
                self.get_last_month_report.execute(
                    user_id
                )
            )

            return (
                self.report_formatter.monthly_report(
                    report
                )
            )

        if intent == "current_month_report":

            now = datetime.now()

            report = (
                self.get_monthly_report.execute(
                    user_id,
                    now.year,
                    now.month
                )
            )

            return (
                self.report_formatter.monthly_report(
                    report
                )
            )

        if intent == "summary":

            return (
                self.get_summary.execute(
                    user_id
                )
            )

        if intent == "recent_expenses":

            return (
                self.get_recent.execute(
                    user_id
                )
            )
        if intent == "monthly_comparison":

            comparison = (
                self.compare_months.execute(
                    user_id
                )
            )

            return (
                self.report_formatter
                .comparison_report(
                    comparison
                )
            )
        
        if intent == "top_spending_category":

            now = datetime.now()

            report = (
                self.get_monthly_report.execute(
                    user_id,
                    now.year,
                    now.month
                )
            )

            analysis = (
                self.category_analysis.analyze(
                    report
                )
            )

            return (
                self.report_formatter
                .top_spending_category(
                    analysis
                )
            )

        return self.ai_service.analyze(
            analysis={},
            expenses=[],
            question=question
        )