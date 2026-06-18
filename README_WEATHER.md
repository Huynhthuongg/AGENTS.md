# 🌤️ Weather Dashboard

A modern, responsive weather dashboard that fetches real-time weather data from OpenWeatherMap API.

## ✨ Features

- 🌍 **Search Cities Worldwide** - Find weather for any city globally
- 🌤️ **Real-time Weather Data** - Current conditions with temperature, humidity, wind, pressure
- ⭐ **Save Favorites** - Bookmark your favorite cities to SQLite
- 📱 **Responsive Design** - Works perfectly on mobile, tablet, and desktop
- 🔒 **Security** - HTTP security headers, input validation
- ⚡ **Fast & Async** - Built with FastAPI and aiohttp
- 🎨 **Modern UI** - Beautiful gradient design with smooth animations

## 🚀 Quick Start

### Prerequisites

- Python 3.10+
- OpenWeatherMap API key (free tier available)

### Installation

1. Clone and setup
```bash
git clone https://github.com/Huynhthuongg/AGENTS.md.git
cd AGENTS.md
git checkout feature/weather-dashboard
```

2. Install dependencies
```bash
pip install fastapi uvicorn aiohttp
```

3. Get your free OpenWeatherMap API key
- Visit https://openweathermap.org/api
- Sign up for a free account
- Generate an API key

4. Set up environment
```bash
cp config/weather.env.example .env
# Edit .env and add your OpenWeatherMap API key
```

5. Run the application
```bash
export OPENWEATHER_API_KEY="your_api_key_here"
python -m weather_dashboard.app
```

Open your browser: **http://127.0.0.1:8001**

## 📋 API Endpoints

### `GET /`
Serves the main dashboard HTML.

### `GET /health`
Health check endpoint.
```json
{"status": "ok", "version": "1.0.0"}
```

### `GET /api/weather`
Get current weather for coordinates.

**Parameters:**
- `lat` (float, required) - Latitude
- `lon` (float, required) - Longitude

**Response:**
```json
{
  "city": "London",
  "country": "GB",
  "temperature": 15.5,
  "feels_like": 14.2,
  "temp_min": 13.0,
  "temp_max": 17.0,
  "humidity": 72,
  "pressure": 1013,
  "wind_speed": 3.5,
  "wind_deg": 240,
  "cloudiness": 60,
  "description": "partly cloudy",
  "icon": "02d",
  "icon_url": "https://openweathermap.org/img/wn/02d@2x.png",
  "sunrise": "2026-06-03T05:30:00",
  "sunset": "2026-06-03T21:15:00"
}
```

### `GET /api/search`
Search for cities.

**Parameters:**
- `q` (string, required, min 2 chars) - City name
- `limit` (int, optional, default 5) - Max results (1-20)

**Response:**
```json
[
  {
    "name": "London",
    "latitude": 51.5085,
    "longitude": -0.1257,
    "country": "GB",
    "state": null
  }
]
```

### `GET /api/saved-cities`
Get all saved cities.

**Response:**
```json
[
  {
    "id": 1,
    "city_name": "London",
    "latitude": 51.5085,
    "longitude": -0.1257,
    "added_at": "2026-06-03T10:30:00"
  }
]
```

### `POST /api/saved-cities`
Save a city to favorites.

**Parameters:**
- `city_name` (string, required) - City name
- `latitude` (float, required) - Latitude
- `longitude` (float, required) - Longitude

### `DELETE /api/saved-cities/{city_id}`
Delete a saved city.

## 🛠️ Development

### Project Structure

```
weather_dashboard/
├── __init__.py              # Package initialization
├── app.py                   # FastAPI application
├── config.py                # Configuration management
├── models.py                # Data models
├── weather_service.py       # OpenWeatherMap integration
├── database.py              # SQLite operations
└── templates.py             # HTML templates
```

### Configuration

Edit `.env` file to customize settings:

```bash
# OpenWeatherMap API
OPENWEATHER_API_KEY=your_key

# Server
WEATHER_HOST=127.0.0.1
WEATHER_PORT=8001

# Database
DATABASE_URL=sqlite:///weather_dashboard.db
```

## 🔐 Security

- ✅ HTTP security headers (X-Content-Type-Options, X-Frame-Options, etc.)
- ✅ Input validation with Pydantic
- ✅ Safe path validation
- ✅ Error handling and logging
- ✅ CORS-friendly

## 📱 Responsive Design

- Desktop: 2-column grid layout
- Tablet: Responsive grid
- Mobile: Single column stack

## 🎨 UI Features

- Beautiful gradient background
- Smooth animations and transitions
- Loading spinner
- Error messages
- Real-time weather icons
- Weather details cards

## 🐛 Troubleshooting

### "OPENWEATHER_API_KEY environment variable is required"
```bash
export OPENWEATHER_API_KEY="your_api_key"
```

### Search returns empty results
- Check your internet connection
- Verify OpenWeatherMap API key is valid
- Try searching for a major city first

### Port 8001 already in use
```bash
export WEATHER_PORT=8002
```

## 📦 Dependencies

- **FastAPI** - Web framework
- **Uvicorn** - ASGI server
- **aiohttp** - Async HTTP client
- **Pydantic** - Data validation

## 📄 License

AGPL-3.0-only

## 🤝 Contributing

Contributions welcome! Please create a pull request.

---

**Made with ❤️ by Huynhthuongg**
