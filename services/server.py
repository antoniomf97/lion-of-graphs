import uvicorn

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from decouple import config, Csv

from services.plotter.server import plotter_router
# from services.fitter.server import fitter_router


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
    # app.include_router(fitter_router())

    return app


if __name__ == "__main__":
    host, port, log_level = config("MONOLITH", cast=Csv())
    uvicorn.run(
        "server:app", host=host, port=int(port), log_level=log_level, reload=True
    )
