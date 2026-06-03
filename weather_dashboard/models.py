"""Data models for Weather Dashboard."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional


@dataclass(frozen=True)
class Coordinates:
    """Geographic coordinates."""

    latitude: float
    longitude: float


@dataclass(frozen=True)
class WeatherMain:
    """Main weather data."""

    temperature: float
    feels_like: float
    temp_min: float
    temp_max: float
    pressure: int
    humidity: int


@dataclass(frozen=True)
class WeatherDescription:
    """Weather description data."""

    main: str
    description: str
    icon: str


@dataclass(frozen=True)
class Wind:
    """Wind data."""

    speed: float
    deg: int
    gust: Optional[float] = None


@dataclass(frozen=True)
class WeatherData:
    """Complete weather data for a location."""

    city: str
    country: str
    coordinates: Coordinates
    weather: WeatherDescription
    main: WeatherMain
    wind: Wind
    cloudiness: int
    sunrise: datetime
    sunset: datetime
    timezone: int
    timestamp: datetime = field(default_factory=datetime.utcnow)

    @property
    def weather_icon_url(self) -> str:
        """Get the URL for the weather icon."""
        return f"https://openweathermap.org/img/wn/{self.weather.icon}@2x.png"


@dataclass
class SavedCity:
    """Saved city preference."""

    id: Optional[int] = None
    city_name: str = ""
    latitude: float = 0.0
    longitude: float = 0.0
    added_at: datetime = field(default_factory=datetime.utcnow)

    def to_dict(self) -> dict:
        """Convert to dictionary."""
        return {
            "id": self.id,
            "city_name": self.city_name,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "added_at": self.added_at.isoformat(),
        }


@dataclass
class SearchResult:
    """City search result."""

    name: str
    latitude: float
    longitude: float
    country: str
    state: Optional[str] = None

    @property
    def display_name(self) -> str:
        """Get display name for the city."""
        parts = [self.name, self.state or "", self.country]
        return ", ".join(p for p in parts if p)
