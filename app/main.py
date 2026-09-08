from fastapi import FastAPI, Request

from prometheus_client import make_asgi_app
from app.metrics.http_metrics import (http_requests_total, http_request_duration_seconds)
import time


from app.database import Base, engine

from app.routers.health import router as health_router
from app.routers.performance import router as performance_router

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(health_router)
app.include_router(performance_router)

metrics_app = make_asgi_app()
app.mount("/metrics", metrics_app)

@app.middleware("http")
async def metrics_middleware(request: Request, call_next):
    if request.url.path in ("/metrics/", "/metrics"):
        return await call_next(request)

    start_time = time.perf_counter()

    try: 
        response = await call_next(request)

        duration = time.perf_counter() - start_time
        status_code = response.status_code

    except Exception: 
        status_code = 500

        route = request.scope.get("route")

        endpoint = (
            route.path
            if route 
            else request.url.path
        )

        http_requests_total.labels(
            method=request.method,
            endpoint=endpoint,
            status_code=status_code
        ).inc()

        raise

    route = request.scope.get("route")

    endpoint = (
        route.path
        if route
        else request.url.path
    )

    http_requests_total.labels(
        method=request.method,
        endpoint=endpoint,
        status_code=status_code
    ).inc()

    http_request_duration_seconds.labels(
        method=request.method,
        endpoint=endpoint
    ).observe(duration)

    return response   
    



