# O(n^2) brute force method
def bruteForce(arr, k):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i] + arr[j] == k:
                return True

    return False


# O(nlog(n)) sorting method
def sortFirst(arr, k):
    arr.sort()
    
    start = 0
    end = len(arr) - 1
    
    # change numbers being summed based on comparison of current sum to k
    while start != end:
        startEndSum = arr[start] + arr[end]
        if startEndSum == k:
            return True
        elif startEndSum < k:
            start += 1
        else:
            end -= 1

    return False



# O(n) storing difference with k
def hashmapDifference(arr, k):
    differences = dict()

    for i in range(len(arr)):
        if arr[i] in differences:
            return True
        else:
            differences[k - arr[i]] = i     # value of key doesn't really matter

    return False


def main():
    arr = [4, 7, -3, 6, 1, -6]
    k = 9

    print(bruteForce(arr, k))
    print(sortFirst(list(arr), k))      # copy array since it will be sorted
    print(hashmapDifference(arr, k))


if __name__ == '__main__':
    main()