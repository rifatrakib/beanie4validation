import asyncio

from app.config.manager import pool_database_clients


def prepare_database():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(pool_database_clients())
    loop.close()
