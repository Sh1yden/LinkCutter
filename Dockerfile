FROM ghcr.io/astral-sh/uv:python3.12-slim

WORKDIR /app

# Копируем файлы зависимостей
COPY pyproject.toml uv.lock ./

# Устанавливаем зависимости в системный Python (без venv)
# --system устанавливает в системный Python образа
# --no-install-project не собирает твой пакет
RUN uv sync --frozen --no-dev --no-install-project --system

# Копируем исходный код
COPY . .

# Опционально: создаем пользователя для безопасности
RUN useradd -m appuser && chown -R appuser:appuser /app
USER appuser

EXPOSE 8000

# Запускаем uvicorn напрямую (он уже в PATH)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]