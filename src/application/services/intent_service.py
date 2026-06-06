class IntentService:

    def detect(
        self,
        question: str
    ):

        question = question.lower().strip()

        if any(
            phrase in question
            for phrase in [
                "compare",
                "comparison"
            ]
        ):
            return "monthly_comparison"

        if any(
            phrase in question
            for phrase in [
                "last month",
                "previous month",
                "past month"
            ]
        ):
            return "last_month_report"

        if any(
            phrase in question
            for phrase in [
                "this month",
                "current month"
            ]
        ):
            return "current_month_report"

        if any(
            phrase in question
            for phrase in [
                "recent",
                "latest expenses",
                "recent expenses",
                "last expenses"
            ]
        ):
            return "recent_expenses"

        if any(
            phrase in question
            for phrase in [
                "summary",
                "overview",
                "spending summary"
            ]
        ):
            return "summary"
        
        if any(
            phrase in question
            for phrase in [
                "spending the most",
                "highest spending",
                "most money",
                "top category"
            ]
        ):
            return "top_spending_category"
        
        return "general_analysis"