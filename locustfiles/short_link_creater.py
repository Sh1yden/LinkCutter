""""""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))


import asyncio
import random
import time

from sqlalchemy import insert

from app.database.models import URLMap
from app.database.core import AsyncSessionLocal

from app.core import get_logger, setup_logging
from seed_db import generate_random_string, generate_realistic_path, REAL_DOMAINS

_lg = get_logger("LinkCreater")
setup_logging("DEBUG")


async def seed_database(total_records: int = 100_000, batch_size: int = 10_000):
    _lg.debug(f"🚀 Started seeding {total_records} realistic links...")
    start_time = time.time()

    saved_for_locust = []

    async with AsyncSessionLocal() as session:
        for i in range(0, total_records, batch_size):
            batch = []
            for _ in range(batch_size):
                short_code = generate_random_string(8)
                real_domain = random.choice(REAL_DOMAINS)
                path = generate_realistic_path()

                batch.append(
                    {"original_url": f"{real_domain}{path}", "short_url": short_code}
                )

                if random.random() < 0.1 and len(saved_for_locust) < 50000:
                    saved_for_locust.append(short_code)

            await session.execute(insert(URLMap).values(batch))
            await session.commit()
            _lg.debug(f"✅ Inserted {i + batch_size} / {total_records}...")

    with open("locustfiles/urls_for_locust.txt", "w") as f:
        f.write("\n".join(saved_for_locust))

    _lg.debug(f"🎉 Got it in {time.time() - start_time:.2f} sec.")
    _lg.debug(
        f"📄 File 'urls_for_locust.txt' created (in it {len(saved_for_locust)} links)."
    )


if __name__ == "__main__":
    asyncio.run(seed_database(total_records=200_000, batch_size=5_000))
