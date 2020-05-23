import time#so hat sleeep time method can be used
from datetime import datetime as dt#it is used to acess current time
host_temp="hosts"#local hosts file created in the folder
hosts_path=r"C:\Windows\System32\drivers\etc"#it is the location of the hosts file in windows
redirect="127.0.0.1"
website_list=["www.facebook.com","facebook.com"]#domain  names of the websites which u want to block


while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,13) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,14):
        print("working hours")#r+ is used so that u can append ur domain names in yhe non empty file
        with open(hosts_path,'r+') as file:#open is used to open your host file
            content=file.read()#content conyaisn all the written thiongs of the host file
            for website in website_list:#if the host file already contaisn the domains names we wantto bblock the we do nothing else we add those domain names in the hosts file
                if website in content:
                    pass
                else:
                    file.write(redirect+" "+website+"\n")

    else:
        with open(hosts_path,'r+') as file:
            content=file.readlines()#so that it reads the whole file line by line and store these diff lines asa list
            file.seek(0)# to bring the cursor at the begening of the file content
            for line in content:
                if not any (website in line for website in website_list):
                    file.write(line)
            file.truncate()
        print("fun hours")
    time.sleep(5)
