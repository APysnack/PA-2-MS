import random
import time


class ArrayClass:

    # constructor for the array class
    def __init__(self, size):
        # length of the array
        self.length = size

        # the unsorted array
        self.id = self.generate_array(size)

        # the sorted array (initialized as an empty list)
        self.sorted_id = []

        # the amount of time it took to sort the array
        self.sort_time = 0

    # sorts using merge_sort() and times the performance
    def sort_self(self):
        # begins timer
        start_time = time.perf_counter_ns()

        # executes sort and stores the sorted array in the sorted version of the instance
        self.sorted_id = ArrayClass.merge_sort(self.id)

        # stops the timer
        stop_time = time.perf_counter_ns()

        # stores the time it took to sort in the instance
        self.sort_time = (stop_time - start_time)

    # creates a randomized array
    @staticmethod
    def generate_array(num):
        array = []

        # iterates num times
        for x in range(num):
            # generates a random number between argument a and argument b
            a = random.randint(0, 2000)

            # appends this number to the array
            array.append(a)
        return array

    # basic merge method for merging 2 sorted lists
    @staticmethod
    def merge(left, right):
        # resulting array to be output
        result = []

        # initializing left and right pointers to 0
        left_pointer, right_pointer = 0, 0

        # while the left point and right pointer have not reached the end of their respective arrays:
        while left_pointer < len(left) and right_pointer < len(right):

            # finds the smaller number of the two pointers and adds it to the result list
            if left[left_pointer] < right[right_pointer]:
                result.append(left[left_pointer])
                left_pointer += 1
            else:
                result.append(right[right_pointer])
                right_pointer += 1

        # upon exiting the while loop, one of the arrays has been fully traversed
        # extend populates result with the remaining elements from the other array
        result.extend(left[left_pointer:])
        result.extend(right[right_pointer:])
        return result

    # merge sort method
    @staticmethod
    def merge_sort(array):
        # base case for when the array size = 1
        if len(array) <= 1:
            return array

        # locates the n/2 element of the array
        middle = int(len(array) / 2)

        # recursively calls merge sort on the left half of the array
        left = ArrayClass.merge_sort(array[:middle])

        # recursively calls merge sort on the right half of the array
        right = ArrayClass.merge_sort(array[middle:])

        # once left and right results have been returned as sorted arrays,
        # passes them to the merge function to be merged together
        return ArrayClass.merge(left, right)