from pandas_profiling import ProfileReport

import pandas as pd

df = pd.DataFrame({
    "name": ["Alice", "Bob", "Charlie", "David"],
    "age": [25, 30, 35, 40],
    "salary": [50000, 60000, 70000, 80000],
    "city": ["New York", "Los Angeles", "Chicago", "Houston"]
})

