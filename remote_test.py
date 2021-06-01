from selenium import webdriver
#from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
chrome_options = webdriver.ChromeOptions()
from selenium.webdriver.common.proxy import Proxy, ProxyType
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-gpu')
prox = Proxy()
prox.proxy_type = ProxyType.MANUAL


p="208.127.60.176:8080"
print ("PROXY: "+p)
# Proxy IP & Port
prox.http_proxy = p
#prox.socks_proxy = p
prox.ssl_proxy = p
chrome_options.add_argument('--ignore-certificate-errors')
# Configure capabilities 
capabilities = webdriver.DesiredCapabilities.CHROME
prox.add_to_capabilities(capabilities)


driver = webdriver.Chrome("/usr/local/bin/chromedriver", options=chrome_options, desired_capabilities=capabilities)
#driver = webdriver.Remote("http://172.17.0.1:4444/wd/hub", options=chrome_options,desired_capabilities=capabilities)
driver.get('https://whatismyip.host')
print(driver.page_source)
