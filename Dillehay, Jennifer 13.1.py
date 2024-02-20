#Dillehay, Jennifer
#M06 Programming Assignment, 13.1, 13.2, 13.3


import time

# Get the current time
now = time.time()

# Convert the current time to a string representation
today_string = time.ctime(now)
print("Today's string representation:", today_string)

# Parse the date from the string representation
parsed_date = time.strptime(today_string)
print("Parsed date:", parsed_date)
