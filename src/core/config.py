import os
from typing import Dict, List, Union
from loguru import logger
import yaml
from pydantic import BaseSettings, AnyHttpUrl, validator


config_file = os.path.join(os.path.dirname(__file__), "../../app_settings.yaml")

with open(config_file, "r") as f:
    try:
        configs = yaml.safe_load(f)
    except yaml.YAMLError as exc:
        logger.info(exc)


class Settings(BaseSettings):
    API_V1: str = "/api/v1"
    PROJECT_NAME: str = "KYVE Slashing Monitoring"
    VERSION: str = "0.0.1"
    DESCRIPTION: str = "KYVE Slashing Monitoring."
    DOCS_URL: str = "/documentation"

    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []

    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)

    # _______________________HEADERS FOR REQUEST________________________________
    HEADERS: Dict[str, str] = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
                      "Chrome/74.0.3729.169 Safari/537.36",
    }

    CLICKHOUSE_DRIVER: str = configs["CLICKHOUSE"]["DRIVER"]
    CLICKHOUSE_HOST: str = configs["CLICKHOUSE"]["HOST"]
    CLICKHOUSE_PORT: str = configs["CLICKHOUSE"]["PORT"]
    CLICKHOUSE_NAME: str = configs["CLICKHOUSE"]["NAME"]
    CLICKHOUSE_USER: str = configs["CLICKHOUSE"]["USER"]
    CLICKHOUSE_PASSWORD: str = configs["CLICKHOUSE"]["PASSWORD"]

    CLICKHOUSE_URL: str = f"http://{CLICKHOUSE_HOST}:{CLICKHOUSE_PORT}"

    class Config:
        case_sensitive = True


settings = Settings()
