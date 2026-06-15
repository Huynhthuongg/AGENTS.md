"""FastAPI application for Weather Dashboard."""

from __future__ import annotations

import logging
from typing import List

from fastapi import FastAPI, HTTPException, Query
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

from .config import Settings, load_settings
from .weather_service import WeatherService
from .database import DatabaseManager
from .templates import get_index_html

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize settings
settings = load_settings()

# Initialize services
weather_service = WeatherService(settings)
db_manager = DatabaseManager()

# Create FastAPI app
app = FastAPI(
    title="Weather Dashboard",
    description="Real-time weather information from OpenWeatherMap",
    version="1.0.0",
)


# Pydantic models for API
class WeatherResponse(BaseModel):
    """Weather response model."""

    city: str
    country: str
    temperature: float
    feels_like: float
    temp_min: float
    temp_max: float
    humidity: int
    pressure: int
    wind_speed: float
    wind_deg: int
    cloudiness: int
    description: str
    icon: str
    icon_url: str
    sunrise: str
    sunset: str


class SavedCityResponse(BaseModel):
    """Saved city response model."""

    id: int
    city_name: str
    latitude: float
    longitude: float
    added_at: str


class SearchResultResponse(BaseModel):
    """Search result response model."""

    name: str
    latitude: float
    longitude: float
    country: str
    state: str | None


# Security middleware
@app.middleware("http")
async def security_headers(request, call_next):
    """Add security headers to response."""
    response = await call_next(request)
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["X-XSS-Protection"] = "1; mode=block"
    response.headers["Referrer-Policy"] = "no-referrer"
    return response


# Routes
@app.get("/", response_class=HTMLResponse)
async def index() -> str:
    """Serve the dashboard HTML."""
    return get_index_html()


@app.get("/health")
async def health() -> dict:
    """Health check endpoint."""
    return {"status": "ok", "version": "1.0.0"}


@app.get("/api/weather", response_model=WeatherResponse)
async def get_weather(
    lat: float = Query(..., description="Latitude"),
    lon: float = Query(..., description="Longitude"),
) -> WeatherResponse:
    """Get current weather for given coordinates."""
    try:
        weather_data = await weather_service.get_current_weather(lat, lon)
        return WeatherResponse(
            city=weather_data.city,
            country=weather_data.country,
            temperature=weather_data.main.temperature,
            feels_like=weather_data.main.feels_like,
            temp_min=weather_data.main.temp_min,
            temp_max=weather_data.main.temp_max,
            humidity=weather_data.main.humidity,
            pressure=weather_data.main.pressure,
            wind_speed=weather_data.wind.speed,
            wind_deg=weather_data.wind.deg,
            cloudiness=weather_data.cloudiness,
            description=weather_data.weather.description,
            icon=weather_data.weather.icon,
            icon_url=weather_data.weather_icon_url,
            sunrise=weather_data.sunrise.isoformat(),
            sunset=weather_data.sunset.isoformat(),
        )
    except Exception as e:
        logger.error(f"Error fetching weather: {e}")
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/api/search", response_model=List[SearchResultResponse])
async def search_cities(
    q: str = Query(..., min_length=2, description="City name to search"),
    limit: int = Query(5, ge=1, le=20),
) -> List[SearchResultResponse]:
    """Search for cities by name."""
    try:
        results = await weather_service.search_cities(q, limit)
        return [
            SearchResultResponse(
                name=result.name,
                latitude=result.latitude,
                longitude=result.longitude,
                country=result.country,
                state=result.state,
            )
            for result in results
        ]
    except Exception as e:
        logger.error(f"Error searching cities: {e}")
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/api/saved-cities", response_model=List[SavedCityResponse])
async def get_saved_cities() -> List[SavedCityResponse]:
    """Get all saved cities."""
    cities = db_manager.get_all_cities()
    return [
        SavedCityResponse(
            id=city.id,
            city_name=city.city_name,
            latitude=city.latitude,
            longitude=city.longitude,
            added_at=city.added_at.isoformat(),
        )
        for city in cities
    ]


@app.post("/api/saved-cities", response_model=SavedCityResponse)
async def save_city(
    city_name: str = Query(..., description="City name"),
    latitude: float = Query(..., description="Latitude"),
    longitude: float = Query(..., description="Longitude"),
) -> SavedCityResponse:
    """Save a city to favorites."""
    try:
        saved_city = db_manager.add_city(city_name, latitude, longitude)
        return SavedCityResponse(
            id=saved_city.id,
            city_name=saved_city.city_name,
            latitude=saved_city.latitude,
            longitude=saved_city.longitude,
            added_at=saved_city.added_at.isoformat(),
        )
    except Exception as e:
        logger.error(f"Error saving city: {e}")
        raise HTTPException(status_code=400, detail=str(e))


@app.delete("/api/saved-cities/{city_id}")
async def delete_saved_city(city_id: int) -> dict:
    """Delete a saved city."""
    success = db_manager.delete_city(city_id)
    if not success:
        raise HTTPException(status_code=404, detail="City not found")
    return {"status": "deleted"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        app,
        host=settings.host,
        port=settings.port,
        log_level="info",
    )
