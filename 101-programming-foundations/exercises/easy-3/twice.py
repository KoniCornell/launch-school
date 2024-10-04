
def twice(number: int):
    num = list(str(number))
    idx = len(num) // 2
    if (num[:idx] == num[idx:]):
        num = ''.join(num)
        return int(num)
    else:
        num = ''.join(num)
        return (int(num) * 2)


print(twice(37) == 74)                  # True
print(twice(44) == 44)                  # True
print(twice(334433) == 668866)          # True
print(twice(444) == 888)                # True
print(twice(107) == 214)                # True
print(twice(103103) == 103103)          # True
print(twice(3333) == 3333)              # True
print(twice(7676) == 7676)              # True