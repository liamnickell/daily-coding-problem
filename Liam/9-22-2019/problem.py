# easy solution using division
def withDivision(arr):
    arrProduct = 1
    
    for i in range(len(arr)):
        arrProduct *= arr[i]

    newArr = [None] * len(arr)
    for i in range(len(arr)):
        newArr[i] = arrProduct // arr[i]

    return newArr


# O(nlog(n)) solution Logan and I thought of:
# recursively splits up array into smallest parts and builds product array up by applying each half's running 
# product to its opposite (relative) half
#
# didn't intend on passing subarray bounds along the whole way, but python wasn't applying changes to passed 
# subarrays to the original array itself for some reason (I'm probably just not understanding python's pass by 
# value of reference approach correctly)
def splitProducts(arr):
    newArr = [1] * len(arr)
    getProducts(arr, newArr, 0, len(arr))
    return newArr


def getProducts(arr, newArr, start, end):
    if (end - start) == 1:
        return arr[start]
    elif (end - start) == 2:
        # apply products to opposite relative "halves" and return total product of this half
        newArr[start] *= arr[start + 1]
        newArr[start + 1] *= arr[start]
        return arr[start] * arr[start + 1]

    # recursively calculate the product of the first half of the array while applying products to
    # first half of product array correctly
    firstHalfProduct = getProducts(arr, newArr, start, start + (end - start) // 2)
    for i in range(start + (end - start) // 2, start + (end - start)):
        newArr[i] *= firstHalfProduct

    # recursively calculate the product of the second half of the array while applying products to
    # second half of product array correctly
    secondHalfProduct = getProducts(arr, newArr, start + (end - start) // 2, start + (end - start))
    for i in range(start, start + (end - start) // 2):
        newArr[i] *= secondHalfProduct

    return firstHalfProduct * secondHalfProduct


# O(n) prefix and suffix products solution (looked at correct solution) :(
def prefixSuffixProducts(arr):
    if len(arr) == 0:
        return arr

    prefixProducts = [ arr[0] ]
    suffixProducts = [ arr[-1] ]

    for i in range(1, len(arr)):
        # appends the product of current arr element and previous prefix product element
        prefixProducts.append(prefixProducts[i - 1] * arr[i])

        # make product of (i+1)-th to last arr element and first suffix product the new first suffix product
        suffixProducts.insert(0, suffixProducts[0] * arr[-(i + 1)])

    newArr = [1] * len(arr)

    for i in range(len(newArr)):
        if i < (len(newArr) - 1):
            newArr[i] *= suffixProducts[i + 1]
        if i > 0:
            newArr[i] *= prefixProducts[i - 1]

    return newArr


def main():
    arr = [1, 2, 3, 4, 5, 6]
    print(withDivision(arr))
    print(splitProducts(arr))
    print(prefixSuffixProducts(arr))


if __name__ == '__main__':
    main()
    