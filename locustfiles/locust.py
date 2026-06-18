import random
from locust import HttpUser, task, between, events
import string
import os

TEST_URLS = []


@events.test_start.add_listener
def on_test_start(environment, **kwargs):
    """Выполняется один раз перед началом теста. Читаем файл в память."""
    global TEST_URLS
    if os.path.exists("locustfiles/urls_for_locust.txt"):
        with open("locustfiles/urls_for_locust.txt", "r") as f:
            TEST_URLS = f.read().splitlines()
        print(f"🔥 Locust загрузил {len(TEST_URLS)} ссылок для обстрела!")
    else:
        print(
            "⚠️ Файл locustfiles/urls_for_locust.txt не найден! Рандомные клики не сработают."
        )


class LinkCutterUser(HttpUser):
    wait_time = between(0.1, 0.5)

    @task(4)  # Вес 4: Это действие будет выполняться в 4 раза чаще
    def redirect_to_url(self):
        """Эмуляция перехода по короткой ссылке (GET)"""
        if not TEST_URLS:
            return

        # Берем случайную короткую ссылку из памяти
        short_code = random.choice(TEST_URLS)

        with self.client.get(
            f"/linkcutter/api/v1/{short_code}",
            allow_redirects=False,
            catch_response=True,
        ) as response:
            if response.status_code in [301, 302, 307]:
                response.success()
            else:
                response.failure(f"Expected redirect, got {response.status_code}")

    @task(1)  # Вес 1: Это действие будет выполняться реже
    def create_new_url(self):
        """Эмуляция создания новой ссылки (POST)"""
        domains = ["https://habr.com/ru/news/", "https://github.com/pulls/"]
        path = "".join(random.choices(string.ascii_letters, k=8))
        real_url = f"{random.choice(domains)}{path}"

        self.client.post("/linkcutter/api/v1/shorten", json={"original_url": real_url})
