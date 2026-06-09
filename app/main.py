from fastapi import FastAPI
from app.api.endpoints import router as main_router
from app.api.lifespan import lifespan

app = FastAPI(
    title="LinkCutter",
    version="v0.1.0",
    docs_url="/api.linkcutter/swagger_docs",
    redoc_url="/api.linkcutter/redoc_docs",
    openapi_url="/api.linkcutter/openapi",
    lifespan=lifespan,
)

app.include_router(main_router, prefix="/api.linkcutter", tags=["api.linkcutter"])
