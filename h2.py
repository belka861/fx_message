from selenium import webdriver
# Option 1 - with ChromeOptions
chrome_options = webdriver.ChromeOptions()
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from phone_gen import PhoneNumber

chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox') # required when running as root user. otherwise you would get no sandbox errors. 
import time,os,random,datetime,sys
# Option 2 - with pyvirtualdisplay
#from pyvirtualdisplay import Display 
#display = Display(visible=0, size=(1024, 768)) 
#display.start() 
#driver = webdriver.Chrome(driver_path='/home/dev/chromedriver', 
#  service_args=['--verbose', '--log-path=/tmp/chromedriver.log'])
# Log path added via service_args to see errors if something goes wrong (always a good idea - many of the errors I encountered were described in the logs)
# And now you can add your website / app testing functionality: 

logfile="h2.log"
def _log(message):
#    fh=open(logfile,"a",encoding="cp1251")
    fh=open(logfile,"a")
    text=str(datetime.datetime.now())+" "+str(message)+"\r\n"
    print(text)
    fh.write(text)
    fh.close()
    return True

import requests

from transliterate import translit, get_available_language_codes
url = 'https://raw.githubusercontent.com/belka861/fx_message/main/phrases.txt'
r = requests.get(url, allow_redirects=True)
open('phrases.txt', 'wb').write(r.content)

url = 'https://raw.githubusercontent.com/belka861/fx_websocket/main/names_f.txt'
r = requests.get(url, allow_redirects=True)
open('names_f.txt', 'wb').write(r.content)

url = 'https://raw.githubusercontent.com/belka861/fx_websocket/main/countries.txt'
r = requests.get(url, allow_redirects=True)
open('countries.txt', 'wb').write(r.content)

url = 'https://raw.githubusercontent.com/belka861/fx_websocket/main/surnames_f.txt'
r = requests.get(url, allow_redirects=True)
open('surnames_f.txt', 'wb').write(r.content)

with open('nyse-listed.csv', 'r') as file:
    nyse = file.readlines()













def _wait_element(xpath):
    r = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, xpath)))
    return True



def _click(xpath):
    r=driver.find_element_by_xpath(xpath)
    r.click()
    return True

def _do_email():
    driver.get('https://24xforex.com/ru#contact')
#    time.sleep(2)

    e=driver.find_element_by_xpath('//*[@id="contact_email"]')
    e.send_keys(email)
#    time.sleep(1)
    name1=driver.find_element_by_xpath('//*[@id="contact_name"]')
    name1.send_keys(final_name)
    _click('//*[@id="contact_message"]')
    text1=driver.find_element_by_xpath('//*[@id="contact_message"]')
    text1.send_keys(question)
#    time.sleep (1)
#    _wait_element
#    r=driver.find_element_by_css_selector('#contact > div.contact-block > div.form-block > form > button')
#    r.click()
    _wait_element('//*[@id="contact"]/div[2]/div[2]/form/button')
    driver.execute_script('document.evaluate(\'//*[@id="contact"]/div[2]/div[2]/form/button\', document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue.click();')
#    time.sleep(4)
    _wait_element('//*[@id="contact"]/div[2]/div[1]')
    r=driver.find_element_by_xpath('//*[@id="contact"]/div[2]/div[1]').text
    print(r)



def _do_chat():
    driver.get("https://24xforex.com/ru")
    _wait_element('//*[@id="jvlabelWrap"]/jdiv[2]')
    _click('//*[@id="jvlabelWrap"]/jdiv[2]')

    _wait_element('//*[@id="jcont"]/jdiv[3]/jdiv/jdiv[3]/jdiv[1]/jdiv[1]/textarea')
    r=driver.find_element_by_xpath('//*[@id="jcont"]/jdiv[3]/jdiv/jdiv[3]/jdiv[1]/jdiv[1]/textarea')
    r.send_keys(question)

    webdriver.ActionChains(driver).send_keys(Keys.ENTER).perform()

    _wait_element('//*[@id="scrollbar-container"]/jdiv[1]/jdiv/jdiv[4]/jdiv/jdiv/jdiv/jdiv/jdiv[1]/input')
    name1=driver.find_element_by_xpath('//*[@id="scrollbar-container"]/jdiv[1]/jdiv/jdiv[4]/jdiv/jdiv/jdiv/jdiv/jdiv[1]/input')
    name1.send_keys(final_name)

    phone=driver.find_element_by_xpath('//*[@id="scrollbar-container"]/jdiv[1]/jdiv/jdiv[4]/jdiv/jdiv/jdiv/jdiv/jdiv[2]/input')
    phone.send_keys(tnf)


    _wait_element('//*[@id="scrollbar-container"]/jdiv[1]/jdiv/jdiv[4]/jdiv/jdiv/jdiv/jdiv/jdiv[3]/input')
    e=driver.find_element_by_xpath('//*[@id="scrollbar-container"]/jdiv[1]/jdiv/jdiv[4]/jdiv/jdiv/jdiv/jdiv/jdiv[3]/input')
    e.send_keys(email)
    time.sleep(1)

    #button
    _wait_element('//*[@id="scrollbar-container"]/jdiv[1]/jdiv/jdiv[4]/jdiv/jdiv/jdiv/jdiv/jdiv[4]')
    _click('//*[@id="scrollbar-container"]/jdiv[1]/jdiv/jdiv[4]/jdiv/jdiv/jdiv/jdiv/jdiv[4]')
    driver.execute_script('document.evaluate(\'//*[@id="scrollbar-container"]/jdiv[1]/jdiv/jdiv[4]/jdiv/jdiv/jdiv/jdiv/jdiv[4]\', document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue.click();')


    time.sleep(3)
    text2=driver.find_element_by_xpath('//*[@id="jcont"]').text
    print(text2)

    return True

#os.system('pkill chrome')

#random question
with open('phrases.txt', 'r') as file:
    data = file.readlines()

with open('names_f.txt', 'r') as file:
    names = file.readlines()

with open('surnames_f.txt', 'r') as file:
    surnames = file.readlines()

with open('countries.txt', 'r') as file:
    countries = file.readlines()

while True:
    driver = webdriver.Chrome('/home/igor/chromedriver', options=chrome_options, service_args=['--verbose', '--log-path=/tmp/chromedriver.log'])

    question=data[random.randint(1,len(data)-1)].replace('\n', '')
#    _log(question)

    name=names[random.randint(1,len(names)-1)].replace('\n', '')
#    _log(name)

    surname=surnames[random.randint(1,len(surnames)-1)].replace('\n', '')
#    _log(surname)

    country=countries[random.randint(1,len(countries)-1)].replace('\n', '')
#    _log(country)

    #phone # depends on conutry
    ph=PhoneNumber(country)
    tn=ph.get_number(full=False)
    tnf=ph.get_number()
#    _log(tnf)

    #random full name choice
    dice=random.choice([1,2,3])
    _log (dice)
    if (dice==1):
        final_name=name
    if (dice==2):
        final_name=name+" "+surname
    if (dice==3):
        final_name=surname+" "+name
    _log(final_name)

    dice=random.choice([1,2,3,4,5,6,7,8,9,20])
    if (dice==5):
        tick=nyse[random.randint(1,len(nyse)-1)].replace('\n', '')
        question="Мне аналитик посоветовал купить акции "+tick+" А ОНИ СЕГОДНЯ ОБВАЛИЛИСЬ! ВЕРНИТЕ МНЕ МОИ ДЕНЬГИ!!!"
#    _log(question)


    #email
    domains=['mail.ru','yandex.ru', 'rambler.ru', 'outlook.com', 'gmail.com', 'hotmail.com', 'list.ru', 'bk.ru', 'inbox.ru', 'internet.ru',  'yahoo.com', 'aol.com', 'e1.ru','inbox.lv', 'dino.lv','human.lv', 'fit.lv','sok.lv', 'eclub.lv', 'zohomail.com', 'protonmail.com', 'mail.com', 'usa.com', 'counsellor.com', 'cyberservices.com', 'protestant.com']
    domain=random.choice(domains)
    password=""
    for i in range (1,7):
        password=password+random.choice('01234567890')
    username=translit(final_name, reversed=True).replace(" ", "_").replace("'","").lower()+password
    email=username+"@"+domain

    _log (final_name+" "+tnf+" "+country+" "+email+" "+question)
    t=question

#    sys.exit()



#email='testemail4543544@yandex.ru'
#final_name="Alina Mavrodi"
#t="test message ths is tes"

#driver.get('https://24xforex.com/') 
#print(driver.title)
# driver.click...

#_do_email()
    _do_chat()
    _do_email()
    driver.delete_all_cookies()
    driver.close()
    driver.quit()
    os.system('pkill chrome')
