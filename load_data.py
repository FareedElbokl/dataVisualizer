# ECOR 1042 Lab 3 - Team submission
# Remember to include docstring and type annotations for your functions

# Update "" to list all students contributing to the team work
__author__ = "Jonathan DeLeavey, Fareed El Bokl, Bogdan Price, Rayvel Arjoon"

# Update "" with your team (e.g. T102)
__team__ = "T109"

#==========================================#
# Place your student_school_list function after this line


def student_school_list(file: str, school: str) -> list[dict]:
    """Returns a list dictionaries corresponding to each student that attended the school provided as an input.

    Preconditions: none

    >>>student_school_list('student-mat.csv', 'GP')
    [{'Age': 18, 'StudyTime': 2.0, 'Failures': 0, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6 },
    {another element},
    …
    ]
    """
    students = []
    count = 0
    infile = open(file, "r")
    for line in infile:
        if count > 0:
            student = line.split(",")  # find out how to remove \n
            if student[0] == school:
                students.append({"Age": int(student[1]), "StudyTime": float(student[2]), "Failures": int(student[3]), "Health": int(
                    student[4]), "Absences": int(student[5]), "G1": int(student[6]), "G2": int(student[7]), "G3": int(student[8])})
        count += 1
    infile.close()
    return students


#==========================================#
# Place your student_health_list function after this line
def student_health_list(filename: str, n: int) -> list:
    """
    Returns a list of students whose health is equal to a specified value

    Preconditions: 0 <= n <= 5

    >>> student_health_list('student-mat.csv', 3)
    [{'School': 'GP', 'Age': 15, 'StudyTime': 3.0, 'Failures': 0, 'Absences': 4, 'G1': 10, 'G2': 12, 'G3': 12}, {additional elements},
    ...
    """
    student_list = []
    with open(filename)as health_file:
        counter = 0
        for line in health_file:
            if counter > 0:
                student_data = line.split(",")
                if int(student_data[4]) == n:
                    directory = {'School': student_data[0], 'Age': int(student_data[1]), 'StudyTime': float(student_data[2]), 'Failures': int(
                        student_data[3]), 'Absences': int(student_data[5]), 'G1': int(student_data[6]), 'G2': int(student_data[7]), 'G3': int(student_data[8])}
                    student_list.append(directory)
            counter += 1

    return(student_list)


#==========================================#
# Place your student_age_list function after this line
def student_age_list(f: str, specified_age: int) -> list:
    """Returns data in the form of a list of students of the specified age from the
    file.

    >>>student_age_list("student-mat.csv", 15)
    [ {'School': 'GP', 'StudyTime': 4.2, 'Failures': 3, 'Health': 3, 'Absences': 6,
        'G1': 7, 'G2': 8, 'G3': 10},
    {another element},
      …
    ]
    """
    ages = []
    with open(f) as file:
        counter_1 = 0
        for line in file:
            if counter_1 > 0:
                columns = line.strip().split(",")
                age = int(columns[1])
                if age == specified_age:
                    diction = {"School": columns[0], "StudyTime": float(columns[2]), 'Failures': int(columns[3]),
                               "Health": int(columns[4]), "Absences": int(columns[5]), "G1": int(columns[6]), "G2": int(columns[7]), "G3": int(columns[8])}
                    ages.append(diction)
            counter_1 += 1
    return ages

#==========================================#
# Place your student_failures_list function after this line


def student_failures_list(filename: str, failures: int) -> dict:
    """
    Returns the students with the same number of failures that was entered (failures) from the file specified (filename).

    Preconditions: 
    filename must exist
    failures >= 0

    Examples:
    >>> student_failures_list('student-mat.csv', 0)
    [{'School': 'GP', 'Studytime': '2', 'Failures': '0', 'Health': '3', 'Absences': '6', 'G1': '5', 'G2': '6', 'G3': '6'}, {another element}]

    >>> student_failures_list('student-mat.csv', 2)
    [{'School': 'GP', 'Age': '16', 'StudyTime': '1', 'Failures': '2', 'Health': '5', 'Absences': '14', 'G1': '6', 'G2': '9', 'G3': '8'}, {another element}]
    """

    # creates a dictionary of students with the same number of failures as the entered quantity
    failures_list = []
    # open the file and set file read mode
    with open(filename, 'r') as file:
        rows = file.readlines()

    # removes commas and turns the row in the csv file into a list with commas seperating each header
    header = rows[0].strip().split(',')
    dict_list = []

    # read through the file
    for row in rows[1:]:
        # seperate values with a comma in to a row dictionary row_dict
        values = row.strip().split(',')
        row_dict = {}

        # sets the values for the dictionary here
        for i in range(len(header)):
            row_dict[header[i]] = values[i]

        # adds the dictionaries to the list
        dict_list.append(row_dict)

    # looks at every student in the file
    for student in dict_list:
        # checks if the number of failures of the student matches the search quantity
        if student.get('Failures') == str(failures):
            # converts values to acceptable types and removes failures
            student.pop('Failures')
            student['Age'] = int(student.get('Age'))
            student['StudyTime'] = float(student.get('StudyTime'))
            student['Health'] = int(student.get('Health'))
            student['Absences'] = int(student.get('Absences'))
            student['G1'] = int(student.get('G1'))
            student['G2'] = int(student.get('G2'))
            student['G3'] = int(student.get('G3'))

            # saves that student to the list
            failures_list.append(student)

    return failures_list


#==========================================#
# Place your load_data function after this line
def load_data(file_name: str, values: tuple) -> list:
    """Return data based on the users choice through the specified file name and
    the values they pass through.

    >>>load_data('student-mat.csv', (‘Failures’, 0))
    [ {'School': 'GP', 'Age': 18, 'StudyTime': 6.7, 'Health': 3,
        'Absences': 7, 'G1': 12, 'G2': 13, 'G3': 14},
      {another element},
      …
    ] 
    """

    if values[0] == "All":
        data = []
        with open(file_name) as file:
            counter = 0
            for line in file:
                if counter > 0:
                    columns = line.strip().split(",")
                    diction = {"School": columns[0], "Age": int(columns[1]), "StudyTime": float(columns[2]), 'Failures': int(columns[3]),
                               "Health": int(columns[4]), "Absences": int(columns[5]), "G1": int(columns[6]), "G2": int(columns[7]), "G3": int(columns[8])}
                    data.append(diction)
                counter += 1
            return data

    elif values[0] == "Failures":
        return student_failures_list(file_name, values[1])
    elif values[0] == "Age":
        return student_age_list(file_name, values[1])
    elif values[0] == "Health":
        return student_health_list(file_name, values[1])
    elif values[0] == "School":
        return student_school_list(file_name, values[1])
    else:
        print("Invalid Value")
        return []


#==========================================#
# Place your add_average function after this line
def add_average(l1: list) -> list:
    """Return a list containing student data in the form of dictionaries with 
    the student's grade average being displayed along with their three grades.

    >>> add_average([ {'School': 'GP', 'Age': 18, 'StudyTime': 6.7,
                        'Failures': 1, 'Health': 3, 'Absences': 7,
                        'G1': 5, 'G2': 6, 'G3': 6},
                       {another element},
                         … ] )
    [  {'School': 'GP', 'Age': 18, 'StudyTime': 6.7, 'Failures': 1,
         'Health': 3, 'Absences': 7, 'G1': 5, 'G2': 6, 'G3': 6,
         'G_Avg': 5.67 },
      {another element}
    …
    ]
    """
    total = 0
    divisor = 3
    grades = ["G1", "G2", "G3"]
    for dictionary in l1:
        total = 0
        for grade in grades:
            total += int(dictionary[grade])
        average = total / divisor
        dictionary["G_Avg"] = round(average, 2)
    return l1


# Do NOT include a main script in your submission
