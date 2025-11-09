import pandas as pd
import os

folder_path = "data/raw"
output_folder = "data/cleaned"
os.makedirs(output_folder, exist_ok=True)

ingredient_path = os.path.join(folder_path, "MSY Data - Ingredient.csv")
if os.path.exists(ingredient_path):
    df_ing = pd.read_csv(ingredient_path, encoding="utf-8") 
    df_ing.to_excel(os.path.join(output_folder, "Ingredient_Data.xlsx"), index=False)
    print("output : Ingredient_Data.xlsx")
else:
    print("can't find")