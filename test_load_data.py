# ECOR 1042 Lab 4 - team submission

# import check module here
import check
# import load_data module here
import load_data
# Update "" with your the name of the active members of the team
__author__ = "Fareed El Bokl, Rayvel Arjoon, Jonathan DeLeavey, Bogdan Price"

# Update "" with your student number (e.g., 100100100)

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-109"

#==========================================#

# Place test_return_list function here


def test_return_list():
    # Complete the function with your test cases

    # test that student_school_list returns a list (3 different test cases required)
    check.equal(isinstance(load_data.student_school_list(
        "student-test.csv", "GP"), list), True)
    check.equal(isinstance(load_data.student_school_list(
        "student-test.csv", "MB"), list), True)
    check.equal(isinstance(load_data.student_school_list(
        "student-test.csv", "not a school"), list), True)
    # test that student_age_list returns a list (3 different test cases required)
    check.equal(isinstance(load_data.student_age_list(
        "student-test.csv", 18), list), True)
    check.equal(isinstance(load_data.student_age_list(
        "student-test.csv", 22), list), True)
    check.equal(isinstance(load_data.student_age_list(
        "student-test.csv", 11), list), True)
    # test that student_health_list returns a list (3 different test cases required)
    check.equal(isinstance(load_data.student_health_list(
        "student-test.csv", 3), list), True)
    check.equal(isinstance(load_data.student_health_list(
        "student-test.csv", 5), list), True)
    check.equal(isinstance(load_data.student_health_list(
        "student-test.csv", 11), list), True)

    # test that student_failures_list returns a list (3 different test cases required)
    check.equal(isinstance(load_data.student_failures_list(
        "student-test.csv", 0), list), True)
    check.equal(isinstance(load_data.student_failures_list(
        "student-test.csv", 15), list), True)
    check.equal(isinstance(load_data.student_failures_list(
        "student-test.csv", 2), list), True)
    # test that load_data returns a list (6 different test cases required)
    check.equal(isinstance(load_data.load_data(
        "student-test.csv", ("All", 11)), list), True)
    check.equal(isinstance(load_data.load_data(
        "student-test.csv", ("something", 11)), list), True)
    check.equal(isinstance(load_data.load_data(
        "student-test.csv", ("Failures", 3)), list), True)
    check.equal(isinstance(load_data.load_data(
        "student-test.csv", ("Health", 1)), list), True)
    check.equal(isinstance(load_data.load_data(
        "student-test.csv", ("Age", 17)), list), True)
    check.equal(isinstance(load_data.load_data(
        "student-test.csv", ("School", "MS")), list), True)
    # test that add_average returns a list (3 different test cases required)
    check.equal(isinstance(load_data.add_average(
        load_data.load_data("student-test.csv", ("All", 11))), list), True)
    check.equal(isinstance(load_data.add_average(
        load_data.load_data("student-test.csv", ("Age", 18))), list), True)
    check.equal(isinstance(load_data.add_average(
        load_data.load_data("student-test.csv", ("Health", 3))), list), True)

    check.summary()

# Place test_return_list_correct_lenght function here


def test_return_list_correct_lenght():
    # Complete the function with your test cases

    # test that student_school_list returns a list with the correct lenght (3 different test cases required)

    # school_test_cases = {"GP": 3, "CF": 3, "MS": 4} # Test case dict = {INPUT: EXPECTED}
    check.equal(len(load_data.student_school_list(
        'student-test.csv', "GP")), 3)
    check.equal(len(load_data.student_school_list(
        'student-test.csv', "MS")), 4)
    check.equal(len(load_data.student_school_list(
        'student-test.csv', "RF")), 0)

    # test that student_age_list returns a list  with the correct lenght (3 different test cases required)
    check.equal(len(load_data.student_age_list('student-test.csv', 18)), 4)
    check.equal(len(load_data.student_age_list('student-test.csv', 12)), 0)
    check.equal(len(load_data.student_age_list('student-test.csv', 17)), 6)

    # test that student_health_list returns a list  with the correct lenght (3 different test cases required)
    check.equal(len(load_data.student_health_list('student-test.csv', 3)), 8)
    check.equal(len(load_data.student_health_list('student-test.csv', 4)), 3)
    check.equal(len(load_data.student_health_list('student-test.csv', 6)), 0)

    # test that student_failures_list returns a list   with the correct lenght(3 different test cases required)
    check.equal(
        len(load_data.student_failures_list('student-test.csv', 0)), 11)
    check.equal(
        len(load_data.student_failures_list('student-test.csv', 2)), 2)
    check.equal(
        len(load_data.student_failures_list('student-test.csv', 4)), 0)

    # test that load_data returns a list  with the correct lenght (6 different test cases required)
    check.equal(len(load_data.load_data(
        'student-test.csv', ("Failures", 0))), 11)
    check.equal(len(load_data.load_data(
        'student-test.csv', ("Health", 3))), 8)
    check.equal(len(load_data.load_data('student-test.csv', ("Age", 18))), 4)
    check.equal(len(load_data.load_data(
        'student-test.csv', ("School", "MS"))), 4)
    check.equal(len(load_data.load_data('student-test.csv', ("All", 0))), 15)
    check.equal(len(load_data.load_data('student-test.csv', ("G1", 5))), 0)

    # test that add_average returns a list   with the correct lenght (3 different test cases required)
    check.equal(len(load_data.add_average([{"School": "GP", "Age": 18, "StudyTime": 2,
                "Failures": 0, "Health": 3, "Absences": 6, "G1": 5, "G2": 6, "G3": 6}])), 1)
    check.equal(len(load_data.add_average([{"School": "MS", "Age": 17, "StudyTime": 1,
                "Failures": 0, "Health": 4, "Absences": 8, "G1": 11, "G2": 10, "G3": 10}])), 1)
    check.equal(len(load_data.add_average([{"School": "MS", "Age": 17, "StudyTime": 1, "Failures": 0, "Health": 4, "Absences": 8, "G1": 11, "G2": 10, "G3": 10}, {
                "School": "GP", "Age": 18, "StudyTime": 2, "Failures": 0, "Health": 3, "Absences": 6, "G1": 5, "G2": 6, "G3": 6}])), 2)

    check.summary()

# Place test_return_correct_dict_inside_list function here


def test_return_correct_dict_inside_list() -> None:
    # Complete the function with your test cases

    # test that student_school_list returns a correct dictionary inside the list (3 different test cases required)
    check.equal(load_data.student_school_list('student-test.csv', 'GP')
                [0], {'Age': 18, 'StudyTime': 2.0, 'Failures': 0, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6})

    check.equal(load_data.student_school_list('student-test.csv', 'MS')
                [3], {'Age': 18, 'StudyTime': 3.0, 'Failures': 0, 'Health': 5, 'Absences': 2, 'G1': 9, 'G2': 8, 'G3': 8})

    check.equal(load_data.student_school_list('student-test.csv', 'CF')
                [2], {'Age': 17, 'StudyTime': 1.0, 'Failures': 2, 'Health': 5, 'Absences': 0, 'G1': 7, 'G2': 6, 'G3': 0})

    # test that student_age_list returns a correct dictionary inside the list  (3 different test cases required)
    check.equal(load_data.student_age_list('student-test.csv', 18)
                [1], {'School': 'BD', 'StudyTime': 2.0, 'Failures': 0, 'Health': 3, 'Absences': 2, 'G1': 8, 'G2': 8, 'G3': 8})

    check.equal(load_data.student_age_list('student-test.csv', 16)
                [1], {'School': 'CF', 'StudyTime': 2.0, 'Failures': 1, 'Health': 5, 'Absences': 4, 'G1': 10, 'G2': 12, 'G3': 12})

    check.equal(load_data.student_age_list('student-test.csv', 18)
                [2], {'School': 'BD', 'StudyTime': 3.0, 'Failures': 0, 'Health': 3, 'Absences': 1, 'G1': 13, 'G2': 12, 'G3': 12})

    # test that student_health_list returns a correct dictionary inside the list  (3 different test cases required)
    check.equal(load_data.student_health_list('student-test.csv', 1)
                [0], {'School': 'MS', 'Age': 17, 'StudyTime': 3.0, 'Failures': 0, 'Absences': 7, 'G1': 10, 'G2': 9, 'G3': 9})

    check.equal(load_data.student_health_list('student-test.csv', 4)
                [2], {'School': 'MS', 'Age': 17, 'StudyTime': 3.0, 'Failures': 0, 'Absences': 4, 'G1': 14, 'G2': 14, 'G3': 14})

    check.equal(load_data.student_health_list('student-test.csv', 5)
                [2], {'School': 'MS', 'Age': 18, 'StudyTime': 3.0, 'Failures': 0, 'Absences': 2, 'G1': 9, 'G2': 8, 'G3': 8})

    # test that student_failures_list returns a correct dictionary inside the list (3 different test cases required)
    check.equal(load_data.student_failures_list('student-test.csv', 2)
                [0], {'School': 'CF', 'Age': 15, 'StudyTime': 5.0, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 9, 'G3': 7})

    check.equal(load_data.student_failures_list('student-test.csv', 2)
                [1], {'School': 'CF', 'Age': 17, 'StudyTime': 1.0, 'Health': 5, 'Absences': 0, 'G1': 7, 'G2': 6, 'G3': 0})

    check.equal(load_data.student_failures_list('student-test.csv', 3)
                [0], {'School': 'GP', 'Age': 15, 'StudyTime': 2.0, 'Health': 3, 'Absences': 10, 'G1': 7, 'G2': 8, 'G3': 10})

    # test that load_data returns a correct dictionary inside the list (6 different test cases required)
    check.equal(load_data.load_data('student-test.csv', ('School', 'MB')), [{'Age': 16, 'StudyTime': 2.0, 'Failures': 0, 'Health': 3, 'Absences': 12, 'G1': 5, 'G2': 5, 'G3': 5}, {
                'Age': 15, 'StudyTime': 1.0, 'Failures': 0, 'Health': 3, 'Absences': 2, 'G1': 10, 'G2': 12, 'G3': 12}])

    check.equal(load_data.load_data('student-test.csv', ('Age', 16)), [{'School': 'MB', 'StudyTime': 2.0, 'Failures': 0, 'Health': 3, 'Absences': 12, 'G1': 5, 'G2': 5, 'G3': 5}, {
                'School': 'CF', 'StudyTime': 2.0, 'Failures': 1, 'Health': 5, 'Absences': 4, 'G1': 10, 'G2': 12, 'G3': 12}])

    check.equal(load_data.load_data('student-test.csv', ('School', 'GP')), [{'Age': 18, 'StudyTime': 2.0, 'Failures': 0, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6}, {
                'Age': 17, 'StudyTime': 2.0, 'Failures': 0, 'Health': 3, 'Absences': 4, 'G1': 5, 'G2': 5, 'G3': 6}, {'Age': 15, 'StudyTime': 2.0, 'Failures': 3, 'Health': 3, 'Absences': 10, 'G1': 7, 'G2': 8, 'G3': 10}])

    check.equal(load_data.load_data('student-test.csv', ('Failures', 1)),
                [{'School': 'CF', 'Age': 16, 'StudyTime': 2.0, 'Health': 5, 'Absences': 4, 'G1': 10, 'G2': 12, 'G3': 12}])

    check.equal(load_data.load_data('student-test.csv', ('Health', 1)),
                [{'School': 'MS', 'Age': 17, 'StudyTime': 3.0, 'Failures': 0, 'Absences': 7, 'G1': 10, 'G2': 9, 'G3': 9}])

    check.equal(load_data.load_data('student-test.csv', ('Health', 3)), [{'School': 'GP', 'Age': 18, 'StudyTime': 2.0, 'Failures': 0, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6}, {'School': 'GP', 'Age': 17, 'StudyTime': 2.0, 'Failures': 0, 'Absences': 4, 'G1': 5, 'G2': 5, 'G3': 6}, {'School': 'GP', 'Age': 15, 'StudyTime': 2.0, 'Failures': 3, 'Absences': 10, 'G1': 7, 'G2': 8, 'G3': 10}, {'School': 'MB', 'Age': 16, 'StudyTime': 2.0, 'Failures': 0, 'Absences': 12, 'G1': 5, 'G2': 5, 'G3': 5}, {
                'School': 'MB', 'Age': 15, 'StudyTime': 1.0, 'Failures': 0, 'Absences': 2, 'G1': 10, 'G2': 12, 'G3': 12}, {'School': 'CF', 'Age': 15, 'StudyTime': 5.0, 'Failures': 2, 'Absences': 6, 'G1': 5, 'G2': 9, 'G3': 7}, {'School': 'BD', 'Age': 18, 'StudyTime': 2.0, 'Failures': 0, 'Absences': 2, 'G1': 8, 'G2': 8, 'G3': 8}, {'School': 'BD', 'Age': 18, 'StudyTime': 3.0, 'Failures': 0, 'Absences': 1, 'G1': 13, 'G2': 12, 'G3': 12}])

    # test that add_average returns a correct dictionary inside the list  (3 different test cases required)
    check.equal(load_data.add_average([{'School': 'GP', 'Age': 18, 'StudyTime': 2.0, 'Failures': 0, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6}, {'School': 'GP', 'Age': 17, 'StudyTime': 2.0, 'Failures': 0, 'Absences': 4, 'G1': 5, 'G2': 5, 'G3': 6}, {'School': 'GP', 'Age': 15, 'StudyTime': 2.0, 'Failures': 3, 'Absences': 10, 'G1': 7, 'G2': 8, 'G3': 10}, {'School': 'MB', 'Age': 16, 'StudyTime': 2.0, 'Failures': 0, 'Absences': 12, 'G1': 5, 'G2': 5, 'G3': 5}, {'School': 'MB', 'Age': 15, 'StudyTime': 1.0, 'Failures': 0, 'Absences': 2, 'G1': 10, 'G2': 12, 'G3': 12}, {'School': 'CF', 'Age': 15, 'StudyTime': 5.0, 'Failures': 2, 'Absences': 6, 'G1': 5, 'G2': 9, 'G3': 7}, {'School': 'BD', 'Age': 18, 'StudyTime': 2.0, 'Failures': 0, 'Absences': 2, 'G1': 8, 'G2': 8, 'G3': 8}, {'School': 'BD', 'Age': 18, 'StudyTime': 3.0, 'Failures': 0, 'Absences': 1, 'G1': 13, 'G2': 12, 'G3': 12}]), [{'School': 'GP', 'Age': 18, 'StudyTime': 2.0,
                'Failures': 0, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6, 'G_Avg': 5.67}, {'School': 'GP', 'Age': 17, 'StudyTime': 2.0, 'Failures': 0, 'Absences': 4, 'G1': 5, 'G2': 5, 'G3': 6, 'G_Avg': 5.33}, {'School': 'GP', 'Age': 15, 'StudyTime': 2.0, 'Failures': 3, 'Absences': 10, 'G1': 7, 'G2': 8, 'G3': 10, 'G_Avg': 8.33}, {'School': 'MB', 'Age': 16, 'StudyTime': 2.0, 'Failures': 0, 'Absences': 12, 'G1': 5, 'G2': 5, 'G3': 5, 'G_Avg': 5.0}, {'School': 'MB', 'Age': 15, 'StudyTime': 1.0, 'Failures': 0, 'Absences': 2, 'G1': 10, 'G2': 12, 'G3': 12, 'G_Avg': 11.33}, {'School': 'CF', 'Age': 15, 'StudyTime': 5.0, 'Failures': 2, 'Absences': 6, 'G1': 5, 'G2': 9, 'G3': 7, 'G_Avg': 7.0}, {'School': 'BD', 'Age': 18, 'StudyTime': 2.0, 'Failures': 0, 'Absences': 2, 'G1': 8, 'G2': 8, 'G3': 8, 'G_Avg': 8.0}, {'School': 'BD', 'Age': 18, 'StudyTime': 3.0, 'Failures': 0, 'Absences': 1, 'G1': 13, 'G2': 12, 'G3': 12, 'G_Avg': 12.33}])

    check.equal(load_data.add_average([{'Age': 18, 'StudyTime': 2.0, 'Failures': 0, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6}, {'Age': 17, 'StudyTime': 2.0, 'Failures': 0, 'Health': 3, 'Absences': 4, 'G1': 5, 'G2': 5, 'G3': 6}, {'Age': 15, 'StudyTime': 2.0, 'Failures': 3, 'Health': 3, 'Absences': 10, 'G1': 7, 'G2': 8, 'G3': 10}]), [
                {'Age': 18, 'StudyTime': 2.0, 'Failures': 0, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6, 'G_Avg': 5.67}, {'Age': 17, 'StudyTime': 2.0, 'Failures': 0, 'Health': 3, 'Absences': 4, 'G1': 5, 'G2': 5, 'G3': 6, 'G_Avg': 5.33}, {'Age': 15, 'StudyTime': 2.0, 'Failures': 3, 'Health': 3, 'Absences': 10, 'G1': 7, 'G2': 8, 'G3': 10, 'G_Avg': 8.33}])

    check.equal(load_data.add_average([{'School': 'MS', 'Age': 17, 'StudyTime': 3.0, 'Failures': 0, 'Absences': 7, 'G1': 10, 'G2': 9, 'G3': 9}]), [
                {'School': 'MS', 'Age': 17, 'StudyTime': 3.0, 'Failures': 0, 'Absences': 7, 'G1': 10, 'G2': 9, 'G3': 9, 'G_Avg': 9.33}])

    check.summary()


# Place test_add_average function here
def test_add_average():
    # Complete the function with your test cases

    # test that the function does not change the lengh of the list provided as input parameter (5 different test cases required)
    check.equal(len(load_data.add_average(
        load_data.student_health_list('student-test.csv', 3))), 8)
    check.equal(len(load_data.add_average(
        load_data.student_age_list('student-test.csv', 15))), 3)
    check.equal(len(load_data.add_average(
        load_data.student_failures_list('student-test.csv', 2))), 2)
    check.equal(len(load_data.add_average(
        load_data.student_school_list('student-test.csv', 'GP'))), 3)
    check.equal(len(load_data.add_average(
        load_data.load_data('student-test.csv', ('All', 0)))), 15)

    # test that the function returns an empty list when it is called whith an empty list
    check.equal(len(load_data.add_average([])), 0)

    # test that the function inscrememnts the number of keys of the dictionary inside the list by one  (5 different test cases required)
    check.equal(len(load_data.add_average(
        load_data.student_health_list('student-test.csv', 1))[0]), 9)
    check.equal(len(load_data.add_average(
        load_data.student_age_list('student-test.csv', 16))[0]), 9)
    check.equal(len(load_data.add_average(
        load_data.student_failures_list('student-test.csv', 1))[0]), 9)
    check.equal(len(load_data.add_average(
        load_data.student_school_list('student-test.csv', 'MS'))[0]), 9)
    check.equal(len(load_data.add_average(
        load_data.load_data('student-test.csv', ('All', 0)))[0]), 10)

    # test that the G_Avg value is properly calculated  (5 different test cases required)
    check.equal(load_data.add_average(load_data.student_age_list(
        'student-test.csv', 18))[0]['G_Avg'], 5.67)
    check.equal(load_data.add_average(load_data.student_health_list(
        'student-test.csv', 5))[0]['G_Avg'], 11.33)
    check.equal(load_data.add_average(load_data.student_failures_list(
        'student-test.csv', 1))[0]['G_Avg'], 11.33)
    check.equal(load_data.add_average(load_data.student_school_list(
        'student-test.csv', 'BD'))[0]['G_Avg'], 8.0)
    check.equal(load_data.add_average(load_data.load_data(
        'student-test.csv', ('All', 0)))[0]['G_Avg'], 5.67)

    check.summary()


# Do NOT include a main script in your submission
