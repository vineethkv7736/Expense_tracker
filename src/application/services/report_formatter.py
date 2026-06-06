

class ReportFormatter:

    CATEGORY_EMOJIS = {
        "Food": "🍔",
        "Transport": "🚗",
        "Utilities": "💡",
        "Shopping": "🛍️",
        "Healthcare": "🏥",
        "Education": "📚",
        "Entertainment": "🎬",
        "Investment": "📈",
        "Bills": "🧾",
        "Rent": "🏠",
        "Insurance": "🛡️",
        "Travel": "✈️",
        "Salary": "💰",
        "Business": "🏢",
        "Other": "📦"
    }

    def monthly_report(self, report: dict) -> str:

        if report["transaction_count"] == 0:
            return """📊 Monthly Expense Report

 No transactions recorded for this month.""".strip()

        lines = []

        lines.append("📊 Monthly Expense Report")
        lines.append("")
        lines.append("💰 Total Spent")
        lines.append(f"₹{report['total_spent']:,.2f}")
        lines.append("")
        lines.append("📂 Category Breakdown")
        lines.append("")

        for category, items in report["categories"].items():

            emoji = self.CATEGORY_EMOJIS.get(
                category,
                "📦"
            )

            lines.append(
                f"{emoji} {category}"
            )

            for item in items:
                lines.append(
                    f"• {item['item']} — ₹{item['amount']:,.2f}"
                )

            lines.append("")

        lines.append("📈 Summary")

        lines.append(
            f"• Transactions: {report['transaction_count']}"
        )

        if report.get("top_category"):
            lines.append(
                f"• Top Category: {report['top_category']['name']} (₹{report['top_category']['amount']:,.2f})"
            )

        if report.get("largest_expense"):
            lines.append(
                f"• Largest Expense: {report['largest_expense']['item']} (₹{report['largest_expense']['amount']:,.2f})"
            )

        return "\n".join(lines)
    def comparison_report(
        self,
        comparison
    ):

        lines = []

        lines.append(
            "📊 Monthly Comparison"
        )

        lines.append("")

        lines.append(
            "📅 Current Month"
        )

        lines.append(
            f"₹{comparison['current_total']:,.2f}"
        )

        lines.append(
            f"{comparison['current_transactions']} transactions"
        )

        lines.append("")

        lines.append(
            "📅 Previous Month"
        )

        lines.append(
            f"₹{comparison['previous_total']:,.2f}"
        )

        lines.append(
            f"{comparison['previous_transactions']} transactions"
        )

        lines.append("")

        lines.append(
            "📈 Difference"
        )

        sign = "+" if (
            comparison["difference"] >= 0
        ) else ""

        lines.append(
            f"{sign}₹{comparison['difference']:,.2f}"
        )

        if (
            comparison[
                "percentage_change"
            ] is not None
        ):
            lines.append(
                f"{comparison['percentage_change']:.2f}%"
            )

        return "\n".join(lines)
    
    def top_spending_category(
        self,
        analysis
    ):

        if analysis is None:

            return (
                "No expenses found."
            )

        return f"""
    📊 Spending Analysis

    🏆 Highest Spending Category

    {analysis['top_category']}

    💰 Amount Spent

    ₹{analysis['amount']:,.2f}
    """.strip()