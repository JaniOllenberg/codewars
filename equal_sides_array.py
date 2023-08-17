def find_even_index(arr):
    for i in range(len(arr)):
        left_sum = 0
        right_sum = 0
        left_sum = sum(arr[0:i])
        right_sum = sum(arr[i+1:])
        print(f"left:{left_sum} right:{right_sum}")
        if left_sum == right_sum:
            return i
    return -1

print(find_even_index([1,2,3,4,3,2,1]))