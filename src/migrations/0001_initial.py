from infi.clickhouse_orm import migrations

from src.schemas import StakerSchema


operations = [migrations.CreateTable(StakerSchema)]
