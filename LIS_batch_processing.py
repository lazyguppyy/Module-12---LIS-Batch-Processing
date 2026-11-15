#MODULE 12: LIS Batch Processing
#author: Logan Grisby
#assignment: write a Python script that performs batch processing on a set of library records

#load the dataset into pandas
import pandas as pd
df = pd.read_csv("library_batch_data_raw.csv")
df.head()

#update publication years to a standardized format
df["Publication Year"] = (
  df["Publication Year"]
  .astype(str)
  .str.extract(r"(\d{4})")
  .astype("Int64")
)

#add a new column indicating the resource type of your choice (e.g., book, journal)
df["Resource Type"] = "Book"

#identify and report duplicate entries
duplicates = df[df.duplicated()]
print(duplicates)
print()

#summary report
summary = {
  "Total Records": len(df),
  "Unique Titles": df["Title"].nunique(),
  "Duplicates Found": duplicates.shape[0],
  "Number of Resource Types": df["Resource Type"].value_counts().to_dict()
}

print(summary, "\n")

#save the processed dataset
df.to_csv("library_batch_data_cleaned.csv", index=False)
