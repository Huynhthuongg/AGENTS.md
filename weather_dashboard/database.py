"""Database operations for Weather Dashboard."""

from __future__ import annotations

import sqlite3
from datetime import datetime
from pathlib import Path
from typing import List, Optional

from .models import SavedCity


class DatabaseManager:
    """Manages database operations for saved cities."""

    def __init__(self, db_path: str = "weather_dashboard.db"):
        """Initialize database manager."""
        self.db_path = db_path
        self.init_db()

    def init_db(self) -> None:
        """Initialize database schema."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS saved_cities (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    city_name TEXT NOT NULL,
                    latitude REAL NOT NULL,
                    longitude REAL NOT NULL,
                    added_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    UNIQUE(city_name, latitude, longitude)
                )
                """
            )
            conn.commit()

    def add_city(self, city_name: str, latitude: float, longitude: float) -> SavedCity:
        """Add a city to saved cities."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            try:
                cursor.execute(
                    """
                    INSERT INTO saved_cities (city_name, latitude, longitude)
                    VALUES (?, ?, ?)
                    """,
                    (city_name, latitude, longitude),
                )
                conn.commit()
                city_id = cursor.lastrowid

                return SavedCity(
                    id=city_id,
                    city_name=city_name,
                    latitude=latitude,
                    longitude=longitude,
                )
            except sqlite3.IntegrityError:
                return self.get_city_by_name(city_name)

    def get_all_cities(self) -> List[SavedCity]:
        """Get all saved cities."""
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute(
                "SELECT id, city_name, latitude, longitude, added_at FROM saved_cities ORDER BY added_at DESC"
            )
            rows = cursor.fetchall()

            return [
                SavedCity(
                    id=row["id"],
                    city_name=row["city_name"],
                    latitude=row["latitude"],
                    longitude=row["longitude"],
                    added_at=datetime.fromisoformat(row["added_at"]),
                )
                for row in rows
            ]

    def get_city_by_name(self, city_name: str) -> Optional[SavedCity]:
        """Get a saved city by name."""
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute(
                "SELECT id, city_name, latitude, longitude, added_at FROM saved_cities WHERE city_name = ?",
                (city_name,),
            )
            row = cursor.fetchone()

            if row:
                return SavedCity(
                    id=row["id"],
                    city_name=row["city_name"],
                    latitude=row["latitude"],
                    longitude=row["longitude"],
                    added_at=datetime.fromisoformat(row["added_at"]),
                )
            return None

    def delete_city(self, city_id: int) -> bool:
        """Delete a saved city."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM saved_cities WHERE id = ?", (city_id,))
            conn.commit()
            return cursor.rowcount > 0

    def delete_city_by_name(self, city_name: str) -> bool:
        """Delete a saved city by name."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM saved_cities WHERE city_name = ?", (city_name,))
            conn.commit()
            return cursor.rowcount > 0
