from app.config.manager import pool_database_clients


async def prepare_database():
    await pool_database_clients()
