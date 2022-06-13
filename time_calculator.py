day_map = {
    "Monday": 0,
    "Tuesday": 1,
    "Wednesday": 2,
    "Thursday": 3,
    "Friday": 4,
    "Saturday": 5,
    "Sunday": 6,
}

week_days = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday",
}


def add_time(start, duration, day=""):
    # print(add_time("11:06 PM", "13:02"))

    slicing_of_start = start.split()

    start = slicing_of_start[0].split(":")
    duration = duration.split(":")
    time_index = slicing_of_start[1]

    end = frmt(start, duration, time_index, day)

    return end[0]


def frmt(start, duration, time_index, day_name):
    s_hour = int(start[0])
    s_min = int(start[1])
    d_hour = int(duration[0])
    d_min = int(duration[1])

    e_hour = 0
    e_min = s_min + d_min

    if e_min >= 60:
        d_hour += 1
        e_min = e_min - 60

    days = int(d_hour / 24)

    if days >= 1:
        d_hour -= days * 24

    if s_hour + d_hour < 12:
        e_hour = s_hour + d_hour
    elif s_hour + d_hour >= 12 and time_index == "AM":
        e_hour = s_hour + d_hour - 12
        time_index = "PM"
    elif s_hour + d_hour >= 12 and time_index == "PM":
        days += 1
        time_index = "AM"
        e_hour = s_hour + d_hour - 12

    if e_hour == 0:
        e_hour = 12

    e_hour = str(e_hour)
    e_min = str(e_min)

    zero = "0"

    if len(e_min) == 1:
        e_min = "".join((zero, e_min))

    string_days = ""

    if days == 1:
        string_days = "(next day)"
    elif days > 1:
        string_days = "(" + str(days) + " days later)"

    if day_name == "":
        result = [e_hour + ":" + e_min + " " + time_index + " " + string_days]
        return result
    else:
        day_name = day_name.lower()
        day_name = day_name[0].upper() + day_name[1:]
        end_day = week_days[(day_map[day_name] + days) % 7]
        result = [e_hour + ":" + e_min + " " + time_index + ", " + end_day + " " + string_days]
        return result