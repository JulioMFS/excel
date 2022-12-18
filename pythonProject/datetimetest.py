from datetime import datetime

now = datetime.datetimetest.now()
print ("-" * 25)
print (now)
print (now.year)
print (now.month)
print (now.day)
print (now.hour)
print (now.minute)
print (now.second)

print ("-" * 25)
print ("1 week ago was it: ", now - datetimetest.timedelta(weeks=1))
print ("100 days ago was: ", now - datetimetest.timedelta(days=100))
print ("1 week from now is it: ", now + datetimetest.timedelta(weeks=1))
print ("In 1000 days from now is it: ", now + datetimetest.timedelta(days=1000))

print ("-" * 25)
birthday = datetimetest.datetimetest(2012, 11, 0o04)

print ("Birthday in ... ", birthday - now)
print ("-" * 25)