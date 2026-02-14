import pandas as pd
import numpy as np


def create_grid_zones(
    df: pd.DataFrame,
    lat_col: str = "latitude",
    lon_col: str = "longitude",
    grid_size_m: float = 300
) -> pd.DataFrame:
    """
    Partition geographic crime points into fixed grid zones
    and aggregate crime counts per zone.

    Parameters
    ----------
    df : pd.DataFrame
        Input dataframe containing latitude and longitude.
    lat_col : str
        Name of latitude column.
    lon_col : str
        Name of longitude column.
    grid_size_m : float
        Grid size in metres (default 300m).

    Returns
    -------
    pd.DataFrame
        Zone-level dataframe containing:
        - zone_id
        - lat_bin
        - lon_bin
        - centroid_lat
        - centroid_lon
        - crime_count
    """

    df = df.copy()

    # --- Degree-to-metre conversion (approximate) ---
    mean_lat = df[lat_col].mean()
    meters_per_degree_lat = 111_320
    meters_per_degree_lon = 111_320 * np.cos(np.radians(mean_lat))

    dlat = grid_size_m / meters_per_degree_lat
    dlon = grid_size_m / meters_per_degree_lon

    min_lat = df[lat_col].min()
    min_lon = df[lon_col].min()

    # --- Assign grid bins ---
    df["lat_bin"] = np.floor((df[lat_col] - min_lat) / dlat).astype(int)
    df["lon_bin"] = np.floor((df[lon_col] - min_lon) / dlon).astype(int)

    df["zone_id"] = (
        "z_" + df["lat_bin"].astype(str) + "_" + df["lon_bin"].astype(str)
    )

    # --- Aggregate crime counts ---
    zones = (
        df.groupby(["zone_id", "lat_bin", "lon_bin"])
        .size()
        .reset_index(name="crime_count")
    )

    # --- Compute centroids ---
    zones["centroid_lat"] = min_lat + (zones["lat_bin"] + 0.5) * dlat
    zones["centroid_lon"] = min_lon + (zones["lon_bin"] + 0.5) * dlon

    return zones.sort_values("crime_count", ascending=False).reset_index(drop=True)
