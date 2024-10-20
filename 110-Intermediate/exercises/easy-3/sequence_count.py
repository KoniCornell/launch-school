def sequence_count(total:int, start: int):
    return [start * num for num in range(1, total + 1)]

print(sequence_count(5, 1) == [1, 2, 3, 4, 5])          # True
print(sequence_count(4, -7) == [-7, -14, -21, -28])     # True
print(sequence_count(3, 0) == [0, 0, 0])                # True
print(sequence_count(0, 1000000) == [])                 # True