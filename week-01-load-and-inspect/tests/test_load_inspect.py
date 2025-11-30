import pytest
import pandas as pd
from pathlib import Path
from src.load_and_inspect import load_data, generate_overview

# Path file (harus sama dengan file yang ada)
RAW_DATA_PATH = Path("data/raw/sample_dataset.csv")

# 1️⃣ Test Load Data
def test_load_data():
    df = load_data(RAW_DATA_PATH)
    # Test: harus return DataFrame
    assert isinstance(df, pd.DataFrame), "Data harus berbentuk DataFrame"
    # Test: dataset tidak kosong
    assert not df.empty, "DataFrame tidak boleh kosong"

# 2️⃣ Test Generate Overview
def test_generate_overview():
    df = load_data(RAW_DATA_PATH)
    overview_df = generate_overview(df)
    # Test: harus DataFrame
    assert isinstance(overview_df, pd.DataFrame), "Overview harus DataFrame"
    # Test: kolom yang dihasilkan sesuai
    expected_cols = ["column_name", "data_type", "missing_values", "unique_values", "sample_value"]
    for col in expected_cols:
        assert col in overview_df.columns, f"Kolom {col} harus ada di overview"
    # Test: jumlah baris overview sama dengan jumlah kolom dataset
    assert len(overview_df) == len(df.columns), "Jumlah baris overview harus sama dengan jumlah kolom dataset"
