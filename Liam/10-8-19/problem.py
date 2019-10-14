from collections import deque

# O(kn) solution using a running max element variable and iterating through array 
# while looking at a k-length window
def printSubarrayMaxesWindow(arr, k):
    if len(arr) == 0:
        return
    elif len(arr) == 1:
        print(arr[0])
        return

    currentMaxEl = arr[0]

    for i in range(len(arr) - (k - 1)):
        for j in range(i, i + k):
            if currentMaxEl < arr[j]:
                currentMaxEl = arr[j]

        print(currentMaxEl)
        currentMaxEl = arr[i + 1]


# O(n) solution (looked up solution since Justin wanted to see the answer) >:(
def printSubarrayMaxesDeque(arr, k):
    dequeWindow = deque()

    for i in range(k):
        while dequeWindow and arr[i] >= arr[ dequeWindow[-1] ]:
            dequeWindow.pop()

        dequeWindow.append(i)

    print(arr[ dequeWindow[0] ])

    for i in range(k, len(arr)):
        while dequeWindow and dequeWindow[0] <= (i - k):
            dequeWindow.popleft()

        while dequeWindow and arr[i] >= arr[ dequeWindow[-1] ]:
            dequeWindow.pop()

        dequeWindow.append(i)
        print(arr[ dequeWindow[0] ])



def main():
    arr = [10, 5, 2, 7, 8, 7]
    k = 3

    printSubarrayMaxesWindow(arr, k)
    print()
    printSubarrayMaxesDeque(arr, k)


if __name__ == '__main__':
    main()