import asyncio

from app.config.manager import pool_database_clients, populate_collections


def prepare_database():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(pool_database_clients())
    loop.close()


def populate_database():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(populate_collections())
    loop.close()
