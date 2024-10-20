def substrings(lst: list):
    
    result = [lst[j:i + 1] 
            for j in range(len(lst))
            for i in range(j, len(lst))]
    print(result)
    
    return result

expected_result = [
    "a", "ab", "abc", "abcd", "abcde",
    "b", "bc", "bcd", "bcde",
    "c", "cd", "cde",
    "d", "de",
    "e",
]

print(substrings('abcde') == expected_result)  # True