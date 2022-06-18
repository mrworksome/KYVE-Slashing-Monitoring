from infi.clickhouse_orm.engines import MergeTree
from infi.clickhouse_orm.fields import StringField
from infi.clickhouse_orm.models import Model


class StakerSchema(Model):
    staker = StringField()
    pool_id = StringField()
    account = StringField()
    amount = StringField()
    total_delegation = StringField()
    commission = StringField()
    moniker = StringField()
    website = StringField()
    points = StringField()
    date = StringField()

    engine = MergeTree(partition_key=(pool_id,),
                       order_by=('account', 'date',)
                       )

    @classmethod
    def table_name(cls):
        return "stakers"
