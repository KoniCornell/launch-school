def triangle(num: int):
    j = num
    for i in range(1,num + 1):
        print((' ' * j) + ('*' * i))
        j -= 1

triangle(5)
triangle(9)