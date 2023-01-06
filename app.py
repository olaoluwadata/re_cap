import pandas pd
from app.py import add_column

df = pd.read_csv("Data.csv")

new_col =add_column(df["Company_size"],df.Training_hours)
