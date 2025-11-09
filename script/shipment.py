import pandas as pd
import os

folder_path = "data/raw"
output_folder = "data/cleaned"
os.makedirs(output_folder, exist_ok=True)

shipment_path = os.path.join(folder_path, "MSY Data - Shipment.csv")

if os.path.exists(shipment_path):
    df_ship = pd.read_csv(shipment_path, encoding="utf-8")
    
    output_path = os.path.join(output_folder, "Shipment_Data.xlsx")
    df_ship.to_excel(output_path, index=False)
    
    print(f"output：{output_path}")
else:
    print("can't find Shipment")