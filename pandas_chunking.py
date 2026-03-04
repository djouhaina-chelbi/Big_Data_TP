import pandas as pd
import time

def pandas_chunking(filename, chunksize=100_000):
    start = time.time()
    total = 0

    for chunk in pd.read_csv(filename, chunksize=chunksize):
        total += chunk['entropy'].sum()

    elapsed = time.time() - start
    return total, elapsed