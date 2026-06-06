import os

print("BOT FILE LOADED")

from src.infrastructure.postgres.database import (
    engine
)

from src.infrastructure.postgres.models import (
    Base
)

from src.container import (
    add_expense_use_case,
    get_summary_use_case,
    get_recent_expenses_use_case,
    analyze_expenses_use_case,
    agent_chat_use_case
)

from dotenv import load_dotenv

from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)

load_dotenv()

BOT_TOKEN = os.getenv(
    "TELEGRAM_BOT_TOKEN"
)


async def start(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):
    await update.message.reply_text(
        "Expense Tracker Bot Started 🚀"
    )


async def add_expense(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    message = update.message.text

    user_id = str(
        update.effective_user.id
    )

    try:
        expense = (
            add_expense_use_case.execute(
                user_id=user_id,
                message=message
            )
        )

        await update.message.reply_text(
            f"""
✅ Expense Added

Item: {expense.item}
Amount: ₹{expense.amount}
Category: {expense.category}
"""
        )

    except Exception as e:

        print(e)

        await update.message.reply_text(
            "❌ Failed to add expense"
        )

async def summary(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    user_id = str(
        update.effective_user.id
    )

    try:

        result = (
            get_summary_use_case.execute(
                user_id
            )
        )

        text = (
            f"📊 Expense Summary\n\n"
            f"Total Spent: ₹{result['total_spent']}\n"
            f"Expenses: {result['expense_count']}\n\n"
        )

        for category, amount in (
            result["categories"].items()
        ):
            text += (
                f"{category}: ₹{amount}\n"
            )

        await update.message.reply_text(
            text
        )

    except Exception as e:

        print(e)

        await update.message.reply_text(
            "❌ Failed to get summary"
        )
async def recent(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    user_id = str(
        update.effective_user.id
    )

    try:

        expenses = (
            get_recent_expenses_use_case.execute(
                user_id=user_id,
                limit=10
            )
        )

        if not expenses:

            await update.message.reply_text(
                "No expenses found."
            )

            return

        text = (
            "🕒 Recent Expenses\n\n"
        )

        for expense in expenses:

            text += (
                f"{expense['item']} "
                f"- ₹{expense['amount']} "
                f"({expense['category']})\n"
            )

        await update.message.reply_text(
            text
        )

    except Exception as e:

        print(e)

        await update.message.reply_text(
            "❌ Failed to get expenses"
        )
async def ask(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    user_id = str(
        update.effective_user.id
    )

    question = " ".join(
        context.args
    )

    if not question:

        await update.message.reply_text(
            "Usage:\n/ask Analyze my expenses"
        )

        return

    try:

        result = (
            agent_chat_use_case.execute(
                user_id=user_id,
                question=question
            )
        )

        await update.message.reply_text(
            str(result)
        )

    except Exception as e:

        print(e)

        await update.message.reply_text(
            "Analysis failed."
        )

def main():

    app = Application.builder() \
        .token(BOT_TOKEN) \
        .build()

    app.add_handler(
        CommandHandler(
            "start",
            start
        )
    )

    app.add_handler(
        CommandHandler(
            "summary",
            summary
        )
    )
    app.add_handler(
        CommandHandler(
            "recent",
            recent
        )
    )
    app.add_handler(
        CommandHandler(
            "ask",
            ask
        )
    )
    app.add_handler(
        MessageHandler(
            filters.TEXT,
            add_expense
        )
    )
    print(
        "Telegram Bot Running..."
    )

    app.run_polling()


if __name__ == "__main__":
    Base.metadata.create_all(
        bind=engine
    )
    main()