import uvicorn
import matplotlib

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from decouple import config, Csv

from services.plotter.server import plotter_router
# from services.example_service.server import example_router


def app():
    app = FastAPI()

    origins = [
        "http://localhost:8080",
    ]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(plotter_router())

    return app


if __name__ == "__main__":
    # .env file example:
    # MONOLITH=127.0.0.1,8081,debug
    host, port, log_level = config("MONOLITH", cast=Csv())
    uvicorn.run(
        "server:app", host=host, port=int(port), log_level=log_level, reload=True
    )
