def running_total(numbers: list):
    '''
    Returns a list of the cumulative totals
    '''

    # list comprehensions
    cumulatives = [sum(numbers[:idx + 1]) for idx in range(len(numbers))]
    return cumulatives

print(running_total([2, 5, 13]) == [2, 7, 20])    # True
print(running_total([14, 11, 7, 15, 20])
      == [14, 25, 32, 47, 67])                    # True
print(running_total([3]) == [3])                  # True
print(running_total([]) == [])                    # True