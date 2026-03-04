# High-Performance CSV Processing using Pandas and Dask

## 📌 Project Overview

This project demonstrates efficient techniques for processing large CSV files in Python without causing memory overflow.

The experiment compares different Big Data approaches in terms of:

* ⏱ **Execution Time**
* 🧠 **RAM Consumption**
* 💾 **Storage Efficiency**

The goal is to analyze which method provides the best performance when processing large datasets.

---

# 📂 Dataset Used

**File:** `augmented_files.csv`

A compressed version of the dataset is also provided:

```
augmented_files.csv.gz
```

This allows testing **compression efficiency** and **storage optimization**.

---

# 🏗 Project Structure

```
TP_BIG_DATA_2/
│
├ augmented_files.csv
├ augmented_files.csv.gz
│
├ pandas_chunking.py
├ dask_method.py
├ compression_pandas.py
│
├ main.py
├ requirements.txt
├ README.md
└ results.csv
```

---

# ⚙️ Technologies Used

* Python 3
* Pandas
* Dask
* psutil (RAM monitoring)
* gzip

---

# 🔬 Methods Implemented

## 1️⃣ Pandas Chunking

```python
pd.read_csv(file, chunksize=100000)
```

✔ Efficient memory management
✔ Stable processing
❌ Sequential execution

Used when datasets are too large to load fully into RAM.

---

## 2️⃣ Dask Parallel Processing

```python
dd.read_csv(file)
```

✔ Parallel processing
✔ Faster computation
✔ Optimized for Big Data

Dask splits the dataset into partitions and processes them simultaneously.

---

## 3️⃣ File Compression (gzip)

Compression is applied to reduce disk usage.

```python
gzip compression
```

✔ Reduces storage space
❌ Requires additional CPU time

---

# 📊 Experimental Results

Results are saved in `results.csv` after execution.

| Method          | Execution Time (sec) | RAM Usage (MB) |
| --------------- | -------------------- | -------------- |
| Pandas Chunking | Check results.csv    | Check results.csv |
| Dask            | Check results.csv    | Check results.csv |
| Compression     | Check results.csv    | Check results.csv |

---

# 📈 Performance Analysis

🥇 **Fastest Method:** Dask
💾 **Best Storage Optimization:** Compression
⚖ **Balanced Approach:** Pandas Chunking

Dask provides faster execution thanks to **parallel computation**.
Compression significantly reduces storage but increases processing time.

---

# 🧠 Key Takeaways

* Large CSV datasets cannot be safely loaded entirely into memory.
* Chunking improves memory control.
* Parallel processing significantly improves performance.
* Compression reduces storage usage but increases CPU workload.

---

# ▶️ How to Run

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the project:

```bash
python main.py
```

The results will be saved in `results.csv`.

---

# 🎯 Conclusion

This project demonstrates practical techniques for processing large datasets efficiently in Python using **Pandas**, **Dask**, and **Compression strategies**.

