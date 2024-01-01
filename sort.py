# ECOR 1042 Lab 5 - Team submission
# Remember to include docstring and type annotations for your functions

# Update "" to list all students contributing to the team work
__author__ = "Fareed El Bokl, Rayvel Arjoon, Jonathan DeLeavey, Bogdan Price"

# Update "" with your team (e.g. T102)
__team__ = "T109"

#==========================================#
# Place your sort_students_age_bubble function after this line


def sort_students_age_bubble(l1: list, order: str) -> list:
    """Return the specified list of dictionaries in descending or ascending order based on the Age value in the dictionaries. If no 'Age' key in dictionaries, original list is returned.

    >>>sort_students_age_bubble(
     [{"Age":10,"School":"GP"},{"Age":19,"School":"MS"}], "D")
    [{"Age": 19, "School":"MS"}, {"Age":10, "School":"GP"}]

    >>> sort_students_age_bubble([{"School":"GP"}, {"School":"MS"}], "D")
    "Age" key is not present.
    [{"School":"GP"}, {"School":"MS"}]
    """

    if "Age" not in l1[0]:
        print('"Age" key is not present.')
        return l1

    if order == "A":
        indexing_length = len(l1) - 1
        sort_status = False

        while not sort_status:
            sort_status = True
            for i in range(0, indexing_length):
                if l1[i]["Age"] > l1[i + 1]["Age"]:
                    sort_status = False
                    l1[i], l1[i + 1] = l1[i + 1], l1[i]
        return l1
    elif order == "D":
        indexing_length = len(l1) - 1
        sort_status = False

        while not sort_status:
            sort_status = True
            for i in range(0, indexing_length):
                if l1[i]["Age"] < l1[i + 1]["Age"]:
                    sort_status = False
                    l1[i], l1[i + 1] = l1[i + 1], l1[i]
        return l1

#==========================================#
# Place your sort_students_time_selection function after this line


def sort_students_time_selection(students: list[dict], order: str) -> list[dict]:
    """Given a list of dictionaries, the function returns them in order of ascending or descending study times

    Preconditions: order must be A or D

    >>> sort_students_time_selection ( [{"StudyTime":10.2,"School":"GP"}, {"StudyTime":19.1,"School":"MS"}], "D")
    [{"StudyTime": 19.1, "School":"MS"}, {"StudyTime":10.2, "School":"GP"}]

    >>>sort_students_time_selection([{"School":"GP"},{"School":"MS"}], "D")
    "StudyTime" key is not present
    [{"School":"GP"}, {"School":"MS"}]
    """
    # Checks every dictionary for a "StudyTime" key
    for k in range(len(students)):
        if students[k].get("StudyTime") == None:
            print('"StudyTime" key is not present')
            return students

    # Goes through the selection sorting algorithm in ascending order
    if order == "A":
        for i in range(len(students)):
            min = i
            for j in range(i + 1, len(students)):
                if students[min].get("StudyTime") > students[j].get("StudyTime"):
                    min = j
            students[i], students[min] = students[min], students[i]
        return students

    # Goes through the selection sorting algorithm in descending order
    elif order == "D":
        for i in range(len(students)):
            max = i
            for j in range(i + 1, len(students)):
                if students[max].get("StudyTime") < students[j].get("StudyTime"):
                    max = j
            students[i], students[max] = students[max], students[i]
        return students


#==========================================#
# Place your sort_students_g_avg_insertion function after this line
def sort_students_g_avg_insertion(l1: list, order: str) -> list:
    """
    Uses the insertion sorting algorithm to sort the students in the list (dicts) in ascending, or descending order (order).

    Preconditions:
    order must be 'A' or 'D' for ascending or descending

    Examples
    >>> sort_students_g_avg_insertion( [{"G_Avg":7.2,"School":"GP"},
    {"G_Avg":9.1,"School":"MS"}], "D")
    [{"G_Avg": 9.1, "School":"MS"}, {"G_Avg":7.2, "School":"GP"}]

    >>> sort_students_g_avg_insertion([{"School":"GP"},{"School":"MS"}], "D")
    "G_Avg" key is not present"
    [{"School":"GP"}, {"School":"MS"}]
    """

    if "G_Avg" not in l1[0]:
        print('"G_Avg" key is not present')
        return l1

    if order == "A":
        indexing_length = range(1, len(l1))
        for i in indexing_length:
            value_to_sort = l1[i]["G_Avg"]

            while l1[i - 1]["G_Avg"] > value_to_sort and i > 0:
                l1[i], l1[i - 1] = l1[i - 1], l1[i]
                i = i - 1
        return l1

    elif order == "D":
        indexing_length = range(1, len(l1))
        for i in indexing_length:
            value_to_sort = l1[i]["G_Avg"]

            while l1[i - 1]["G_Avg"] < value_to_sort and i > 0:
                l1[i], l1[i - 1] = l1[i - 1], l1[i]
                i = i - 1
        return l1


#==========================================#
# Place your sort_students_failures_bubble function after this line
def sort_students_failures_bubble(dictionaries: list, order: str) -> list:
    """
    returns a sorted list of dictionaries based on the student failures value, either in ascending or descending order

    Preconditions: len(dictionaries) >= 2 

    >>>sort_students_failures_bubble([{"Failures":10,"School":"GP"},{"Failures":19,"School":"MS"}], "D")
    [{'Failures': 19, 'School': 'MS'}, {'Failures': 10, 'School': 'GP'}]


    >>>sort_students_failures_bubble([{"School":"GP"},{"School":"MS"}],"D")
    "Failures" key is not present.
    [{'School': 'GP'}, {'School': 'MS'}]
    """
    failure_number = 0
    for b in dictionaries:
        for n in b:
            if n == "Failures":
                failure_number += 1
    if failure_number == len(dictionaries):

        swap = True
        if order == "A":
            while swap:
                swap = False
                for i in range(len(dictionaries) - 1):
                    if dictionaries[i]["Failures"] > dictionaries[i + 1]["Failures"]:
                        swapper = dictionaries[i]
                        dictionaries[i] = dictionaries[i + 1]
                        dictionaries[i + 1] = swapper
                        swap = True
        if order == "D":
            while swap:
                swap = False
                for i in range(len(dictionaries) - 1):
                    if dictionaries[i]["Failures"] < dictionaries[i + 1]["Failures"]:
                        swapper = dictionaries[i]
                        dictionaries[i] = dictionaries[i + 1]
                        dictionaries[i + 1] = swapper
                        swap = True
    else:
        print('"Failures" key is not present.')
        return (dictionaries)

    return dictionaries


#==========================================#
# Place your sort function after this line
def sort(l1: list, order: str, data: str) -> list:
    """Return sorted list from original list, in descending or ascending order based on the specified data.

    >>>sort([{"Age":10,"School":"GP"},{"Age":19.1,"School":"MS"}],"D","Age")
    [{"Age": 19, "School":"MS"}, {"Age":10, "School":"GP"}]

    >>>sort([{"School":"GP"},{"School":"MS"}], "D", "School")
    Cannot be sorted by "School"
    [{"School":"GP"}, {"School":"MS"}]
    """

    if data == "Age":
        return sort_students_age_bubble(l1, order)
    elif data == "StudyTime":
        return sort_students_time_selection(l1, order)
    elif data == "G_Avg":
        return sort_students_g_avg_insertion(l1, order)
    elif data == "Failures":
        return sort_students_failures_bubble(l1, order)
    else:
        print(f'Cannot be sorted by "{data}"')
        return l1


# Do NOT include a main script in your submission
