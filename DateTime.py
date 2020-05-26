# Day8 of Python Programming by ChisoftMedia
#
import calendar
import datetime
import time

# Date & Time
import timeit
import_module = "import random"

currentTime = time.time()
print(currentTime)

# Creating a Calendar
mycalender = calendar.month(2020, 5)
print(mycalender)
print(calendar.firstweekday())

myTime = time.asctime()
print(myTime)
print(myTime)

timeNow = datetime.datetime.now()
print("The time is : " + str(timeNow))
print("The month is: " + str(timeNow.month))
print("The month is: " + str(timeNow.year))
print(timeNow.strftime("%A"))

# Creating Date Objects
x = datetime.datetime(2020, 5, 17)
print(x)

# The strftime() Method

x = datetime.datetime(2020, 5, 26)
print(x.strftime("%B"))

# The time Module
print(time.altzone)

def procedure():
    time.sleep(2.5)

# Timeit() - timeit.timeit(stmt, setup,timer, number)
print(timeit.timeit('output = 10*5'))

print("The time taken is ", timeit.timeit(stmt='a = 10; b = 10; sum= a+b'))

# using triple quotes
testcode = '''
def test():
    return random.randint(10,100)
'''

print(timeit.repeat(stmt=testcode, setup=import_module))

print(timeit.timeit(stmt=testcode, setup=import_module))
