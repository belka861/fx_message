
import urllib.request , socket
import requests
socket.setdefaulttimeout(180)
                                                                                                                                            	
response = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=https&timeout=7000&anonymity=elite&ssl=yes')
q=[]
for line in response.text.splitlines():
    print (line)
    q.append(line)
print (q)
# prinitng request content
#print(response.content)
#pr=str(response.content).split('\r\n')
#print (pr)
# read the list of proxy IPs in proxyList
proxyList = ['140.82.61.218:8080','178.32.47.218:17501'] # there are two sample proxy ip
proxyList =q

import sys
import urllib.request, socket
from threading import Thread
                
socket.setdefaulttimeout(30)

def check_proxy(pip):
    try:        
        proxy_handler = urllib.request.ProxyHandler({'https': pip})        
        opener = urllib.request.build_opener(proxy_handler)
        opener.addheaders = [('User-agent', 'Mozilla/5.0')]
        urllib.request.install_opener(opener)        
        sock=urllib.request.urlopen('https://trade.globalallianceltd.com/registration-ru')  # change the url address here
        print(pip)
    except urllib.error.HTTPError as e:        
        return e
    except Exception as detail:
        return detail
    return 0

#Example run : echo -ne "192.168.1.1:231\n192.168.1.2:231" | python proxy_checkpy3-async.py
proxies = q
threads = []

for proxy in proxies:
    thread = Thread( target=check_proxy, args=(proxy.strip(), ))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()
