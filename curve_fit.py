# ECOR 1042 Lab 6 - Individual submission for curve_fit function

# Remember to include docstring and type annotations for your functions

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Bogdan Price"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101272576"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-109"

#==========================================#
# Place your curve_fit function after this line
import numpy as np


def curve_fit(data_list: list[dict], attribute_str: str, degree_int: int):
    """Returns the equation for a curve comparing an attribute to the average grade average

    Preconditions: Only attributes with numerical values, and the attribute provided is a key in all dictionaries in the list. The degree is between 1 and 5 included

    >>>curve_fit([{'School': 'GP', 'Age': 18, 'StudyTime': 2.0, 'Failures': 0, 'Health': 3, 'Absences': 6, 'G_Avg': 6.2}, {'School': 'GP', 'Age': 17, 'StudyTime': 2.0, 'Failures': 0, 'Health': 3, 'Absences': 4, 'G_Avg': 4.3}, {'School': 'GP', 'Age': 15, 'StudyTime': 2.0, 'Failures': 3, 'Health': 3, 'Absences': 10, 'G_Avg': 5.6}], 'Age', 2)
    '0.85x^2+-27.85x+232.1'
    """

    values_list = [entry['G_Avg'] for entry in data_list]
    keys_list = [entry[attribute_str] for entry in data_list]
    new_data_list = []

    for i in range(len(values_list)):
        new_data_list.append({keys_list[i]: values_list[i]})

    grouped_data_dict = {}
    for data_dict in new_data_list:
        for key, value in data_dict.items():
            if key in grouped_data_dict:
                grouped_data_dict[key].append(value)
            else:
                grouped_data_dict[key] = [value]

    avg_data_dict = {}
    for key, value in grouped_data_dict.items():
        avg_data_dict[key] = sum(value) / len(value)

    x_list = list(avg_data_dict.keys())
    y_list = list(avg_data_dict.values())
    result_str = ""

    if len(x_list) > degree_int + 1:
        poly_degree_int = degree_int
    else:
        poly_degree_int = len(x_list) - 1

    coefficients_list = np.polyfit(x_list, y_list, poly_degree_int)
    order_int = len(coefficients_list) - 1

    for coefficient in coefficients_list:
        if order_int == 1:
            result_str += str(round(coefficient, 2)) + "x" + "+"
        elif order_int > 1:
            result_str += str(round(coefficient, 2)) + \
                "x" + "^" + str(order_int) + "+"
        else:
            result_str += str(round(coefficient, 2))
        order_int -= 1

    return result_str
# Do NOT include a main script in your submission
