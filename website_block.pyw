import time
from datetime import datetime as dt
host_temp=r"D:\APPLICATION_BUILDUP\hosts"
host_path=r"C:\Windows\System32\drivers\etc\hosts"
redirect="127.0.0.1"
websites=["www.facebook.com" , "facebook.com","youtube.com"]

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,16):
         print("working hours")
         file =open(host_path ,"r+")
         data=file.read()
         for website in websites:
            if website in data :
                pass
            else:
                file.write(redirect +"  "+ website + "\n")
    else:
        file=open(host_path, "r+")
        data=file.readlines()#readlines:produces list with all the lines in the file
        file.seek(0)
        for lines in data :
            if not any (website in lines for website in websites):
                file.write(lines)
        file.truncate()
        print("fun hours")
    time.sleep(5)