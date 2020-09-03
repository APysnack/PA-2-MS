from CSV_Generator import GenCSV
from Array import ArrayClass
from math import log2


# generates 9 array objects of length (i * 1000) where i = 1 - 10
def generate_all():
    array_list = []

    # iterates values of i
    for i in range(1, 10):

        # num will be size of array (1000, 2000, 3000, etc.)
        num = i * 1000

        # creates a temporary array object
        temp = ArrayClass(num)

        # adds the array object to a list of array objects
        array_list.append(temp)

    # returns the list of all generated arrays
    return array_list


# sorts all arrays in the list of array objects
def sort_all(a_list):

    # iterates through list of array objects
    for array in a_list:

        # calls a class function that sorts each instance of the array
        array.sort_self()


# appends csv with merge_sort statistics
def append_csv(a_list, csv):

    # for every array in the list of array objects
    for array in a_list:

        # storing values for each column (n, logn, time, nlogn/time)
        n = array.length
        nlogn = (n * log2(n))
        time = array.sort_time
        final = (nlogn / time)

        # these are the column values for each row
        cols = [n, nlogn, time, final]

        # adds a new row with the above values
        csv.add_row(cols)


# main user menu
def create_csv(array_list):
    # name of the csv file we will create
    csv_name = "Mergesort_Time.csv"

    # header for each of the csv columns
    header = ["Input size n for Array_i", "Value of n*logn", "Time Spent (nanoseconds)",
              "Value of (n*logn / time)"]

    # declares a CSV object with a specified name and header (currently hardcoded)
    csv_obj = GenCSV(csv_name, header)

    # creates a new CSV file with csv_name as file name and header as the header
    csv_obj.create()

    # iterates through the array list and writes each statistic as a row to the csv file
    append_csv(array_list, csv_obj)


def main():
    pass
    # # generates 9 arrays of varying sizes and stores them in a list
    # array_list = generate_all()
    #
    # # sorts all 9 arrays using merge sort
    # sort_all(array_list)
    #
    # # prompts user with a menu to select from options
    # user_menu(array_list)