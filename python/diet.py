import pandas as pd
df = pd.read_excel("Fruits_Vegetables_Seeds_Nutrition_100g.xlsx")
def filter_food(category=None, nutrient=None, mode=None):
    data = df.copy()
    if category:
        data = data[data["Category"].str.lower() == category.lower()]
    if nutrient == "protein":
        col = "Protein (g)"
    elif nutrient == "calories":
        col = "Calories (kcal)"
    else:
        return []
    if mode == "max":
        data = data.sort_values(col, ascending=False)
    elif mode == "min":
        data = data.sort_values(col, ascending=True)
    data = data.head(10)
    data = data.rename(columns={
        "Food Name": "food_name",
        "Calories (kcal)": "calories",
        "Protein (g)": "protein"
    })
    return data.to_dict(orient="records")