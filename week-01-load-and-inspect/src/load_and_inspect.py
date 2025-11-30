import pandas as pd
from pathlib import Path

# PATH
RAW_DATA_PATH = Path("data/raw/sample_dataset.csv")
OUTPUT_PATH = Path("data/processed/data_overview.csv")

def load_data(path):
    """
    Fungsi untuk membaca dataset CSV
    """
    try:
        df = pd.read_csv(path)
        print("Data berhasil dibaca")
        return df
    except Exception as e:
        print(f"Gagal membaca data: {e}")
        return None

def generate_overview(df):
    """
    Fungsi untuk membuat ringkasan dataset:
    - nama kolom
    - tipe data
    - jumlah missing
    - contoh value
    - jumlah unique value
    """
    overview = []

    for col in df.columns:
        overview.append({
            "column_name": col,
            "data_type": str(df[col].dtype),
            "missing_values": df[col].isna().sum(),
            "unique_values": df[col].nunique(),
            "sample_value": df[col].dropna().iloc[0] if not df[col].dropna().empty else None
        })

    return pd.DataFrame(overview)

def main():
    print("Membaca data...")
    df = load_data(RAW_DATA_PATH)

    if df is None:
        return
    
    print("\n Info dataset:")
    print(df.info())

    print("\n 5 baris pertama:")
    print(df.head())

    print("\n Membuat overview dataset...")
    overview_df = generate_overview(df)

    print("\n Menyimpan hasil ke data/processed...")
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    overview_df.to_csv(OUTPUT_PATH, index=False)

    print("Selesai! File data_overview.csv berhasil dibuat")


if __name__ == "__main__":
    main()