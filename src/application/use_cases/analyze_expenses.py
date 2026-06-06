from src.application.services.expense_analyzer import ExpenseAnalyzer

class AnalyzeExpensesUseCase:

    def __init__(
        self,
        repository,
        ai_service
    ):
        self.repository = repository
        self.ai_service = ai_service

        self.analyzer = (
            ExpenseAnalyzer()
        )

    def execute(
        self,
        user_id: str,
        question: str
    ):

        expenses = (
            self.repository.get_by_user(
                user_id
            )
        )

        analysis = (
            self.analyzer.analyze(
                expenses
            )
        )

        return self.ai_service.analyze(
            analysis=analysis,
            expenses=expenses,
            question=question
        )