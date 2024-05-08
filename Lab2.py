import statistics

def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")

def get_user_input():
    numbers = input()
    split_numbers = numbers.split(", ") #split_numbers is a string list
    float_numbers = [float(i) for i in split_numbers] #for every element in split_numbers, convert to float 

    return float_numbers

def calc_average(num_list):
    length = len(num_list)
    summation = sum(num_list)
    average = summation / length #don't need typecast since sum is in float 
    return average

def find_min_max(num_list):
    minimum = min(num_list)
    maximum = max(num_list)
    minmax_list = [minimum, maximum]

    return minmax_list

def sort_temperature(num_list):
    sorted = num_list 
    sorted.sort()
    return sorted


def calc_median_temperature(sorted_list):
    median = statistics.median(sorted_list)
    return median

def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_list = get_user_input() #list is in float
    mean = calc_average(num_list)
    min_and_max = find_min_max(num_list)
    sorted_list = sort_temperature(num_list)
    median = calc_median_temperature(sorted_list)

    print("Mean is :", mean)
    print("Min and Max is :", min_and_max)
    print("Median is :", median)

if __name__ == "__main__":
    main()