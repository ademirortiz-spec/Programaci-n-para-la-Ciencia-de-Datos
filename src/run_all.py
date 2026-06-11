"""Orquestador mínimo dentro del repo principal.

Uso ejemplo:
    python -m src.run_all --data data/raw/EarthquakesChile_2000-2024.csv --outdir figures
"""
import argparse
from .preprocessing import load_data, preprocess_dates, impute_and_scale, save_clean
from .eda import generate_plots


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--data', required=True)
    parser.add_argument('--outdir', required=True)
    args = parser.parse_args()

    df = load_data(args.data)
    df = preprocess_dates(df, date_cols=['UTC Date', 'Date'])
    num_cols = df.select_dtypes(include=['number']).columns.tolist()
    if num_cols:
        df = impute_and_scale(df, num_cols)
    save_clean(df, 'data/clean.csv')
    generate_plots(df, args.outdir)


if __name__ == '__main__':
    main()
