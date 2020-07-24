import requests
import re

def runScript():
    file_object = open("proxies-list.txt", "w")
    r = requests.get("https://www.sslproxies.org/")
    matches = re.findall(r"<td>\d+.\d+.\d+.\d+</td><td>\d+</td>", r.text)
    revised_list = [m1.replace("<td>", "") for m1 in matches]
    for socket_str in revised_list:
        file_object.write(socket_str[:-5].replace("</td>", ":")+"\n")


runScript()
