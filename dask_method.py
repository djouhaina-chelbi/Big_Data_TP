import dask.dataframe as dd
import time

def dask_method(filename):
    start = time.time()

    # حل مشكلة dtype
    df = dd.read_csv(filename, assume_missing=True)
    total = df['entropy'].sum().compute()

    elapsed = time.time() - start
    return total, elapsed
