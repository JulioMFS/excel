import urllib
import re

print ("we will try to open this url, in order to get IP Address")

#url = "http://checkip.dyndns.org"
url = "https://sanfona.myvnc.com"
print (url)
#--------------------------------------------------
import urllib.request as ur
s = ur.urlopen(url)
sl = s.read()
print(sl)
#---------------------------------------------------
#request = urllib.urlopen(url).read()

#theIP = re.findall(r"d{1,3}.d{1,3}.d{1,3}.d{1,3}", sl)

print ("your IP Address is: ",  sl)