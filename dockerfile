FROM python:3.13-slim

WORKDIR /app

RUN pip install uv

COPY pyproject.toml .
COPY uv.lock* .

RUN uv sync

COPY . .

CMD ["uv", "run", "python", "-m", "src.infrastructure.telegram.bot"]