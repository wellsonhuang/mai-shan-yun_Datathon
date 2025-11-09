import pandas as pd
import os
import re

folder_path = "data/raw"
output_folder = "data/cleaned"
os.makedirs(output_folder, exist_ok=True)

month_dict = {
    "May": "2025-05-01",
    "June": "2025-06-01",
    "July": "2025-07-01",
    "August": "2025-08-01",
    "September": "2025-09-01",
    "October": "2025-10-01",
    "November": "2025-11-01",
    "December": "2025-12-01"
}

df_group_all = pd.DataFrame()
df_category_all = pd.DataFrame()
df_item_all = pd.DataFrame()

files = [f for f in os.listdir(folder_path) if f.endswith(".xlsx") and "MSY Data" not in f]

for file_name in files:
    print(f"working on ：{file_name}")

    match = re.search(r"(May|June|July|August|September|October|November|December)", file_name)
    if not match:
        print(f"pass：{file_name}")
        continue

    month_name = match.group(1)
    month_date = pd.to_datetime(month_dict[month_name], format="%Y-%m-%d")
    file_path = os.path.join(folder_path, file_name)

    try:
        df_group = pd.read_excel(file_path, sheet_name="data 1")
        df_category = pd.read_excel(file_path, sheet_name="data 2")
        df_item = pd.read_excel(file_path, sheet_name="data 3")
    except Exception as e:
        print(f"can't read {file_name} {e}")
        continue

    for df in [df_group, df_category, df_item]:
        df["Month"] = month_date         
        df["Month_Label"] = month_name   

    df_group_all = pd.concat([df_group_all, df_group], ignore_index=True)
    df_category_all = pd.concat([df_category_all, df_category], ignore_index=True)
    df_item_all = pd.concat([df_item_all, df_item], ignore_index=True)

output_path = os.path.join(output_folder, "AllMonths_Data.xlsx")
with pd.ExcelWriter(output_path, engine="openpyxl", date_format="YYYY-MM-DD") as writer:
    df_group_all.to_excel(writer, sheet_name="Group", index=False)
    df_category_all.to_excel(writer, sheet_name="Category", index=False)
    df_item_all.to_excel(writer, sheet_name="Item", index=False)

print(f"output: {output_path}")