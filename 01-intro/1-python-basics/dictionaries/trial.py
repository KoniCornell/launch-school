sub_list = ["-", "-", "-"]
matrix = []

for _ in range(3):
    matrix.append(sub_list.copy()) #use a shallow copy of the list

print(matrix)

matrix[0][0] = "X"
print(matrix) # [['X', '-', '-'], ['X', '-', '-'], ['X', '-', '-']]