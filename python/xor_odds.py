def find_odd_occurrence(arr):
    result = 0
    for num in arr:
        result = result ^ num
    return result
