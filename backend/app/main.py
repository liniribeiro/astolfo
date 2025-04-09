import logging
from http import HTTPStatus

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from starlette.requests import Request
from starlette.responses import JSONResponse

from api.v1.routes import api_v1_router
from exceptions.exceptions import Error
from settings import settings

app = FastAPI(
    title=settings.PROJECT_NAME, openapi_url=f"{settings.API_V1_STR}/openapi.json"
)


# Add the CORS middleware to the application
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],          # Specify allowed origins
    allow_credentials=True,         # Allow cookies and authentication headers
    allow_methods=["*"],            # Allow all HTTP methods
    allow_headers=["*"],            # Allow all headers
)


@app.exception_handler(Exception)
async def generic_exception_handler(request: Request, exc: Exception):
    if isinstance(exc, Error):
        return JSONResponse(
            status_code=exc.status_code,
            content=exc.to_dict(),
        )
    logging.exception("Unhandled error occurred")
    return JSONResponse(
        status_code=500,
        content={"description": "Internal Server Error",
                 "name": "internal-server-error",
                 "detail": str(exc)},
    )

@app.get("/health/check", tags=["Monitoring"], operation_id="health_check")
def health_check():
    return HTTPStatus.OK


app.include_router(api_v1_router, prefix=settings.API_V1_STR)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)