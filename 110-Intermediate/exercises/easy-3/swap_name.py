def swap_name(string):
    string = string.split(' ')
    result = f'{string[-1]}, {" ".join(string[:-1])}'
    print(result)
    return result

# def swap_name(name):
#     return f"{name.split()[-1]}, {' '.join(name.split()[:-1])}"
print(swap_name('Joe Roberts') == "Roberts, Joe")   # True
print(swap_name('Karl Oskar Henriksson Ragvals')
                == "Ragvals, Karl Oskar Henriksson")  # True
