from fastapi import FastAPI
from scripts import Configs, WeatherStatus
import uvicorn
import os


app = FastAPI()

BASEDIR = os.path.dirname(os.path.abspath(__file__))
CONFIGDIR = os.path.join(BASEDIR, "configs")
CONFIGPATH = os.path.join(CONFIGDIR, "appConfigs.yaml")

conf = Configs.createConfigWithFile(CONFIGPATH)
weatherManager = WeatherStatus(conf)

@app.get("/")
async def root(): return {"author": "Muhammed Taşkır"}

@app.get("/temperature")
async def get_temp(city: str): return weatherManager.findWithCity(city)


if __name__ == "__main__": uvicorn.run(app, host = "0.0.0.0", port = 5000)