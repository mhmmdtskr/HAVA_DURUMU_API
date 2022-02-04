from dataclasses import dataclass, field
from scripts.configs import Configs
import requests


@dataclass
class WeatherStatus:
    configs: Configs

    def findWithCity(self, city: str) -> dict:
        api_key = self.configs.config["openweather"]["api_key"]
        responseOWM = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric").json()
        return {"temperature": responseOWM["main"]["temp"]}