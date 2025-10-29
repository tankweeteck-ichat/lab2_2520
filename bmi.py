def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    bmi = weight/(height**2)
    print("BMI = ", f"{bmi: .2f}")
    if bmi<18.5:
        print("Under Weight")
    elif bmi>25.0:
        print("Over Weight")
    else:
        print("Normal Weight")


calculate_bmi(weight=37, height=1.73)
calculate_bmi(weight=57, height=1.73)
calculate_bmi(weight=97, height=1.73)
