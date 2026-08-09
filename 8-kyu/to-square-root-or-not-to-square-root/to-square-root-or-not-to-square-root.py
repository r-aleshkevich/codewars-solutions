def square_or_square_root(arr):
    result = []
    for i in arr:
        root = i ** 0.5
        if int(root) == root:
            result.append(int(root))
        else:
            result.append(i ** 2)
    return result
​
        