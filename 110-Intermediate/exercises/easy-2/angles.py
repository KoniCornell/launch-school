'''
 Function takes a floating point number representing an angle 
 between 0 and 360 degrees and returns a string representing 
 that angle in degrees, minutes, and seconds. You should use a 
 degree symbol (°) to represent degrees, a single quote (') to 
 represent minutes, and a double quote (") to represent seconds. 
 There are 60 minutes in a degree, and 60 seconds in a minute.
 1° = 60 min
 1 min = 60 s
'''
DEGREE = "\u00B0"

def dms(num: float):
    if num == 0:
        degree, minute, seconds = 0, 0, 0
    else:
        degree = num - (num % int(num)) 
        minute = (num - degree) * 60
        if minute == 0:
            seconds = 0
        else:
            seconds = (minute % int(minute)) * 60

    result = f"{int(degree)}{DEGREE}{int(minute):02}'{int(seconds):02}\""
    print(result)
    return result


# All of these examples should print True
print(dms(30) == "30°00'00\"")
print(dms(76.73) == "76°43'48\"")
print(dms(254.6) == "254°35'59\"")
print(dms(93.034773) == "93°02'05\"")
print(dms(0) == "0°00'00\"")
print(dms(360) == "360°00'00\"" or dms(360) == "0°00'00\"")