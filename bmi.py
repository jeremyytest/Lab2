def calculate_bmi(height, weight):

    bmi = weight / (height * height)

    print("Height = " + str(height))
    print("Weight = " + str(weight))
    print("bmi = ", '%.1f' % bmi)

    if bmi < 18.5:
        return -1
        #print("User is Under Weight ")
    elif bmi > 25.0:
        return 1
        #print("Over Weight")
    else: 
        return 0
        #print("Normal Weight")

def main():
    calculate_bmi(weight = 57, height = 1.73)
    
if __name__ == "__main__":
    main()