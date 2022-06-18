from infi.clickhouse_orm import Database

from src.core.config import settings

db_clickhouse = Database(settings.CLICKHOUSE_NAME, db_url=settings.CLICKHOUSE_URL, timeout=300)

db_clickhouse.migrate('src.migrations')
