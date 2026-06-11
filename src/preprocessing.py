"""Preprocesamiento de datos para el repo principal.

Funciones esperadas:
- load_data(path)
- preprocess_dates(df, date_cols)
- impute_and_scale(df, cols)
- save_clean(df, path)
"""
from typing import List
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler


def load_data(path: str) -> pd.DataFrame:
    """Leer CSV y devolver DataFrame."""
    return pd.read_csv(path)


def preprocess_dates(df: pd.DataFrame, date_cols: List[str] = None) -> pd.DataFrame:
    if date_cols is None:
        return df
    for c in date_cols:
        df[c] = pd.to_datetime(df[c], errors='coerce')
    return df


def impute_and_scale(df: pd.DataFrame, cols: List[str]) -> pd.DataFrame:
    imputer = SimpleImputer()
    scaler = StandardScaler()
    df[cols] = imputer.fit_transform(df[cols])
    df[cols] = scaler.fit_transform(df[cols])
    return df


def save_clean(df: pd.DataFrame, path: str) -> None:
    df.to_csv(path, index=False)
