'''
a function named "rotate" that takes an array and returns a new one with the elements inside rotated n spaces.

If n is greater than 0 it should rotate the array to the right. If n is less than 0 it should rotate the array to the left. If n is 0, then it should return the array unchanged.

egs:
data = [1, 2, 3, 4, 5];

rotate(data, 1) # => [5, 1, 2, 3, 4]
rotate(data, 2) # => [4, 5, 1, 2, 3]
rotate(data, 3) # => [3, 4, 5, 1, 2]
rotate(data, 4) # => [2, 3, 4, 5, 1]
'''
def rotate(arr, n):
    n = n % len(arr)
    return arr[- n:] + arr[: - n]
