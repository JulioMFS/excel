import html
import os

def find_files(filename, search_path):
   result = []

# Wlaking top-down from the root
   for root, dir, files in os.walk(search_path):
      if filename in files:
         print("search path: ", search_path, ", dir: ", dir)
         result.append(os.path.join(root, filename))
   return result

print(find_files("Passwords.ods","C:\\"))
#---------------------------------------------------------------------------------
import os

for dirpath, dirnames, filenames in os.walk("c:\\"):
   for filename in filenames:
      if filename.endswith(".txt"):
         print(os.path.join(dirpath, filename))

#----------------------------------------------------------------------------
#!/usr/bin/env python2
import requests
from bs4 import BeautifulSoup
import pynotify
from time import sleep
def sendmessage(title, message):
    pynotify.init("Test")
    notice = pynotify.Notification(title, message)
    notice.show()
    return
url = "http://static.cricinfo.com/rss/livescores.xml"
while True:
    r = requests.get(url)
    while r.status_code != 200:
            r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    data = soup.find_all("description")
    score = data[1].text
    sendmessage("Score", score)
    sleep(60)

#-----------------------------------------------------------------------
import os
from os.path import join

#lookfor = "Passwords.ods"
lookfor = "SanfonaStuff.xlsx"
for root, dirs, files in os.walk('C:\\'):
    #print ("searching", root)
    if lookfor in files:
        print ("found: %s" % join(root, lookfor))
        break

#------------------------------------------------------------------------
import os

counter = 0
print("If you want all the excel file, for example write .xlsx")
inp = input("What are you looking for?:> ")
thisdir = os.getcwd()
for r, d, f in os.walk("C:\\"):  # change the hard drive, if you want
    for file in f:
        filepath = os.path.join(r, file)
        if inp in file:
            counter += 1
            print(os.path.join(r, file))
print(f"trovati {counter} files.")

#-----------------------------------------------------------------------------

import os
import shutil
import path
#from path import path

destination = "F:\\file_copied"


# os.makedirs(destination)

def copyfile(dir, filetype='pptx', counter=0):
    "Searches for pptx (or other - pptx is the default) files and copies them"
    for pack in os.walk(dir):
        for f in pack[2]:
            if f.endswith(filetype):
                fullpath = pack[0] + "\\" + f
                print(fullpath)
                shutil.copy(fullpath, destination)
                counter += 1
    if counter > 0:
        print('-' * 30)
        print("\t==> Found in: `" + dir + "` : " + str(counter) + " files\n")


for dir in os.listdir():
    "searches for folders that starts with `_`"
    if dir[0] == '_':
        # copyfile(dir, filetype='pdf')
        copyfile(dir, filetype='txt')