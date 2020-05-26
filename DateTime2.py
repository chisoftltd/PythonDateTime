# Python DateTime project by ChisoftMedia
import datetime
from datetime import date

# Getting Day, Month, Year and Weekday

today = date.today()
print("Today's date is :", today)

print("Day: ", today.day)
print("Month: ", today.month)
print("Year: ", today.year)

# Getting both Date and Time
today1 = datetime.time()
print("Today's date is: ", today1)
print("Hour: ", today1.hour)

today2 = datetime.datetime.now()
print(today2)


# Here is the complete code to get current date and time using datetime now
def main():
    ##DATETIME OBJECTS
    #Get today's date from datetime class
    today=datetime.datetime.now()
    #print (today)
    # Get the current time
    #t = datetime.time(datetime.now())
    #print "The current time is", t
    #weekday returns 0 (monday) through 6 (sunday)
    wd=date.weekday(today)
    #Days start at 0 for monday
    days= ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
    print("Today is day number %d" % wd)
    print("which is a " + days[wd])

if __name__== "__main__":
    main()

#  Working with Only Time
currenttime = datetime.datetime.now()
print("Year ", currenttime.year)
print("Month ", currenttime.month)
print("Weekday ", currenttime.day)
print("Day ", currenttime.day)
print("Hours ", currenttime.hour)
print("Minutes ", currenttime.minute)
print("Seconds ", currenttime.second)
print("Microseconds", currenttime.microsecond)

# Formatting Date and Time using strftime()
print(currenttime.strftime("%A %b %d %Y by %I:%M %p %Y %S %Z %X %c"))