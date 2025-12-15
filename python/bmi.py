def BMI(weight, height):
    height_m = height / 100
    bmii = weight / (height_m * height_m)
    return bmii


def BMR(weight, height, age, gender):
    if gender == 'M':
        bmr = (10 * weight) + (6.25 * height) - (5 * age) + 5
    else:
        bmr = (10 * weight) + (6.25 * height) - (5 * age) - 161
    return bmr


def BF(gender, age, bmii):
    if gender == 'M':
        bf = 1.20 * bmii + 0.23 * age - 16.2
    else:
        bf = 1.20 * bmii + 0.23 * age - 5.4
    return bf


def LBM(weight, gender, height):
    if gender == "M":
        lbm = 0.407 * weight + 0.267 * height - 19.2
    else:
        lbm = 0.252 * weight + 0.473 * height - 48.3
    return lbm


def water(weight):
    return weight * 0.033  # liters/day


def protein(weight):
    normal = 0.8 * weight
    fat_loss = 1.4 * weight
    muscle_gain = 1.95 * weight
    return normal, fat_loss, muscle_gain


def MuscleMass(lbm):
    return lbm * 0.55


def BoneMass(weight, gender):
    if gender == "M":
        return weight * 0.052
    else:
        return weight * 0.048


def calories(lbm):
    weight_loss = 22 * lbm
    muscle_gain = 40 * lbm
    maintain = 33 * lbm
    return weight_loss, muscle_gain, maintain
