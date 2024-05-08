def calculate_bmi(height, weight):

    bmi = weight / (height * height)

    print("Height = " + str(height))
    print("Weight = " + str(weight))
    print("bmi = ", '%.1f' % bmi)

    if bmi < 18.5:
        print("User is Under Weight ")
    elif bmi > 25.0:
        print("Over Weight")
    else:
        print("Normal Weight")



calculate_bmi(weight = 57, height = 1.73)