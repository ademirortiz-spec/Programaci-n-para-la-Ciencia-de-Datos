"""Análisis exploratorio (EDA) para el repo principal.

Funciones mínimas:
- summary_stats(df)
- generate_plots(df, out_dir)
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os


def summary_stats(df: pd.DataFrame) -> pd.DataFrame:
    return df.describe(include='all')


def generate_plots(df: pd.DataFrame, out_dir: str) -> None:
    os.makedirs(out_dir, exist_ok=True)
    num_cols = df.select_dtypes(include=['number']).columns.tolist()
    if not num_cols:
        return
    plt.figure()
    sns.histplot(df[num_cols[0]].dropna(), kde=False)
    plt.savefig(os.path.join(out_dir, f"hist_{num_cols[0]}.png"))
    plt.close()
