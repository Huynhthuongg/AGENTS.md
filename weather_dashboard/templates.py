"""HTML templates for Weather Dashboard."""

from __future__ import annotations

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Weather Dashboard</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        :root {
            --primary: #667eea;
            --secondary: #764ba2;
            --accent: #f093fb;
            --bg-light: #f7fafc;
            --bg-dark: #1a202c;
            --text-dark: #2d3748;
            --text-light: #718096;
            --border: #e2e8f0;
            --shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
        }

        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
            background: linear-gradient(135deg, var(--primary) 0%, var(--secondary) 100%);
            min-height: 100vh;
            padding: 20px;
            color: var(--text-dark);
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
        }

        header {
            text-align: center;
            color: white;
            margin-bottom: 40px;
        }

        header h1 {
            font-size: 2.5rem;
            margin-bottom: 10px;
            text-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        }

        header p {
            font-size: 1.1rem;
            opacity: 0.9;
        }

        .main-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 30px;
            margin-bottom: 40px;
        }

        .card {
            background: white;
            border-radius: 20px;
            padding: 30px;
            box-shadow: var(--shadow);
            transition: transform 0.3s, box-shadow 0.3s;
        }

        .card:hover {
            transform: translateY(-5px);
            box-shadow: 0 15px 40px rgba(0, 0, 0, 0.15);
        }

        .search-section h2,
        .saved-cities-section h2 {
            font-size: 1.5rem;
            margin-bottom: 20px;
            color: var(--text-dark);
        }

        .search-container {
            display: flex;
            gap: 10px;
            margin-bottom: 20px;
        }

        .search-container input {
            flex: 1;
            padding: 12px 16px;
            border: 2px solid var(--border);
            border-radius: 10px;
            font-size: 1rem;
            transition: border-color 0.3s;
        }

        .search-container input:focus {
            outline: none;
            border-color: var(--primary);
        }

        .search-container button {
            padding: 12px 24px;
            background: linear-gradient(135deg, var(--primary), var(--secondary));
            color: white;
            border: none;
            border-radius: 10px;
            font-weight: 600;
            cursor: pointer;
            transition: transform 0.2s;
        }

        .search-container button:active {
            transform: scale(0.98);
        }

        .search-results {
            display: flex;
            flex-direction: column;
            gap: 10px;
            max-height: 300px;
            overflow-y: auto;
        }

        .search-result-item {
            padding: 12px;
            background: var(--bg-light);
            border-radius: 8px;
            cursor: pointer;
            transition: background-color 0.2s;
        }

        .search-result-item:hover {
            background-color: #e2e8f0;
        }

        .weather-display {
            text-align: center;
        }

        .weather-icon {
            font-size: 80px;
            margin: 20px 0;
        }

        .temperature {
            font-size: 3rem;
            font-weight: 700;
            color: var(--primary);
            margin-bottom: 10px;
        }

        .weather-description {
            font-size: 1.3rem;
            color: var(--text-light);
            text-transform: capitalize;
            margin-bottom: 20px;
        }

        .weather-details {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 15px;
            margin-top: 20px;
            padding-top: 20px;
            border-top: 2px solid var(--border);
        }

        .detail-item {
            text-align: left;
        }

        .detail-label {
            font-size: 0.9rem;
            color: var(--text-light);
            margin-bottom: 5px;
        }

        .detail-value {
            font-size: 1.2rem;
            font-weight: 600;
            color: var(--text-dark);
        }

        .saved-cities-list {
            display: flex;
            flex-direction: column;
            gap: 10px;
            max-height: 400px;
            overflow-y: auto;
        }

        .city-item {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 15px;
            background: var(--bg-light);
            border-radius: 10px;
            cursor: pointer;
            transition: background-color 0.2s;
        }

        .city-item:hover {
            background-color: #e2e8f0;
        }

        .city-item-name {
            font-weight: 600;
            color: var(--text-dark);
        }

        .city-item-delete {
            background: #f56565;
            color: white;
            border: none;
            border-radius: 5px;
            padding: 5px 10px;
            cursor: pointer;
            font-size: 0.9rem;
            transition: background-color 0.2s;
        }

        .city-item-delete:hover {
            background-color: #e53e3e;
        }

        .save-button {
            width: 100%;
            padding: 12px;
            background: linear-gradient(135deg, var(--primary), var(--secondary));
            color: white;
            border: none;
            border-radius: 10px;
            font-weight: 600;
            cursor: pointer;
            margin-top: 15px;
            transition: transform 0.2s;
        }

        .save-button:active {
            transform: scale(0.98);
        }

        .save-button:disabled {
            opacity: 0.5;
            cursor: not-allowed;
        }

        .loading {
            text-align: center;
            padding: 40px;
            color: var(--text-light);
        }

        .spinner {
            border: 4px solid var(--border);
            border-top: 4px solid var(--primary);
            border-radius: 50%;
            width: 40px;
            height: 40px;
            animation: spin 1s linear infinite;
            margin: 20px auto;
        }

        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }

        .error {
            padding: 15px;
            background: #fed7d7;
            color: #c53030;
            border-radius: 8px;
            margin-bottom: 15px;
            display: none;
        }

        .error.show {
            display: block;
        }

        @media (max-width: 768px) {
            .main-grid {
                grid-template-columns: 1fr;
            }

            header h1 {
                font-size: 1.8rem;
            }

            .temperature {
                font-size: 2.5rem;
            }

            .weather-details {
                grid-template-columns: 1fr;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>🌤️ Weather Dashboard</h1>
            <p>Get real-time weather information from around the world</p>
        </header>

        <div class="main-grid">
            <!-- Search and Weather Display -->
            <div class="card">
                <div class="search-section">
                    <h2>Search Weather</h2>
                    <div class="error" id="error-message"></div>
                    
                    <div class="search-container">
                        <input 
                            type="text" 
                            id="search-input" 
                            placeholder="Search for a city..."
                            autocomplete="off"
                        >
                        <button onclick="searchCities()">Search</button>
                    </div>

                    <div class="search-results" id="search-results" style="display: none;"></div>

                    <div id="weather-display" class="loading" style="display: none;">
                        <div class="spinner"></div>
                        <p>Loading weather...</p>
                    </div>
                </div>
            </div>

            <!-- Saved Cities -->
            <div class="card">
                <div class="saved-cities-section">
                    <h2>Saved Cities</h2>
                    <div class="saved-cities-list" id="saved-cities-list">
                        <p style="color: var(--text-light); text-align: center;">No saved cities yet</p>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <script>
        const API_BASE = '/api';
        let currentWeather = null;

        async function searchCities() {
            const query = document.getElementById('search-input').value.trim();
            if (!query) return;

            try {
                hideError();
                const response = await fetch(`${API_BASE}/search?q=${encodeURIComponent(query)}&limit=5`);
                if (!response.ok) throw new Error('Search failed');
                
                const results = await response.json();
                displaySearchResults(results);
            } catch (error) {
                showError('Failed to search cities: ' + error.message);
            }
        }

        function displaySearchResults(results) {
            const container = document.getElementById('search-results');
            if (results.length === 0) {
                container.style.display = 'none';
                return;
            }

            container.innerHTML = results.map(city => `
                <div class="search-result-item" onclick="fetchWeather(${city.latitude}, ${city.longitude}, '${city.name}', '${city.country}')">
                    <strong>${city.name}</strong>, ${city.state ? city.state + ', ' : ''}${city.country}
                </div>
            `).join('');
            container.style.display = 'flex';
        }

        async function fetchWeather(lat, lon, cityName, country) {
            try {
                hideError();
                showWeatherLoading();
                
                const response = await fetch(`${API_BASE}/weather?lat=${lat}&lon=${lon}`);
                if (!response.ok) throw new Error('Failed to fetch weather');
                
                currentWeather = await response.json();
                currentWeather.lat = lat;
                currentWeather.lon = lon;
                
                displayWeather(currentWeather);
                document.getElementById('search-results').style.display = 'none';
            } catch (error) {
                showError('Failed to fetch weather: ' + error.message);
                hideWeatherLoading();
            }
        }

        function displayWeather(weather) {
            const display = document.getElementById('weather-display');
            
            const sunrise = new Date(weather.sunrise).toLocaleTimeString([], {hour: '2-digit', minute:'2-digit'});
            const sunset = new Date(weather.sunset).toLocaleTimeString([], {hour: '2-digit', minute:'2-digit'});

            display.innerHTML = `
                <h3>${weather.city}, ${weather.country}</h3>
                <img src="${weather.icon_url}" alt="${weather.description}" class="weather-icon">
                <div class="temperature">${Math.round(weather.temperature)}°C</div>
                <div class="weather-description">${weather.description}</div>
                
                <div class="weather-details">
                    <div class="detail-item">
                        <div class="detail-label">Feels Like</div>
                        <div class="detail-value">${Math.round(weather.feels_like)}°C</div>
                    </div>
                    <div class="detail-item">
                        <div class="detail-label">Humidity</div>
                        <div class="detail-value">${weather.humidity}%</div>
                    </div>
                    <div class="detail-item">
                        <div class="detail-label">Wind Speed</div>
                        <div class="detail-value">${weather.wind_speed} m/s</div>
                    </div>
                    <div class="detail-item">
                        <div class="detail-label">Pressure</div>
                        <div class="detail-value">${weather.pressure} hPa</div>
                    </div>
                    <div class="detail-item">
                        <div class="detail-label">Min/Max</div>
                        <div class="detail-value">${Math.round(weather.temp_min)}°C / ${Math.round(weather.temp_max)}°C</div>
                    </div>
                    <div class="detail-item">
                        <div class="detail-label">Sunrise/Sunset</div>
                        <div class="detail-value">${sunrise} / ${sunset}</div>
                    </div>
                </div>
                
                <button class="save-button" onclick="saveCurrentCity()">⭐ Save City</button>
            `;
            display.style.display = 'block';
        }

        function showWeatherLoading() {
            const display = document.getElementById('weather-display');
            display.innerHTML = '<div class="spinner"></div><p>Loading weather...</p>';
            display.style.display = 'block';
        }

        async function saveCurrentCity() {
            if (!currentWeather) return;

            try {
                const response = await fetch(
                    `${API_BASE}/saved-cities?city_name=${encodeURIComponent(currentWeather.city)}&latitude=${currentWeather.lat}&longitude=${currentWeather.lon}`,
                    { method: 'POST' }
                );
                if (!response.ok) throw new Error('Failed to save city');
                
                loadSavedCities();
                showError('City saved successfully!');
                setTimeout(hideError, 3000);
            } catch (error) {
                showError('Failed to save city: ' + error.message);
            }
        }

        async function loadSavedCities() {
            try {
                const response = await fetch(`${API_BASE}/saved-cities`);
                if (!response.ok) throw new Error('Failed to load saved cities');
                
                const cities = await response.json();
                displaySavedCities(cities);
            } catch (error) {
                console.error('Failed to load saved cities:', error);
            }
        }

        function displaySavedCities(cities) {
            const container = document.getElementById('saved-cities-list');
            
            if (cities.length === 0) {
                container.innerHTML = '<p style="color: var(--text-light); text-align: center;">No saved cities yet</p>';
                return;
            }

            container.innerHTML = cities.map(city => `
                <div class="city-item" onclick="fetchWeather(${city.latitude}, ${city.longitude}, '${city.city_name}', '')">
                    <span class="city-item-name">${city.city_name}</span>
                    <button class="city-item-delete" onclick="event.stopPropagation(); deleteCity(${city.id})">Delete</button>
                </div>
            `).join('');
        }

        async function deleteCity(cityId) {
            try {
                const response = await fetch(`${API_BASE}/saved-cities/${cityId}`, { method: 'DELETE' });
                if (!response.ok) throw new Error('Failed to delete city');
                loadSavedCities();
            } catch (error) {
                showError('Failed to delete city: ' + error.message);
            }
        }

        function showError(message) {
            const errorDiv = document.getElementById('error-message');
            errorDiv.textContent = message;
            errorDiv.classList.add('show');
        }

        function hideError() {
            const errorDiv = document.getElementById('error-message');
            errorDiv.classList.remove('show');
        }

        document.addEventListener('DOMContentLoaded', () => {
            document.getElementById('search-input').addEventListener('keypress', (e) => {
                if (e.key === 'Enter') searchCities();
            });
            
            loadSavedCities();
        });
    </script>
</body>
</html>
"""


def get_index_html() -> str:
    """Get the index HTML template."""
    return HTML_TEMPLATE
