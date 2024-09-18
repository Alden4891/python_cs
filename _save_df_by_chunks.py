import pandas as pd
import os

# Function to split DataFrame into smaller chunks and save them
def save_large_df_in_chunks(df, chunk_size=10000, file_prefix='chunk'):
    num_chunks = (len(df) // chunk_size) + 1
    for i in range(num_chunks):
        start_row = i * chunk_size
        end_row = min((i + 1) * chunk_size, len(df))
        chunk = df.iloc[start_row:end_row]
        chunk_filename = f'{file_prefix}_{i + 1}.csv'
        chunk.to_csv(chunk_filename, index=False)
        print(f'Saved {chunk_filename}')

# Function to merge chunks back into a single DataFrame
def merge_chunks(file_prefix='chunk'):
    chunk_files = sorted([f for f in os.listdir() if f.startswith(file_prefix) and f.endswith('.csv')])
    
    if not chunk_files:
        print("No chunk files found with the given prefix.")
        return None

    dfs = []
    for file in chunk_files:
        print(f'Loading {file}...')
        df_chunk = pd.read_csv(file)
        dfs.append(df_chunk)

    combined_df = pd.concat(dfs, ignore_index=True)
    return combined_df

# Sample usage
if __name__ == "__main__":
    # Replace this with your actual DataFrame loading logic
    # For example, df = pd.read_csv('large_file.csv')
    data = {
        'A': range(100000),  # Example data
        'B': range(100000, 200000)
    }
    df = pd.DataFrame(data)

    # Save the DataFrame in chunks
    save_large_df_in_chunks(df)

    # Merge the chunks back into a single DataFrame
    combined_df = merge_chunks()
    
    if combined_df is not None:
        combined_df.to_csv('combined_df.csv', index=False)
        print('Saved combined_df.csv')
