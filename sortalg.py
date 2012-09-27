import random
import copy


class SortAlg(object):
    def __init__(self, size):
        self.size = size
        self.array = []

    def generate_random_array(self):
        """
        generate a random array
        """
        self.array = []
        while len(self.array) < self.size:
            rand_int = random.randint(1, self.size)
            if rand_int in self.array:
                continue
            else:
                self.array.append(rand_int)

    def bubble_sort(self):
        """
        the simplest bubble sort
        return -> the track list of sort algorithm, the element
            with this form:
                cur_array, special_pos(the change pos)
        """
        arr = copy.copy(self.array)
        sort_track = [(copy.copy(arr), 0)]
        for i in xrange(len(arr)):
            for j in xrange(len(arr)):
                if arr[i] < arr[j]:
                    temp = arr[i]
                    arr[i] = arr[j]
                    arr[j] = temp
                    cur_arr = copy.copy(arr)
                    sort_track.append((cur_arr, j))
                    print arr
        return sort_track

    def select_sort(self):
        """
        selection sort
        return -> the track list of sort algorithm, the element
            with this form:
                cur_array, special_pos(the change pos)
        """
        arr = copy.copy(self.array)
        sort_track = [(copy.copy(arr), 0)]
        for i in reversed(xrange(len(arr))):
            largest = 0
            for j in xrange(1, i + 1):
                if arr[largest] < arr[j]:
                    largest = j

            # move the largest to the end of array
            temp = arr[largest]
            arr[largest] = arr[i]
            arr[i] = temp
            sort_track.append((copy.copy(arr), largest))

        return sort_track

    def insert_sort(self):
        """
        the insertion sort
        return -> the track list of sort algorithm, the element
            with this form:
                cur_array, special_pos(the change pos)
        """
        arr = copy.copy(self.array)
        sort_track = [(copy.copy(arr), 0)]
        for unsort_pos in xrange(1, len(arr)):
            if arr[unsort_pos] < arr[unsort_pos - 1]:
                pos = unsort_pos
                cur = arr[unsort_pos]
                while pos > 0 and arr[pos - 1] > cur:
                    arr[pos] = arr[pos - 1]  # move back the entry
                    pos -= 1

                arr[pos] = cur
                sort_track.append((copy.copy(arr), pos))

        return sort_track

    def quick_sort(self):
        """
        the quick sort
        return -> the track list of sort algorithm, the element
            with this form:
                cur_array, special_pos(the change pos)
        """
        pass
