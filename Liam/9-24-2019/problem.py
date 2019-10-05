# O(n) solution using constant space to find least positive integer not appearing in the given array
# (had to look at solution to figure out how to solve in linear time and constant space) #SAD! :(
def findMissingLeastInt(arr):
    # use pidgeonhole principle to know solution must be <= length of array + 1, therefore can copy positive
    # integers less than length of array to their corresponding index number (don't care about preserving
    # array's values other than the positve integers less than the length of array)
    for i in range(len(arr)):
        if arr[i] > 0 and arr[i] <= len(arr):
            arr[ arr[i] - 1 ] = arr[i]

    # iterate and look for which index the positive integers numbers stop counting up in order
    for i in range(len(arr)):
        if arr[i] != (i + 1):
            return (i + 1)

    return (len(arr) + 1)



def main():
    arr = [6, 5, 2, 4, -5, -7]
    assert findMissingLeastInt(arr) == 1

    arr = [1, 2, 3, 4, 5]
    assert findMissingLeastInt(arr) == 6

    arr = [2, -4, 1, -2, -1, 5, 3]
    assert findMissingLeastInt(arr) == 4

    arr = [-1, 2, 2, 1, 4, 5, 4, 1, 1, -2, -1, -3, 5]
    assert findMissingLeastInt(arr) == 3

if __name__ == '__main__':
    main()