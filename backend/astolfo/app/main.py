from http import HTTPStatus

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from api.v1.routes import api_v1_router
from settings import settings

app = FastAPI(
    title=settings.PROJECT_NAME, openapi_url=f"{settings.API_V1_STR}/openapi.json"
)


# Define the list of allowed origins
origins = [
    "http://localhost:3002",  # Example: React frontend running locally
    "https://example.com",    # Example: Deployed frontend
]

# Add the CORS middleware to the application
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,          # Specify allowed origins
    allow_credentials=True,         # Allow cookies and authentication headers
    allow_methods=["*"],            # Allow all HTTP methods
    allow_headers=["*"],            # Allow all headers
)


@app.get("/health/check", tags=["Monitoring"], operation_id="health_check")
def health_check():
    return HTTPStatus.OK


app.include_router(api_v1_router, prefix=settings.API_V1_STR)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)