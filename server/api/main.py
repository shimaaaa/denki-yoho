from api import views
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/ping")
async def root():
    return "pong"


@app.get("/api/forecast", response_model=views.ForecastListResponse)
async def forecast_list() -> views.ForecastListResponse:
    return views.forecast_list()
