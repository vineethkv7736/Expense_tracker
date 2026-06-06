class GetRecentExpensesUseCase:

    def __init__(
        self,
        repository
    ):
        self.repository = repository

    def execute(
        self,
        user_id: str,
        limit: int = 10
    ):

        return self.repository.get_recent_by_user(
            user_id,
            limit
        )