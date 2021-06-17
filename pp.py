
import urllib.request , socket
import requests,os
import sys
import urllib.request, socket
from threading import Thread


                
socket.setdefaulttimeout(30)
ptrade_done=0

def check_proxy(pip):
    global ptrade_done
    try:        
        proxy_handler = urllib.request.ProxyHandler({'https': pip})        
        opener = urllib.request.build_opener(proxy_handler)
        opener.addheaders = [('User-agent', 'Mozilla/5.0')]
        urllib.request.install_opener(opener)        
        sock=urllib.request.urlopen('https://prtrend.org')  # change the url address here
        print(pip)
        req='curl -s --header "Content-Type: application/json"  --request POST  --data \'{"fullName": "\u041b\u0438\u0437\u0430 \u0414\u0435\u043c\u0438\u0434\u043e\u0432\u0430","email": "l4iza_demidova307459@goldmail.ru","country": "DK",  "Lang": "ru",  "countryPrefix": "",  "phone": "739667154",  "password": "abFgfarG307459",  "password repeatPassword": "abFgfarG307459",  "linkID": "",  "checkbox": "on",  "firstName": "\u041b\u0438\u0437\u0430",  "lastName": "\u0414\u0435\u043c\u0438\u0434\u043e\u0432\u0430"}\' --proxy "'+pip+'"  https://prtrend.org/wp-json/xcritical/1.0/registration'
        print(req)

        result = os.popen(req).read()
        print(result)
        if ("leadGuid" in result):
            print(":::::::::::: reg OK::::::::::::::")
            ptrade_done=1
        
    except urllib.error.HTTPError as e:        
        return e
    except Exception as detail:
        return detail
    return 0


def threaded_proxy():
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
#proxyList = ['140.82.61.218:8080','178.32.47.218:17501'] # there are two sample proxy ip
    proxyList =q

#Example run : echo -ne "192.168.1.1:231\n192.168.1.2:231" | python proxy_checkpy3-async.py
    proxies = q
    threads = []

    for proxy in proxies:
        if(ptrade_done==0):
            thread = Thread( target=check_proxy, args=(proxy.strip(), ))
            thread.start()
            threads.append(thread)

    for thread in threads:
        thread.join()

threaded_proxy()
print(ptrade_done)