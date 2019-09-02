def fentian(x, y):
    if x > y:
        if x % y == 0:
            return y
        else:
            return fentian(x - y, y)
    elif x == y:
        return y
    else:
        if y % x == 0:
            return x
        else:
            return fentian(y - x, x)


length = fentian(1680, 640)
print(length)


def sumOfArray(x=None) -> int:
    if x is None:
        return 0
    else:
        if len(x) == 1:
            return x[0]
        else:
            return x[0] + sumOfArray(x[1:])


summary = sumOfArray()
print(summary)


def numberoflist(x) -> int:
    if len(x) == 1:
        return 1
    else:
        return 1 + numberoflist(x[1:])


n = numberoflist([1, 2, 3, 4, 5, 5, 6, 6, 6, 6, 6, 6666666666, 6, 6, 6, 6, 6, 6])
print(n)


def maxoflist(x):
    if len(x) == 1:
        return x[0]
    elif len(x) == 2:
        if x[0] >= x[1]:
            return x[0]
        else:
            return x[1]
    else:
        if x[0] >= x[1]:
            x[1] = x[0]
            return maxoflist(x[1:])
        else:
            return maxoflist(x[1:])


whichmax = maxoflist([1, 2, 3, 4, 4, 4, 4, 4, 4, 9, 12, 121212, 15])
print(whichmax)


def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)


print(quicksort([1, 3, 4, 5, 61, 0, 12]))
