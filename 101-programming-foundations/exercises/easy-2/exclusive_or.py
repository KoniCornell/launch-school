
'''
condition1 = value1 and not value2
condition2 = value2 and not value1
return bool(condition1 or condition2)

'''

# def xor(a,b):
#     if bool(a) and bool(b):
#         return False
#     else:
#         return bool(a) or bool(b)
    
def xor(value1, value2):
    return bool((value1 and not value2) or (value2 and not value1))

    
print(xor(5, 0) == True)
print(xor(False, True) == True)
print(xor(1, 1) == False)
print(xor(True, True) == False)