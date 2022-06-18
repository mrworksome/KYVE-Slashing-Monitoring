import datetime
from enum import Enum
from typing import List

from pydantic import BaseModel


class InfoStaker(BaseModel):
    staker: str
    pool_id: str
    account: str
    amount: str
    total_delegation: str
    commission: str
    moniker: str
    website: str
    points: str


class DbStaker(InfoStaker):
    date: str


class ListStaker(BaseModel):
    stakers: List[InfoStaker]

