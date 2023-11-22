import os
import sqlite3
from abc import ABC, abstractmethod

import pandas as pd

STORAGE_DIR = os.path.join(os.getcwd(), "forecasts")


class Writer(ABC):
    @classmethod
    @abstractmethod
    def save_weather(cls, weather: pd.DataFrame) -> None:
        ...


class ExcelWriter(Writer):
    @classmethod
    def save_weather(cls, weather: pd.DataFrame) -> None:
        path = os.path.join(STORAGE_DIR, "weather-forecast.xlsx")
        weather.to_excel(path, index=False)


class DBWriter(Writer):
    @classmethod
    def save_weather(cls, weather: pd.DataFrame) -> None:
        path = os.path.join(STORAGE_DIR, "db.sqlite3")
        with sqlite3.connect(path) as connection:
            weather.to_sql(
                name="weather",
                con=connection,
                if_exists="replace",
                index=False,
            )
