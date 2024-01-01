# ECOR 1042 Lab 6 - Individual submission for batch_UI

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Fareed El Bokl"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101256495"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-109"

#==========================================#
# Place your script for your batch_UI after this line
import load_data
import sort
import histogram
import curve_fit

if __name__ == "__main__":
    exit = False

    while not exit:
        user_file = input(
            "Please enter the name of the file where your commands are stored: ")

        with open(user_file) as file:
            for line in file:

                line_data = line.strip().split(";")
                action = line_data[0].upper()

                if action == "L":
                    file_name = line_data[1]
                    attribute = line_data[2]

                    if attribute != "All":
                        attribute_val = line_data[3]
                        if attribute != "School":
                            if attribute == "StudyTime":
                                attribute_val = float(attribute_val)
                            else:
                                attribute_val = int(attribute_val)

                    if attribute == "All":
                        values = (attribute, 0)
                    else:
                        values = (attribute, attribute_val)

                    data = load_data.load_data(file_name, values)
                    data = load_data.add_average(data)
                    print("Data Loaded")

                elif action == "S":
                    data_to_sort = data
                    order = line_data[2]
                    attribute = line_data[1]
                    choice_display = line_data[3].upper()

                    sorted_data = sort.sort(data_to_sort, order, attribute)
                    if choice_display == "Y":
                        print(f"Data Sorted. {sorted_data}")
                    elif choice_display == "N":
                        print("Data Sorted.")

                elif action == "H":
                    plotting_attribute = line_data[1]
                    data_to_plot = data
                    histogram.histogram(data_to_plot, plotting_attribute)

                elif action == "C":
                    data_to_plot = data
                    attribute = line_data[1]
                    poly_order = int(line_data[2])
                    print(curve_fit.curve_fit(
                        data_to_plot, attribute, poly_order))

                elif action == "E":
                    exit = True












