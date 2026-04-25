import pandas as pd

dataset_path = "indian_railway_delay_data_.csv"

df = pd.read_csv(dataset_path)

top_2_train_nos = df["Train_no"].value_counts().nlargest(2).index

df_filtered = df[df["Train_no"].isin(top_2_train_nos)].copy()

df_filtered["Total_Delay_Minutes"] = (
    pd.to_timedelta(df_filtered["Dealy_min"]).dt.total_seconds() / 60
)

print(f"Kept Trains: {list(top_2_train_nos)}")
print(f"New shape: {df_filtered.shape}")
print(df_filtered[["Train_name", "Dealy_min", "Total_Delay_Minutes"]])


df_filtered.to_csv("filtered.csv")
