import numpy as np
import pandas as pd

df = pd.read_csv("filtered.csv")

target_rows = 1000
repeats = target_rows // len(df)

df_synthetic = pd.concat([df] * repeats, ignore_index=True)

noise_minutes = np.random.normal(0, 15, size=len(df_synthetic))  # Std dev of 15 mins
df_synthetic["Total_Delay_Minutes"] = (
    df_synthetic["Total_Delay_Minutes"] + noise_minutes
)

df_synthetic["Total_Delay_Minutes"] = df_synthetic["Total_Delay_Minutes"].clip(lower=0)

days_offset = np.random.randint(-10, 10, size=len(df_synthetic))
df_synthetic["Date"] = pd.to_datetime(df_synthetic["Date"]) + pd.to_timedelta(
    days_offset, unit="D"
)

if "Unnamed: 0" in df_synthetic.columns:
    df_synthetic = df_synthetic.drop(columns=["Unnamed: 0"])

df_synthetic.to_csv("synthetic_railway_data.csv", index=False)

print(f"Success! Generated {len(df_synthetic)} rows.")
print(df_synthetic[["Train_name", "Date", "Total_Delay_Minutes"]].head(10))
