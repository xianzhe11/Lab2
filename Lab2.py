def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")

    display()
    num_list = get_user_input()

    average = calc_average_temperature(num_list)
    minMaxList = calc_min_max_temperature(num_list)

    print("Average =" + str(average))
    print("Min Temperature =" + str(minMaxList[0]))
    print("Max Temperature =" + str(minMaxList[1]))
    print(str(minMaxList))

def display():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)") 

def get_user_input():
    print("Enter the temperature values")
    x = input()
    inputs = x.split(",")
    listOfFloat = list(map(float, inputs))

    return listOfFloat


def calc_average_temperature(listOfValues):
    avg = sum(listOfValues) / len(listOfValues)
    return avg
    
def calc_min_max_temperature(listOfValues):
    listOfValues.sort()

    maxTemp = listOfValues[-1]
    minTemp = listOfValues[0]

    integerList = [minTemp, maxTemp]
    return integerList

if __name__ == "__main__":
    main()