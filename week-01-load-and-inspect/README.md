# Week 1 — Load & Inspect Dataset

**Tujuan:** Belajar cara *membuka data* dan *melihat isinya* supaya kita ngerti apa yang mau diproses.

---

## 🍼 Apa sih yang kita lakukan di Week 1?

Minggu ini intinya **kenalan sama data**.
Sebelum dibersihkan, sebelum dibuat laporan, sebelum dipake model AI, kita **harus ngerti datanya dulu**.

Ibarat masak:

> "Sebelum masak, kita lihat dulu bahan-bahannya"

Nah, Week 1 itu lihat bahannya.

---

## 🎯 Kenapa Week 1 penting banget?

Supaya:

* kita **ngerti bentuk datanya** (besar atau kecil?)
* kita **tahu kolom apa aja yang ada**
* kita paham **kolom mana yang kosong**
* kita lihat **kolom mana yang harus dibersihkan**
* kita tahu **apakah dataset ini sehat atau tidak**

Kalau kita salah lihat data di awal → semua proses selanjutnya bakal salah.
Makanya Week 1 itu pondasi.

---

## 📥 Apa yang kita lakukan di kode?

### 1. Load data (buka file)

Kita coba buka:

* CSV
* Excel
* JSON

Contoh:

```python
df = pd.read_csv("data/raw/sample_dataset.csv")
```

---

### 2. Lihat isi data

Pake perintah-perintah dasar:

* `df.head()` → lihat 5 baris pertama
* `df.tail()` → lihat baris terakhir
* `df.shape` → jumlah baris × kolom
* `df.info()` → tipe data tiap kolom
* `df.describe()` → statistik dasar
* `df.isna().sum()` → jumlah missing values

Ini kayak "cek kesehatan data".

---

### 3. Buat file ringkasan: `data_overview.csv`

Isinya:

* nama kolom
* tipe data
* jumlah missing
* contoh isi kolom
* jumlah unique value

Jadi kita punya **raport kecil** tentang dataset.

---

## 🧃 Output Week 1 (yang harus ada)

✔ Notebook: `01_inspect_dataset.ipynb`
✔ File hasil: `data_overview.csv`
✔ Script otomatis: `load_and_inspect.py`
✔ Folder rapi
✔ README ini 😁

---

## 📁 Struktur Folder Week 1

```
week-01-load-inspect/
│
├── data/
│   ├── raw/
│   │   └── sample_dataset.csv
│   ├── processed/
│   │   └── data_overview.csv
│
├── notebooks/
│   └── 01_inspect_dataset.ipynb
│
├── src/
│   └── load_and_inspect.py
│
├── tests/
│   └── test_load_inspect.py
│
└── README.md
```

Penjelasan:

* **data/raw** → data asli, jangan disentuh
* **data/processed** → hasil inspeksi
* **src** → kode utama
* **notebooks** → tempat eksplorasi
* **tests** → opsional, buat cek fungsi
* **README.md** → file yang kamu baca ini

---

## 🍪 Cara menjalankan file

1. Pastikan install paket yang dibutuhkan:

```
pip install -r requirements.txt
```

2. Jalankan script:

```
python src/load_and_inspect.py
```

3. Hasilnya ada di:

```
data/processed/data_overview.csv
```

---

## 🎉 Apa yang harus kamu pahami setelah Week 1?

Minggu ini kamu sudah bisa:

* buka file CSV / Excel / JSON
* lihat isi dataset dengan benar
* paham struktur data
* tahu kolom mana yang kosong
* menghasilkan laporan ringkas otomatis
* punya pondasi sebelum masuk cleaning

Ini skill dasar tapi **super penting** untuk automation.