import time
from datetime import datetime as dt

from matplotlib import lines

hosts_temp = r"D:\USER\Programming\Phyton\app12\hosts"
hosts_path = "C:\Windows\System32\drivers\etc\hosts" 
redirect = "127.0.0.1"
website_list = ["www.facebook.com", "www.twitter.com", "facebook.com", "twitter.com"]

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 10) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 12):
        print("working hours")
        with open(hosts_temp, "r+") as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect + " " + website + "\n")
        
    else:
        with open(hosts_temp, "r+") as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
        print("fun hours")

    time.sleep(5)

"""Task scheduler | create task | higher permissions | triggers | at startup 
    actions | Start a Program | website_blocker.pyw
    
    .pyw to run background"""