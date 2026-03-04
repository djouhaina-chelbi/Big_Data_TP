import pandas as pd
import time
import gzip
import shutil

def compression_pandas(filename):
    # Create compressed version
    compressed_file = filename.replace('.csv', '.csv.gz')
    
    # Compress the file
    with open(filename, 'rb') as f_in:
        with gzip.open(compressed_file, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)

    # Measure reading from compressed file
    start = time.time()
    
    df_comp = pd.read_csv(compressed_file, compression='gzip')
    total = df_comp['entropy'].sum()

    elapsed = time.time() - start
    return total, elapsed