"""Configuration for Weather Dashboard."""

from dataclasses import dataclass
from typing import Optional
import os


@dataclass
class Settings:
    """Application settings."""

    # API Configuration
    openweather_api_key: str = os.getenv("OPENWEATHER_API_KEY", "")
    openweather_base_url: str = "https://api.openweathermap.org/data/2.5"

    # Server Configuration
    host: str = os.getenv("WEATHER_HOST", "127.0.0.1")
    port: int = int(os.getenv("WEATHER_PORT", "8001"))
    debug: bool = os.getenv("WEATHER_DEBUG", "False").lower() == "true"

    # Database Configuration
    database_url: str = os.getenv("DATABASE_URL", "sqlite:///weather_dashboard.db")

    # Cache Configuration (in seconds)
    cache_ttl: int = int(os.getenv("CACHE_TTL", "600"))  # 10 minutes

    def __post_init__(self):
        """Validate settings after initialization."""
        if not self.openweather_api_key:
            raise ValueError(
                "OPENWEATHER_API_KEY environment variable is required. "
                "Get a free key from https://openweathermap.org/api"
            )


def load_settings() -> Settings:
    """Load and return application settings."""
    return Settings()
