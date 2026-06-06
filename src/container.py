from src.infrastructure.firebase.firestore_repository import (
    FirestoreExpenseRepository
)

from src.infrastructure.ollama.ollama_service import (
    OllamaService
)

from src.application.use_cases.add_expense import (
    AddExpenseUseCase
)

from src.application.use_cases.get_summary import (
    GetSummaryUseCase
)

from src.application.use_cases.get_recent_expenses import (
    GetRecentExpensesUseCase
)

from src.application.use_cases.analyze_expenses import (
    AnalyzeExpensesUseCase
)
from src.application.use_cases.get_expenses import (
    GetExpensesUseCase
)
from src.application.use_cases.get_monthly_report import (
    GetMonthlyReportUseCase
)

repo = FirestoreExpenseRepository()

ollama = OllamaService()


add_expense_use_case = AddExpenseUseCase(
    ai_service=ollama,
    repository=repo
)

get_summary_use_case = GetSummaryUseCase(
    repository=repo
)

get_recent_expenses_use_case = (
    GetRecentExpensesUseCase(
        repository=repo
    )
)

analyze_expenses_use_case = (
    AnalyzeExpensesUseCase(
        repository=repo,
        ai_service=ollama
    )
)

get_expenses_use_case = GetExpensesUseCase(
    repository=repo
)

get_monthly_report_use_case = (
    GetMonthlyReportUseCase(
        repository=repo
    )
)