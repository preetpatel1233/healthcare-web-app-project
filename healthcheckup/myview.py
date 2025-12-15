from django.http import HttpResponse
from django.shortcuts import render
from python import bmi
from python import diet
from python import workout
# from python import workout
def homepage(request):
    return render(request,"index.html")
def bmi_page(request):
    data={}
    try:
        if request.method=="POST":
            height=int(request.POST.get('height'))
            weight=int(request.POST.get('weight'))
            age=int(request.POST.get('age'))
            gender=request.POST.get('gender')
            bbmi=bmi.BMI(weight,height)
            bbmr=bmi.BMR(weight, height, age, gender)
            bbf=bmi.BF(gender,age,bbmi)
            lbbm=bmi.LBM(weight, gender, height)
            ww=bmi.water(weight)
            pp=bmi.protein(weight)
            mmm=bmi.MuscleMass(lbbm)
            bmm=bmi.BoneMass(weight, gender)
            cc=bmi.calories(lbbm)
            data={
                'bmi':bbmi,
                'bf':bbf,
                'mm':mmm,
                'bd':bmm,
                'c':cc,
                'w':ww,
                'p':pp
            }
    except:
        pass
    return render(request, 'bmi.html',data)
def Diet_page(request):
    result = []

    if request.method == "POST":
        category = request.POST.get("category")
        nutrient = request.POST.get("nutrient")
        mode = request.POST.get("mode")

        # Treat empty category as None
        if category == "":
            category = None

        # Call filtering function
        if nutrient and mode:
            result = diet.filter_food(
                category=category,
                nutrient=nutrient,
                mode=mode
            )

    return render(request, "diet.html", {
        "result": result
    })
def workout_page(request):
    data = {}

    if request.method == "POST":
        height = int(request.POST.get('height'))
        weight = int(request.POST.get('weight'))
        age = int(request.POST.get('age'))
        gender = request.POST.get('gender')
        select = request.POST.get('type')

        bbmi = bmi.BMI(weight, height)
        bbf = bmi.BF(gender, age, bbmi)
        lbbm = bmi.LBM(weight, gender, height)
        mmm = bmi.MuscleMass(lbbm)
        bmm = bmi.BoneMass(weight, gender)

        cb = workout.CB(gender, weight, height, age, mmm, bbf, bmm)
        target = workout.workout_M(select, cb)
        did = workout.workout_did(select)

        data = {
            "cb": cb,
            "T": target,
            "D": did
        }

    return render(request, 'workout.html', data)
def aboutme(request):
    return render(request,'aboutus.html')