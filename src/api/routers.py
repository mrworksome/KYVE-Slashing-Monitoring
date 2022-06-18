from fastapi import APIRouter
from fastapi_utils.tasks import repeat_every
from loguru import logger

from src.request_manager import pools_info

router = APIRouter()


@router.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app!"}


@router.on_event("startup")
@repeat_every(seconds=60 * 60, logger=logger, wait_first=True)
def cron_job_fetch_pool_info():
    pools_info()

