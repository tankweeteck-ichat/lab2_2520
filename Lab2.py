def display_main_menu():
    print("Sub: display_main_menu")
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")


def get_user_input():
    arraylist = []
    print("Sub: get_user_input")
    numstring = input()
    numlist = numstring.split(",")
    for eachnum in numlist:
        arraylist.append(float(eachnum))
    return arraylist


def calc_average(arraylist):
    print("Sub: calc_average")
    total = sum(arraylist)
    average = total / len(arraylist)
    print("Average = ", f"{average: .2f}")
    return round(average, 2)


def find_min_max(arraylist):
    print("Sub: find_min_max")
    templist = sort_temperature(arraylist)
    min = templist[0]
    max = templist[-1]
    print("MIN = " + str(min) + " and MAX = " + str(max))
    return [min, max]


def sort_temperature(arraylist):
    print("Sub: sort_temperature")
    templist = arraylist.copy()
    templist.sort()
    print("Sort Numbers = ", templist)
    return templist


def calc_median_temperature():
    print("Sub: calc_median_temperature")



def main():
    display_main_menu()
    numArray = get_user_input()
    calc_average(numArray)
    find_min_max(numArray)
    



if __name__ == "__main__":
    main()

