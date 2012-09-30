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
        arr = copy.copy(self.array)
        #print arr
        path_track = [(arr, 0)]
        self._quick_sort_iter(arr, path_track, 0, len(arr) - 1)
        return path_track

    def _quick_sort_iter(self, arr, path_track, lowindex, highindex):
        """
        the iteration version of quick sort
        """
        pivotindex = 0
        if lowindex < highindex:
            pivotindex = self._partion(arr, lowindex, highindex)
            path_track.append((copy.copy(arr), pivotindex))
            self._quick_sort_iter(arr, path_track, lowindex, pivotindex - 1)
            self._quick_sort_iter(arr, path_track, pivotindex + 1, highindex)

    def _partion(self, arr, lowindex, highindex):
        """
        the partion method for quick sort
        """
        # swap between the lowindex and the middle entry
        temp = arr[lowindex]
        arr[lowindex] = arr[(highindex + lowindex) / 2]
        arr[(lowindex + highindex) / 2] = temp

        pivot = arr[lowindex]
        lastsmall = lowindex

        for i in xrange(lowindex + 1, highindex + 1):
            if arr[i] < pivot:
                lastsmall += 1
                temp = arr[i]
                arr[i] = arr[lastsmall]
                arr[lastsmall] = temp

        temp = arr[lastsmall]
        arr[lastsmall] = arr[lowindex]
        arr[lowindex] = temp

        return lastsmall

    def merge_sort(self):
        """
        the merge sort, it can't be show in animation
        return -> the track list of sort algorithm, the element
            with this form:
                cur_array, special_pos(the change pos)
        """
        arr = copy.copy(self.array)
        print arr
        path_track = [(copy.copy(arr), 0)]
        path_track.append(([], 0))
        sort_arr = self._merge_sort_iter(arr, path_track)
        print sort_arr
        return path_track

    def _merge_sort_iter(self, arr, path_track):
        mid = int(len(arr) / 2)
        path_track.append((copy.copy(arr), mid))
        if len(arr) <= 1:
            return arr
        return self._merge(self._merge_sort_iter(arr[:mid], path_track),
                           self._merge_sort_iter(arr[mid:], path_track))

    def _merge(self, list1, list2):
        """
        merge two list in order
        """
        final = []
        while list1 and list2:
            final.append(list1[0] <= list2[0] and list1.pop(0) or list2.pop(0))

        final_list = final + list1 + list2
        return final_list

    def merge_sort_2(self):
        """
        the second version of merge, it can be show in animation
        return -> the track list of sort algorithm, the element
            with this form:
                cur_array, special_pos(the change pos)
        """
        arr = copy.copy(self.array)
        path_track = [(copy.copy(arr), 0)]
        self._merge_sort_2(arr, 0, len(arr) - 1, path_track)
        return path_track

    def _merge_sort_2(self, arr, low, high, path_track):
        if high - low < 1:
            return
        mid = (low + high) // 2

        self._merge_sort_2(arr, low, mid, path_track)
        self._merge_sort_2(arr, mid + 1, high, path_track)

        first = low
        middle = mid

        while first <= middle and middle + 1 <= high:
            if arr[first] >= arr[middle + 1]:
                #print 'first = ' + str(first) + ', middle + 1 = ' + str(middle + 1)
                # insert arr[middle + 1] before arr[first]
                self._insert_before(arr, middle + 1, first)
                middle += 1
            path_track.append((copy.copy(arr), middle))
            first += 1

    def _insert_before(self, arr, from_index, to_index):
        """
        insert the element of arr in index from_index in front of the element
        in index to_index
        """
        value = copy.copy(arr[from_index])
        #print arr

        copy_arr = copy.copy(arr)

        if from_index == to_index:
            return

        for i in xrange(to_index, from_index):
            arr[i + 1] = copy_arr[i]

        arr[to_index] = value

        if to_index < from_index:
            from_index += 1
