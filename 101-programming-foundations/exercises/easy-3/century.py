def century(year):
    # Calculate the century
    century = (year + 99) // 100
    
    # Determine the correct suffix for the century using match-case
    if 11 <= century % 100 <= 13:
        suffix = 'th'
    else:
        last_digit = century % 10
        match last_digit:
            case 1:
                suffix = 'st'
            case 2:
                suffix = 'nd'
            case 3:
                suffix = 'rd'
            case _:
                suffix = 'th'
    
    return f"{century}{suffix}"

print(century(2000) == "20th")          # True
print(century(2001) == "21st")          # True
print(century(1965) == "20th")          # True
print(century(256) == "3rd")            # True
print(century(5) == "1st")              # True
print(century(10103) == "102nd")        # True
print(century(1052) == "11th")          # True
print(century(1127) == "12th")          # True
print(century(11201) == "113th")        # True