"""Weather API service for fetching weather data."""

from __future__ import annotations

import aiohttp
from datetime import datetime
from typing import Optional, List
import logging

from .config import Settings
from .models import (
    WeatherData,
    Coordinates,
    WeatherMain,
    WeatherDescription,
    Wind,
    SearchResult,
)

logger = logging.getLogger(__name__)


class WeatherService:
    """Service for fetching weather data from OpenWeatherMap API."""

    def __init__(self, settings: Settings):
        """Initialize weather service."""
        self.settings = settings
        self.base_url = settings.openweather_base_url
        self.api_key = settings.openweather_api_key

    async def get_current_weather(
        self, latitude: float, longitude: float
    ) -> WeatherData:
        """Fetch current weather for given coordinates."""
        url = f"{self.base_url}/weather"
        params = {
            "lat": latitude,
            "lon": longitude,
            "appid": self.api_key,
            "units": "metric",
        }

        async with aiohttp.ClientSession() as session:
            async with session.get(url, params=params, timeout=aiohttp.ClientTimeout(total=10)) as response:
                if response.status != 200:
                    error_data = await response.json()
                    raise ValueError(f"Weather API error: {error_data.get('message', 'Unknown error')}")

                data = await response.json()
                return self._parse_weather_response(data)

    async def search_cities(self, query: str, limit: int = 5) -> List[SearchResult]:
        """Search for cities by name."""
        url = f"{self.base_url}/../geo/1.0/direct"
        params = {
            "q": query,
            "limit": limit,
            "appid": self.api_key,
        }

        async with aiohttp.ClientSession() as session:
            async with session.get(url, params=params, timeout=aiohttp.ClientTimeout(total=10)) as response:
                if response.status != 200:
                    logger.error(f"City search failed with status {response.status}")
                    return []

                data = await response.json()
                return [
                    SearchResult(
                        name=item["name"],
                        latitude=item["lat"],
                        longitude=item["lon"],
                        country=item.get("country", ""),
                        state=item.get("state", None),
                    )
                    for item in data
                ]

    def _parse_weather_response(self, data: dict) -> WeatherData:
        """Parse OpenWeatherMap API response."""
        coords = data.get("coord", {})
        weather = data.get("weather", [{}])[0]
        main = data.get("main", {})
        wind = data.get("wind", {})
        sys = data.get("sys", {})

        return WeatherData(
            city=data.get("name", "Unknown"),
            country=sys.get("country", ""),
            coordinates=Coordinates(
                latitude=coords.get("lat", 0.0),
                longitude=coords.get("lon", 0.0),
            ),
            weather=WeatherDescription(
                main=weather.get("main", ""),
                description=weather.get("description", ""),
                icon=weather.get("icon", "01d"),
            ),
            main=WeatherMain(
                temperature=main.get("temp", 0.0),
                feels_like=main.get("feels_like", 0.0),
                temp_min=main.get("temp_min", 0.0),
                temp_max=main.get("temp_max", 0.0),
                pressure=main.get("pressure", 0),
                humidity=main.get("humidity", 0),
            ),
            wind=Wind(
                speed=wind.get("speed", 0.0),
                deg=wind.get("deg", 0),
                gust=wind.get("gust", None),
            ),
            cloudiness=data.get("clouds", {}).get("all", 0),
            sunrise=datetime.fromtimestamp(sys.get("sunrise", 0)),
            sunset=datetime.fromtimestamp(sys.get("sunset", 0)),
            timezone=data.get("timezone", 0),
        )
