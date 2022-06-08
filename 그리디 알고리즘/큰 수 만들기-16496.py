n = int(input())
arr = list(map(int, input().split()))
numbers = list(map(str, arr))


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    lesser_arr, equal_arr, greater_arr = [], [], []
    for num in arr:
        p = int(pivot + num)
        v = int(num + pivot)
        if v > p:
            lesser_arr.append(num)
        elif v < p:
            greater_arr.append(num)
        else:
            equal_arr.append(num)
    return quick_sort(lesser_arr) + equal_arr + quick_sort(greater_arr)


numbers = quick_sort(numbers)
print(str(int(''.join(numbers))))

