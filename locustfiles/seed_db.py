import random
import string
import uuid

# Огромная база реалистичных доменов
REAL_DOMAINS = [
    # Технологии и Разработка
    "https://github.com/torvalds/linux/commit/",
    "https://stackoverflow.com/questions/",
    "https://habr.com/ru/articles/",
    "https://dev.to/search?q=",
    "https://hub.docker.com/r/library/",
    "https://pypi.org/project/",
    "https://news.ycombinator.com/item?id=",
    # Соцсети, Медиа и Блоги
    "https://vk.com/wall-",
    "https://t.me/s/",
    "https://vc.ru/tech/",
    "https://dtf.ru/games/",
    "https://pikabu.ru/story/",
    "https://x.com/elonmusk/status/",
    "https://www.reddit.com/r/programming/comments/",
    # Видео, Музыка и Стриминг
    "https://www.youtube.com/watch?v=",
    "https://www.twitch.tv/directory/game/",
    "https://www.kinopoisk.ru/film/",
    "https://open.spotify.com/track/",
    "https://music.yandex.ru/album/",
    # Маркетплейсы и Магазины
    "https://www.avito.ru/rossiya/tovary_dlya_kompyutera/",
    "https://www.ozon.ru/product/",
    "https://www.wildberries.ru/catalog/",
    "https://market.yandex.ru/product--",
    "https://www.amazon.com/dp/",
    # Образование и Энциклопедии
    "https://ru.wikipedia.org/wiki/",
    "https://stepik.org/course/",
    "https://www.coursera.org/learn/",
]


def generate_random_string(length=6):
    """Генерация короткого кода для самой сокращенной ссылки"""
    chars = string.ascii_letters + string.digits
    return "".join(random.choice(chars) for _ in range(length))


def generate_realistic_path():
    """Генерация реалистичного 'хвоста' для оригинального URL"""
    templates = [
        lambda: str(
            random.randint(100000, 9999999)
        ),  # Числовой ID (Хабр, Кинопоиск, Авито)
        lambda: "".join(
            random.choices(string.ascii_letters + string.digits, k=11)
        ),  # YouTube-подобный ID
        lambda: f"awesome-post-about-python-{random.randint(1,9999)}",  # ЧПУ (Slug) как на VC или DTF
        lambda: str(uuid.uuid4()),  # Классический UUID
        lambda: "".join(
            random.choices(string.ascii_lowercase + string.digits, k=40)
        ),  # Git Commit Hash
    ]
    return random.choice(templates)()
