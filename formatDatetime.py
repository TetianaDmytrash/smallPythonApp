from datetime import datetime

# Default format of LocalDate=2016-09-16 16::Sep::2016
local_date = datetime.now().strftime("%Y-%m-%d %H::%b::%Y")
print("Default format of LocalDate =", local_date)

# Default format of LocalDateTime=2016-09-16T11:46:01.455 16::Sep::2016 11::46::01
local_datetime = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + " " + datetime.now().strftime("%d::%b::%Y %H::%M::%S")
print("Default format of LocalDateTime =", local_datetime)

# Default format of Instant=2016-09-16T06:16:01.456Z
instant = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"
print("Default format of Instant =", instant)

# Default format after parsing = 2014-04-27T21:39:48
parsed_date = "2014-04-27T21:39:48"
parsed_datetime = datetime.strptime(parsed_date, "%Y-%m-%dT%H:%M:%S")
print("Default format after parsing =", parsed_datetime.strftime("%Y-%m-%dT%H:%M:%S"))