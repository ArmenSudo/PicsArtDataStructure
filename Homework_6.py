arr = [ 1, 2, 3, 4, 5, -6, 1, 1, 2, 1]

def contain(data, val):
    return val in data

def pop(data, i=None):
    if i == None:
        return data[:-1:]
    elif i > 0 and i < len(data):
        return data[:i:] + data[(i+1)::]
    else:
        return "Index Error"

def remove_all(data, value):
    i = 0
    data = data[:]
    while i != len(data):
        if data[i] == value:
            del data[i]
            i -= 1
        i += 1
    return data

def reverse(data):
    data = data.copy()
    return data[::-1]

def min(data):
    min_value = data[0]
    for x in data:
        if x < min_value:
            min_value = x
    return min_value

def max(data):
    max_value = data[0]
    for x in data:
        if x > max_value:
            max_value = x
    return max_value


print(f'Initial array {arr}\n')
print(f'Contain Result: {contain(arr, 1)}\n')
print(f'Pop Result:\n   Naxnakan: {arr}\n   Stacvac: {pop(arr, 1)}\n')
print(f'Remove_all Result:\n   Naxnakan: {arr}\n   Stacvac: {remove_all(arr, 1)}\n')
print(f'Reverse Result:\n   Naxnakan: {arr}\n   Stacvac: {reverse(arr)}\n')
print(f'Min Result: {min(arr)}')
print(f'Max Result: {max(arr)}')
