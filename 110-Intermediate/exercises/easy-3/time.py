def time_of_day(minutes):
    holder = abs(minutes)
    
    # 1440 minutes in a day
    days = holder // 1440
    holder = holder % 1440

    hour, minute = divmod(holder, 60)

    if minutes < 0:
        hour = 23 - hour
        minute = 60 - minute
    return f'{hour:02d}:{minute:02d}'

print(time_of_day(0) == "00:00")        # True
print(time_of_day(-3) == "23:57")       # True
print(time_of_day(35) == "00:35")       # True
print(time_of_day(-1437) == "00:03")    # True
print(time_of_day(3000) == "02:00")     # True
print(time_of_day(800) == "13:20")      # True
print(time_of_day(-4231) == "01:29")    # True
