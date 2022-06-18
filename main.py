from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from src.core.config import settings
from src.api import routers


def get_application() -> FastAPI:
    application = FastAPI(title=settings.PROJECT_NAME,
                          docs_url=settings.DOCS_URL,
                          description=settings.DESCRIPTION,
                          version=settings.VERSION,
                          redoc_url=None)

    if settings.BACKEND_CORS_ORIGINS:
        application.add_middleware(
            CORSMiddleware,
            allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )
    # Connect API routes
    application.include_router(routers.router, prefix=settings.API_V1)

    return application
