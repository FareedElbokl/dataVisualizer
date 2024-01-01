# ECOR 1042 Lab 6 - Individual submission for text_UI

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Rayvel Arjoon"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101258313"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-109"

#==========================================#
# Place your script for your text_UI after this line
from load_data import *
from sort import *
from histogram import *
from curve_fit import *


def get_selection() -> str:
    # dijsplay the menu and
    selection = input(
        """
        L)oad Data
        S)ort Data
        C)urve Fit
        H)istogram
        E)xit
        Please type your command ----> """
    )
    return selection.lower()

# checks if the data was loaded


def is_data_loaded(data: list) -> bool:
    if len(data) == 0:
        # the data was not loaded
        return False
    else:
        # the data was loaded
        return True


if __name__ == "__main__":
    # variables
    again = True
    loaded_data = []

    # loops until program ends
    while again:
        # get the program choice or exit choice
        program = get_selection()

        # checks which program the user wants to use
        if program == "l":
            # load data
            # get the filename
            filename = input("Please enter the name of the file\n----> ")

            # get the filter attribute
            attribute = input(
                "Please enter the attribute to use as a filter\n----> ")
            attribute = attribute.capitalize()

            # checks which attribute was entered
            if attribute == "All":
                # user entered "all"
                # load the data
                loaded_data = load_data(filename, ("All", None))
                loaded_data = add_average(loaded_data)
                print("Data loaded")

            elif attribute == "School":
                # get attribute value
                value = input("Please enter the attribute value\n----> ")
                data = (attribute, value)

                # load the data
                loaded_data = load_data(filename, data)
                loaded_data = add_average(loaded_data)
                print("Data loaded")

            elif attribute == "Age":
                # get attribute value
                value = int(
                    input("Please enter the attribute value\n----> "))
                data = (attribute, value)

                # load and display data
                loaded_data = load_data(filename, data)
                loaded_data = add_average(loaded_data)
                print("Data loaded")
                print

            elif attribute == "Health":
                # get the attribute value
                value = input("Please enter the attribute value\n----> ")
                data = (attribute, value)

                # load and display data
                loaded_data = load_data(filename, data)
                loaded_data = add_average(loaded_data)
                print("Data loaded")

            elif attribute == "Studytime":
                # get the attribute value
                value = float(
                    input("Please enter the attribute value\n----> "))
                data = (attribute, value)

                # load and display data
                loaded_data = load_data(filename, data)
                loaded_data = add_average(loaded_data)
                print("Data loaded")

            elif attribute == "Failures":
                # get the attribute value
                value = int(
                    input("Please enter the attribute value\n----> "))
                data = (attribute, value)

                # load and display data
                loaded_data = load_data(filename, data)
                loaded_data = add_average(loaded_data)
                print("Data loaded")

            else:
                # invalid input
                print("Invalid attribute")

        elif program == "s":
            # sort data
            if not is_data_loaded(loaded_data):
                print("File not loaded. Please, load a file first.")
                continue

            # get the sorting attribute
            attribute = input(
                """
            Please enter the attribute you want to use for sorting:
            'Age'\t'StudyTime'\t'Failures'\t'G_Avg'
            ----> """)
            if attribute[0] == "G" or attribute[0] == "g":
                attribute = "G_Avg"
            elif attribute[0] == "S" or attribute[0] == "s":
                attribute = "StudyTime"
            else:
                attribute = attribute.capitalize()

            # list of valid attributes
            valid_attributes = ('Age', 'StudyTime', 'Failures', 'G_Avg')
            invalid = True

            # checks if the attribute is valid
            for i in valid_attributes:
                if i == attribute:
                    invalid = False

            if invalid:
                print("Invalid attribute")
                continue

            # get the order for the data to be ordered
            order = input("Ascending (A) or Descending (D) order?\n----> ")
            order = order.upper()

            # sort the data
            data = sort(loaded_data, order, attribute)

            # check if the user wants to display the data
            display = input(
                "Data Sorted. Do you want to display the data?\n----> ")
            display = display.lower()

            # checks if the data should be displayed
            if display == 'y':
                print(data)

            # check which attribute was entered
        elif program == "c":
            # curve fit
            # check if the data was loaded
            if not is_data_loaded(loaded_data):
                print("File not loaded. Please load a file first")
                continue

            # get the plotting attribute
            attribute = input(
                "Please enter the attribute you want to use to find the best fit for G_Avg\n----> ")
            if "study" in attribute or "Study" in attribute:
                attribute = "StudyTime"
            else:
                attribute = attribute.capitalize()

            # get the polynomial higest order
            poly_order = int(
                input("Please enter the order of the polynomial to be fitted\n----> "))

            # display the equation of the polynomial
            print(curve_fit(loaded_data, attribute, poly_order))

        elif program == "h":
            # histogram
            # check if the data was loaded
            if not is_data_loaded(loaded_data):
                print("File not loaded. Please load a file first")
                continue

            # get the plotting attribute
            attribute = input(
                "Please enter the attribute you want to use for plotting\n----> ")
            if "study" in attribute or "Study" in attribute:
                attribute = "StudyTime"
            elif attribute[0] == "G" or attribute[0] == "g":
                attribute = "G_Avg"
            else:
                attribute = attribute.capitalize()

            # displays the histogram
            histogram(loaded_data, attribute)
        elif program == 'e':
            # exit
            again = False
        else:
            # invalid command
            print("Invalid command\n")
            again = True




