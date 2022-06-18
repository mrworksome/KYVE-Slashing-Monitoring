import datetime
from typing import List

import requests
from loguru import logger

from src.model_data import ListStaker, DbStaker
from src.db.base import db_clickhouse
from src.schemas import StakerSchema

pool = {
    "Moonbeam": 0,
    "Avalanche // C-Chain" : 1,
    "Stacks": 2,
    "Bitcoin": 3,
    "Solana": 4,
    "Zilliqa": 5,
    "Near": 6,
    "Celo": 7,
    "Evmos EVM": 8,
    "Cosmos Hub": 9,
    "Injective": 10,
    "Evmos Cosmos": 11,
    "Axelar": 12,
    "Aurora": 13,
    "Cronos": 14,
    "Terra": 15,
    "Umee": 16,
    "Polkadot": 17
}


def pools_info():
    """Requests all stakers in polls"""
    date = datetime.datetime.now().strftime("%d-%b-%Y %H:%M")
    for pool_name, pool_id in pool.items():
        validator_list = []
        data_stakers = fetch_pool_validator(pool_id)
        for staker in data_stakers.stakers:
            validator_db = DbStaker(
                staker=staker.staker,
                pool_id=staker.pool_id,
                account=staker.account,
                amount=staker.account,
                total_delegation=staker.total_delegation,
                commission=staker.commission,
                moniker=staker.moniker,
                website=staker.website,
                points=staker.points,
                date=date
            )
            validator_list.append(validator_db)
        db_clickhouse.insert([StakerSchema(**validator.dict()) for validator in validator_list])
        logger.info(f'{pool_name} all validators loaded')
        validator_list.clear()


def fetch_pool_validator(pool_id: int) -> ListStaker or List:
    """Request poll stakers or validator in pool"""
    KYVE_POOL_VALIDATORS_URL = 'https://api.korellia.kyve.network/kyve/registry/v1beta1/stakers_list/{}'
    try:
        list_stakers = requests.get(KYVE_POOL_VALIDATORS_URL.format(pool_id), timeout=5).json()
        stakers = ListStaker(**list_stakers)
    except Exception as e:
        logger.info("try one more chance...")
        logger.info(e)
        return []
    return stakers
