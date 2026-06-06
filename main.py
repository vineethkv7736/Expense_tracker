from fastapi import FastAPI

from src.presentation.api.expense_routes import (
    router as expense_router
)

from src.presentation.api.summary_routes import (
    router as summary_router
)

from src.presentation.api.analytics_routes import (
    router as analytics_router
)

from src.presentation.api.health_routes import (
    router as health_router
)

app = FastAPI()
app.include_router(expense_router)
app.include_router(summary_router)
app.include_router(analytics_router)
app.include_router(health_router)