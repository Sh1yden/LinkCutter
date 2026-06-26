# Changelog

Все значимые изменения в проекте будут документироваться в этом файле.

Формат основан на [Keep a Changelog](https://keepachangelog.com/ru/1.0.0/),
и этот проект придерживается [Semantic Versioning](https://semver.org/lang/ru/).

## [Released]

### Планируется

- [x] Выход в релиз v1.0.0.

[README (Чеклист заданий)](README.md#-чеклист-задания--roadmap--планируется)

## [1.0.0] 2026-06-26

### Добавлено

- Добавлена ручка для иконки проекта: `/favicon.ico`.
- Добавлена ручка для древа ручек) проекта: `/routes`.
- Добавлена кастомная ручка для страницы документации: `/docs`.
- Новая собственная иконка проекта.

### Изменено

- Структура древа ручек проекта изменена.
  - Изменена структура shotener и short_url.
- Динамическая версия проекта, теперь везде.
- Обновлён `README.md`.
- Обновлён `CHANGELOG.md`.

## [0.2.1] - 2026-06-25

### Изменено

- Доработан `README.md`: уточнения и исправления в документации.

## [0.2.0] - 2026-06-18

### Добавлено

- `CHANGELOG.md` — шаблон файла изменений проекта.
- `requirements.txt` — список зависимостей для запуска без `uv` внутри Docker.
- `Dockerfile` и `docker-compose.yml` — полноценная контейнеризация приложения с PostgreSQL.
- `locustfiles/locust.py` — сценарии нагрузочного тестирования (`Locust`).
- `locustfiles/seed_db.py` — скрипт генерации тестовых данных в БД.
- `locustfiles/short_link_creater.py` — утилита для массового создания коротких ссылок.
- `locustfiles/urls_for_locust.txt` — список URL для нагрузочных тестов.
- `locustfiles/README.md` — документация по нагрузочному тестированию.

### Изменено

- Папка `alembic/` переименована и перенесена в `app/database/migrations/`.
- `README.md` — добавлено описание структуры проекта, инструкции по запуску,
  чеклист задания и раздел про нагрузочное тестирование.
- Обновлена конфигурация `pyproject.toml`.
- `.gitignore` и `.dockerignore` — скрыт лишний контент.
- `.python-version` — зафиксирована версия интерпретатора.

## [0.1.1] - 2026-06-11

### Добавлено

- `README.md` — добавлено описание проекта, технологического стека и инструкция
  по запуску.

### Удалено

- `CHANGELOG.md` — удалён черновой файл (будет восстановлен в `v0.2.0`).

## [0.1.0] - 2026-06-11

### Добавлено

- Основная бизнес-логика сервиса сокращения URL (`app/services/url_service.py`).
- Алгоритм кодирования Base62 (`app/services/shortener.py`) для генерации
  коротких идентификаторов.
- Эндпоинты API v1 (`app/api/endpoints/v1/short_urls_handles.py`):
  создание короткой ссылки, редирект по короткому коду,
  поддержка кастомных (человекочитаемых) алиасов.
- ORM-модель `URLMap` (`app/database/models/models.py`) с полями
  `original_url`, `short_url`, `created_at`.
- Миграция БД через Alembic (`f9b11fc2a63e_initial_migration`).
- Подключение к PostgreSQL через `asyncpg` + `SQLAlchemy` async
  (`app/database/core/database.py`).
- Pydantic-схемы для запросов и ответов API (`app/schemas/url_schema.py`).
- Обновлён `docker-compose.yml`: добавлен сервис `postgres:16-alpine`
  с healthcheck.

### Изменено

- `app/core/config.py` — расширены настройки подключения к PostgreSQL.
- Рефакторинг схем: `app/api/schemas/` → `app/schemas/`.

## [0.0.1] - 2026-06-09

### Добавлено

- Инициализация структуры проекта на `FastAPI` + `uv` + `hatchling`.
- Скелет приложения: `app/main.py`, `app/core/`, `app/api/`, `app/database/`,
  `app/services/`, `app/utils/`, `app/admin/`.
- Базовый роутер и эндпоинт-заглушка (`app/api/endpoints/default.py`).
- Настройка логирования (`app/core/logger.py`, `app/core/logger_config.py`).
- `pyproject.toml` с динамической версией через `hatch-vcs`.
- Базовый `Dockerfile` и `docker-compose.yml`.
- `test_project_version.py` — тест на корректность версии пакета.
- `tests/conftest.py` — базовая конфигурация pytest.
- `.python-version`, `.gitignore`, `.dockerignore`.

## [0.0.0] - 2026-04-20

### Добавлено

- Инициализация репозитория.
- `LICENSE` (MIT).
- `README.md` — заготовка.

[Realesed]: https://github.com/Sh1yden/LinkCutter/compare/v1.0.0...HEAD
[1.0.0]: https://github.com/Sh1yden/LinkCutter/compare/v0.2.1...v1.0.0
[0.2.1]: https://github.com/Sh1yden/LinkCutter/compare/v0.2.0...v0.2.1
[0.2.0]: https://github.com/Sh1yden/LinkCutter/compare/v0.1.1...v0.2.0
[0.1.1]: https://github.com/Sh1yden/LinkCutter/compare/v0.1.0...v0.1.1
[0.1.0]: https://github.com/Sh1yden/LinkCutter/compare/v0.0.1...v0.1.0
[0.0.1]: https://github.com/Sh1yden/LinkCutter/compare/v0.0.0...v0.0.1
[0.0.0]: https://github.com/Sh1yden/LinkCutter/releases/tag/v0.0.0
