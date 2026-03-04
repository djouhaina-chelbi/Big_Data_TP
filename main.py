import psutil
import time
import csv

from pandas_chunking import pandas_chunking
from dask_method import dask_method
from compression_pandas import compression_pandas

filename = 'augmented_files.csv'

results = []

def measure_ram():
    process = psutil.Process()
    return process.memory_info().rss / (1024 * 1024)  # MB

# Pandas Chunking
ram_before = measure_ram()
chunk_total, chunk_time = pandas_chunking(filename)
ram_after = measure_ram()

results.append(["Pandas Chunking", chunk_total, chunk_time, ram_after - ram_before])

# Dask
ram_before = measure_ram()
dask_total, dask_time = dask_method(filename)
ram_after = measure_ram()

results.append(["Dask", dask_total, dask_time, ram_after - ram_before])

# Compression
ram_before = measure_ram()
comp_total, comp_time = compression_pandas(filename)
ram_after = measure_ram()

results.append(["Compression", comp_total, comp_time, ram_after - ram_before])

# حفظ النتائج في ملف
with open("results.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Method", "Result", "Time(sec)", "RAM Usage (MB)"])
    writer.writerows(results)

print("Results saved in results.csv")