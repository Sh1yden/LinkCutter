from fastapi import FastAPI
from fastapi.responses import JSONResponse

from app.api.endpoints import router as main_router
from app.api.lifespan import lifespan
from app.core import get_logger, setup_logging, settings

_lg = get_logger("LinkCutter")
setup_logging(settings.LOG_LEVEL)

_lg.debug("Creating the app...")

app: FastAPI = FastAPI(
    title="LinkCutter",
    version="v0.2.2",
    root_path="/linkcutter",
    docs_url="/api/swagger_docs",
    redoc_url="/api/redoc_docs",
    openapi_url="/api/openapi.json",
    lifespan=lifespan,
    default_response_class=JSONResponse,
)

app.include_router(main_router, prefix="/api", tags=["api.linkcutter"])
