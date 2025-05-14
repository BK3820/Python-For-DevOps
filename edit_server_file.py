import re

def updateserver_config(filepath, key , vaule, operator):
    with open(filepath, "r") as file:
        content = file.readlines()

       

    with open(filepath, "w") as file:
        for eachlines in content:
            print (eachlines)
            if key in eachlines:
                indentation = re.match(r"^\s*",eachlines).group()
                file.write(indentation + key + operator + vaule +";"+ "\n")
        
            else:
                file.write(eachlines)

updateserver_config("server.conf","error_log","/var/log/nginx/SAMPLE.log"," " )
