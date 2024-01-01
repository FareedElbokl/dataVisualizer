# ECOR 1042 Lab 6 - Individual submission for histogram

# Remember to include docstring and type annotations for your functions

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Jonathan DeLeavey"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101266486"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-109"

#==========================================#
# Place your histogram function after this line
import matplotlib.pyplot as plt


def histogram(list_dict: list, key: str) -> None:
    """
    Creates a Histogram based on a list of dictionaries provided with a specified key that is present in dictionary

    Precondition: len(list_dict) >= 2


    >>> histogram([{"apple": 2, "health": 1}, {"health": 3, "apple": 2}] , "health")
    returns a graph of the health values with a return numerical value of None

    """
    y_list = []
    stu_num = []
    x_list = []
    counter = 0
    if key != 'G_Avg':
        for i in range(len(list_dict)):
            y_list.append(list_dict[i][key])
        for s in y_list:
            for b in y_list:
                if b == s:
                    counter += 1
            stu_num.append(counter)
            counter = 0

    elif key == 'G_Avg':
        for i in range(len(list_dict)):
            y_list.append(list_dict[i][key])
        for s in y_list:
            for b in y_list:
                if b == s:
                    counter += 1
            stu_num.append(counter)
            counter = 0

    x_list = y_list
    [set(x_list)]
    plt.bar(x_list, stu_num)
    plt.xlabel(key)
    plt.ylabel('Number of Students')
    plt.title("Histogram of Students")
    plt.show
    return None


# Do NOT include a main script in your submission
