"""
UK Police API client (Day 2): street-level crime ingestion.

Docs: https://data.police.uk/docs/

Design goals:
- simple, reliable retrieval for a (lat, lon, month) query
- return a tidy pandas DataFrame with stable column names
- lightweight retry/backoff for transient failures
"""

from __future__ import annotations

import time
from dataclasses import dataclass
from typing import Optional

import pandas as pd
import requests

BASE_URL = "https://data.police.uk/api"


@dataclass(frozen=True)
class PoliceAPISession:
    timeout_s: int = 30
    max_retries: int = 3
    backoff_s: float = 1.0

    def get_json(self, path: str, params: Optional[dict] = None):
        url = f"{BASE_URL}/{path.lstrip('/')}"
        last_exc = None

        for attempt in range(1, self.max_retries + 1):
            try:
                r = requests.get(url, params=params, timeout=self.timeout_s)
                r.raise_for_status()
                return r.json()
            except Exception as exc:
                last_exc = exc
                if attempt < self.max_retries:
                    time.sleep(self.backoff_s * attempt)
                else:
                    raise last_exc


def get_crimes_all_categories(
    latitude: float,
    longitude: float,
    date: str,
    session: Optional[PoliceAPISession] = None,
) -> pd.DataFrame:
    """
    Pull street-level crimes around a point for a given month.

    Parameters
    ----------
    latitude, longitude : float
    date : str
        Month in "YYYY-MM" (e.g., "2025-12").
    session : PoliceAPISession, optional

    Returns
    -------
    pd.DataFrame
        Normalised crimes with consistent column names.
    """
    if session is None:
        session = PoliceAPISession()

    params = {"lat": latitude, "lng": longitude, "date": date}
    data = session.get_json("crimes-street/all-crime", params=params)

    if not data:
        return pd.DataFrame()

    df = pd.json_normalize(data)

    rename_map = {
        "category": "crime_category",
        "location.latitude": "latitude",
        "location.longitude": "longitude",
        "location.street.id": "street_id",
        "location.street.name": "street_name",
        "outcome_status.category": "outcome_category",
        "outcome_status.date": "outcome_date",
    }
    df = df.rename(columns={k: v for k, v in rename_map.items() if k in df.columns})

    for c in ["latitude", "longitude"]:
        if c in df.columns:
            df[c] = pd.to_numeric(df[c], errors="coerce")

    keep = [
        "crime_category",
        "persistent_id",
        "month",
        "latitude",
        "longitude",
        "street_id",
        "street_name",
        "location_type",
        "outcome_category",
        "outcome_date",
    ]
    keep = [c for c in keep if c in df.columns]
    return df[keep].copy()
