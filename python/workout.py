import pandas as pd
df=pd.read_excel("exercise.xlsx")
def CB(gender, weight, height, age, mm, bf, bd):
    if gender == "M":
        caloriesburn = ((10 * weight) + (6.25 * height) - (5 * age) + 5) \
                        + (20 * mm) - (15 * bf) + bd
    else:
        caloriesburn = ((10 * weight) + (6.25 * height) - (5 * age) - 161) \
                        + (20 * mm) - (15 * bf) + bd
    return round(caloriesburn, 2)

def workout_M(select,rcb):
    col= "Calories Burned 30 min"
    col1="Type"
    if select=="FL":
        target_cal = rcb - 400
    elif select=="M":
        target_cal = rcb
    else:
        target_cal = rcb + 300
    return target_cal
def workout_did(select):
    col = "Calories Burned 30 min"
    col1 = "Type"

    if select == "FL":
        data = df.sort_values(col, ascending=False)
    elif select == "M":
        data = df.sort_values(col, ascending=True)
    else:
        data = df[df[col1] == "Strength"].sort_values(by=col, ascending=True)
    data = data.head(10)
    data = data.rename(columns={
        "Calories Burned 30 min": "cal_30",
        "Main Purpose": "main_purpose",
        "Secondary Benefits": "secondary_benefits"
    })

    return data.to_dict(orient="records")