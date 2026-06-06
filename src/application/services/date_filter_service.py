from datetime import datetime


class DateFilterService:

    def current_month(
        self,
        expenses
    ):

        now = datetime.now()

        return [
            expense
            for expense in expenses
            if (
                expense["created_at"].year == now.year
                and
                expense["created_at"].month == now.month
            )
        ]

    def last_month(
        self,
        expenses
    ):

        now = datetime.now()

        year = now.year
        month = now.month - 1

        if month == 0:
            month = 12
            year -= 1

        return [
            expense
            for expense in expenses
            if (
                expense["created_at"].year == year
                and
                expense["created_at"].month == month
            )
        ]

    def specific_month(
        self,
        expenses,
        year: int,
        month: int
    ):

        return [
            expense
            for expense in expenses
            if (
                expense["created_at"].year == year
                and
                expense["created_at"].month == month
            )
        ]
