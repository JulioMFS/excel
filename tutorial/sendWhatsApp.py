# importing the module
import pywhatkit
import datetime
from datetime import date, timedelta

# datetime object
dt = datetime.datetime.now()
h0 = dt.hour
m1 = dt.minute

dt1 = dt + timedelta(minutes=1)
h = dt1.hour
m = dt1.minute

print("\n\n------------------------------------------------------------------")

print("Datetime object =", dt)
print("Datetime object =", dt1)

print (dt.strftime("hour/minute now:\t %H:%M"))
print (dt1.strftime("hour/minute 1 min:\t %H:%M"))
# printing in dd/mm/YY H:M:S format using strftime()
dt_string = dt.strftime("Date: %d/%m/%Y  time: %H:%M:%S")
print("Current date and time =", dt_string)
msg = (f"Hello from my RPi test pywhatkit, message sent at: {h}:{m}")
print("Message: ", msg)
print("------------------------------------------------------------------\n\n")
# using Exception Handling to avoid
# unprecedented errors
try:

    # sending message to receiver
    # using pywhatkit
    pywhatkit.sendwhatmsg("+351917586991",
                  msg,
                  h, m)
    print("Successfully Sent! " )

except:

    # handling exception
    # and printing error message
    print("An Unexpected Error!")