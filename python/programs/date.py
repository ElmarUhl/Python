# Import date library
import datetime

# Get date
date = datetime.datetime.now()

print(date)
print(date.year)
# Print the week
print(date.strftime("%A"))

# Input date
date2 = datetime.datetime(2020,5,17)
print(date2)

date3 = datetime.datetime(2018, 6, 1)
# Print month
print(date3.strftime("%B"))
