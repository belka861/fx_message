docker=0

q_ingo_reg=0

#ok windows
q_maxi_reg=1


q_24xforex_reg=0

#ok windows
q_24xforex_email=0

#ok windows
q_ingo_email=0

q_ptrend_reg=1
q_ptrend_chat=1
#Recaptcha
q_plus_reg=0
q_plus_email=0

#Global* not working
#q_qlobal*

#REGISTRATION DISABLED NOW
q_umarkets_reg=0

#captcha
q_st24online_reg=0

q_st24online_phone=1
q_st24online_email=1

q_cryptogazprom_reg=1
q_threaded_proxy=1
q_ptrend_email=0
q_ptrend_chat_noreg=1

q_gravity_reg=1
q_everest_chat=1
q_toptrade_email=1

ptrend_people={}
from selenium import webdriver
import platform
from selenium.webdriver.common.proxy import Proxy, ProxyType
#import numpy as np
#from scipy.interpolate import splev, splrep

# Option 1 - with ChromeOptions
chrome_options = webdriver.ChromeOptions()
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from phone_gen import PhoneNumber
import time,os,random,datetime,sys

prox = Proxy()
prox.proxy_type = ProxyType.MANUAL

#good
p="208.127.60.176:8080"
#good


#experiment
#p="175.215.8.145:3128"

# Proxy IP & Port
prox.http_proxy = p
#prox.socks_proxy = p
prox.ssl_proxy = p
chrome_options.add_argument('--ignore-certificate-errors')
# Configure capabilities 
capabilities = webdriver.DesiredCapabilities.CHROME
#prox.add_to_capabilities(capabilities)

import urllib.request , socket
import requests

import sys
import urllib.request, socket
from threading import Thread
                
socket.setdefaulttimeout(10)














if (platform.system()=='Windows'):
    mode="DEV"
else:
    mode="PROD"
global maxi_phone
co2=['Австрия','Азербайджан','Армения','Бельгия','Болгария','Венгрия','Германия','Греция','Дания','Испания','Италия','Казахстан','Кипр','Латвия','Литва','Молдова','Монако','Нидерланды','Норвегия','Польша','Португалия','Российская Федерация','Румыния','Словакия','Словения','Таджикистан','Узбекистан','Франция','Хорватия','Чешская Республика','Швейцария','Швеция',"Эстония"]
co2_dict={'Австрия':'AT','Азербайджан':'AZ','Армения':'AM','Бельгия':'BE','Болгария':'BG','Беларусь':'BY','Великобритания':'GB','Венгрия':'HU','Германия':'DE','Греция':'GR','Грузия':'GE','Дания':'DK','Испания':'ES','Италия':'IT','Казахстан':'KZ','Киргизстан':'KG','Кипр':'CY','Латвия':'LV','Литва':'LT','Люксембург':'LU','Молдова':'MD','Монако':'MC','Нидерланды':'NL','Норвегия':'NO','Польша':'PL','Португалия':'PT','Российская Федерация':'RU','Румыния':'RO','Словакия':'SK','Словения':'SI','Сербия':'RS','Таджикистан':'TJ','Узбекистан':'UZ','Финляндия':'FI','Франция':'FR','Хорватия':'HR','Черногория':'ME','Чешская Республика':'CZ','Швейцария':'CH','Швеция':'SE','Эстония':'EE'}
domains=['mail.ru','yandex.ru', 'rambler.ru', 'outlook.com', 'gmail.com', 'hotmail.com', 'list.ru', 'bk.ru', 'inbox.ru', 'internet.ru',\
'yahoo.com', 'aol.com', 'e1.ru','inbox.lv', 'dino.lv','human.lv', 'fit.lv','sok.lv', 'eclub.lv', 'zohomail.com', 'protonmail.com', 'mail.com',\
 'cyberservices.com', 'protestant.com', 'ya.ru','box.az','byke.com','chez.com','email.ru','gmx.net','goldmail.ru',\
'sendmail.ru','sendmail.com','gold.az','mail.lv','mail.lt','tyt.by','mail.by','rambler.lv','rambler.cz','outlook.ru','tut.by',\
'inet.ru','bigmailbox.com','lycos.com','netaddress.com','techemail.com','yandex.kz','yandex.lv','yandex.com','yandex.az','yandex.tr','ya.az',\
'aport.ru','chat.ru','newmail.ru','sitek.net','zmail.ru','id.ru','ok.ru','ru.ru']



chrome_options.add_argument('--disable-blink-features=AutomationControlled')
PATH='C:\Program Files (x86)\chromedriver.exe'
if (mode=="PROD"):
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('window-size=1920,1080')
    PATH='/usr/local/bin/chromedriver'

#    chrome_options.add_argument('--no-sandbox') # required when running as root user. otherwise you would get no sandbox errors.     
#    chrome_options.add_argument('--disable-blink-features=AutomationControlled')
#    from pyvirtualdisplay import Display 
#    display = Display(visible=0, size=(1920, 1080)) 
#    display.start() 

#else:
#    chrome_options.add_argument('--disable-blink-features=AutomationControlled')



#PATH='/home/sv/chromedriver'
#else:
#    PATH='/home/sv/chromedriver'

# Option 2 - with pyvirtualdisplay
#driver = webdriver.Chrome(driver_path='/home/dev/chromedriver', 
#  service_args=['--verbose', '--log-path=/tmp/chromedriver.log'])
# Log path added via service_args to see errors if something goes wrong (always a good idea - many of the errors I encountered were described in the logs)
# And now you can add your website / app testing functionality: 

logfile="h2.log"
def _log(message):
    fh=open(logfile,"a",encoding="utf-8")
#    fh=open(logfile,"a")
    text=str(datetime.datetime.now())+" "+str(message)+"\r\n"
    print(text)
    fh.write(text)
    fh.close()
    return True

cred_file="cred.txt"
def _cred(s,u,p):
    fh=open(cred_file,"a",encoding="utf-8")
#    fh=open(logfile,"a")
#    text=str(datetime.datetime.now())+" "+str(message)+"\r\n"
    text=s+","+u+","+p+"\r\n"
    _log(text)
    fh.write(text)
    fh.close()
    return True


def human_like_mouse_move(action, start_element):

    points = [[10, 2], [30, 2],[0, 0], [0, 2]];
    points = np.array(points)
    x = points[:,0]
    y = points[:,1]


    t = range(len(points))
    ipl_t = np.linspace(0.0, len(points) - 1, 100)


    x_tup = splrep(t, x, k=1)
    y_tup = splrep(t, y, k=1)

    x_list = list(x_tup)
    xl = x.tolist()
    x_list[1] = xl + [0.0, 0.0, 0.0, 0.0]

    y_list = list(y_tup)
    yl = y.tolist()
    y_list[1] = yl + [0.0, 0.0, 0.0, 0.0]

    x_i = splev(ipl_t, x_list)
    y_i = splev(ipl_t, y_list)

    startElement = start_element

    action.move_to_element(startElement);
    action.perform();

    c = 5
    i = 0
    for mouse_x, mouse_y in zip(x_i, y_i):
        action.move_by_offset(mouse_x,mouse_y);
        action.perform();
        _log("Move mouse to, %s ,%s" % (mouse_x, mouse_y))
        i =i+1    
        if (i == c):
            break














import requests

from transliterate import translit, get_available_language_codes
url = 'https://raw.githubusercontent.com/belka861/fx_message/main/phrases.txt'
r = requests.get(url, allow_redirects=True)
open('phrases.txt', 'wb').write(r.content)

url = 'https://raw.githubusercontent.com/belka861/fx_message/main/names_f.txt'
r = requests.get(url, allow_redirects=True)
open('names_f.txt', 'wb').write(r.content)

url = 'https://raw.githubusercontent.com/belka861/fx_websocket/main/countries.txt'
r = requests.get(url, allow_redirects=True)
open('countries.txt', 'wb').write(r.content)

url = 'https://raw.githubusercontent.com/belka861/fx_message/main/surnames_f.txt'
r = requests.get(url, allow_redirects=True)
open('surnames_f.txt', 'wb').write(r.content)


url = 'https://raw.githubusercontent.com/belka861/fx_message/main/nyse-listed.csv'
r = requests.get(url, allow_redirects=True)
open('nyse-listed.csv', 'wb').write(r.content)

url = 'https://www.mit.edu/~ecprice/wordlist.10000'
r = requests.get(url, allow_redirects=True)
open('wordlist10000.txt', 'wb').write(r.content)

with open('nyse-listed.csv', 'r') as file:
    nyse = file.readlines()


def _send_text(x,t):
    r=driver.find_element_by_xpath(x)
    r.send_keys(t)
    return True

def _get_text(x):
    r=driver.find_element_by_xpath(x).text
    return r










def _wait_element(xpath):
    r = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, xpath)))
    return True

def _wait_element60(xpath):
    r = WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.XPATH, xpath)))
    return True

def _wait_element5(xpath):
    r = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, xpath)))
    return True


#def ai(question):
def ai(question):
#    _log("----AI start---")
#    _log("Q: "+question)
    a=[]
    #question='Здравствуйте, я создам запрос, с вами свяжется ваш менеджер.'
    words=question.replace(',','').replace('.','').replace('\n', '').lower().split()
    for word in words:
       if (len(word)>6):
#           print (word)
           for d in data:
               if word in d.lower():
#                   print(d)
                   a.append(d)

    if (len(a)>2):
        answer=random.choice(a)
    else:
        answer=random.choice(data)
    answer=answer.replace('\n', '')

    if (answer==question):
        answer=random.choice(data)

    dice=random.randint(1,10)
    if (dice==5):
        answer=random.choice(data)

    answer=answer.replace('\n', '')

 


#    _log ("A: "+answer)
#    _log ("-----AI END--------")
    return (answer)


def _click(xpath):
    r=driver.find_element_by_xpath(xpath)
    r.click()
    return True

def _clear(xpath):
    r=driver.find_element_by_xpath(xpath)
    r.clear()
    return True



def get_greet():
    greet=random.choice(['Горячо приветствую',\
'Доброго здоровья',\
'Доброе утро!',\
'Добрый вечер!',\
'Добрый день!',\
'Доброе утро',\
'Добрый вечер',\
'Добрый день',\
'доброе утро',\
'добрый вечер',\
'добрый день',\
'Здравия желаю',\
'Здравствуйте!',\
'Здравствуйте',\
'Здравствуйте поддержка',\
'Ув. поддежка',\
'Ув. компания,',\
'Уважаемая компания компания,',\
'Здравствуй чят',\
'Здравствуй чат',\
'Здравствуйте,',\
'Здравствуйте, необходима ваша помощь',\
'доброго времени суток, необходима ваша помощь',\
'доброго времени суток',\
'Здравствуйте, необходима ваша поддержка',\
'Здравствуйте, необходима ваша консультация',\
'здравствуйте',\
'здравствуйте появились кое-какие вопросы',\
'здравствуйте надо пообщаться',\
'здравствуйте позвоните мне по поводу регистрации',\
'Моё почтение',\
'Позвольте Вас приветствовать',\
'Приветствую Вас',\
'Приветствую',\
'Салам Алейкум',\
'Намасте',\
'Hi, how are you',\
'Вечер в хату',\
'Як та на незалежний?',\
'Добрыдень',\
'Приятный вечер!',\
'Приятный день!',\
'Рада Вам,',\
'Привет,',\
'привет,',\
'Извините, что беспокою',\
'извините, что беспокою',\
'извините, что беспокою возможно по пустякам',\
'Рада Вас видеть',\
'Рада Вас видеть в добром здравии',\
'Рада Вас приветствовать',\
'Рада Вас слышать',\
'Разрешите Вас приветствовать,',\
'С добрым утром',\
'С добрым утром,',\
'Сердечно приветствую Вас,',\
'Как поживаяете?',\
'Салют,',\
'Hi,',\
'Hello,'])
    return greet

















def _24xforex_email():
    question=_get_question()
    name=_get_name()
    surname=_get_surname()
    final_name=_get_final_name(name,surname)
    email=_get_email_from_final_name(final_name)

    driver.get('https://24xforex.com/ru#contact')
#    _wait_element('//*[@id="contact_email')
    _send_text('//*[@id="contact_email"]',email)
    _send_text('//*[@id="contact_name"]',final_name)
    _click('//*[@id="contact_message"]')
    _send_text('//*[@id="contact_message"]',question)
    _wait_element('//*[@id="contact"]/div[2]/div[2]/form/button')
    driver.execute_script('document.evaluate(\'//*[@id="contact"]/div[2]/div[2]/form/button\', document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue.click();')
#    time.sleep(4)
    _wait_element('//*[@id="contact"]/div[2]/div[1]')
    _log(_get_text('//*[@id="contact"]/div[2]/div[1]'))
    return True




def ingo_email():
    question=_get_question()
    name=_get_name()
    surname=_get_surname()
    final_name=_get_final_name(name,surname)
    email=_get_email_from_final_name(final_name)
    driver.get('https://ingoinvest.com/ru')
#    time.sleep(7)
    _wait_element('//*[@id="contact_email"]')
    _send_text('//*[@id="contact_email"]',email)
    _send_text('//*[@id="contact_name"]',final_name)
    _click('//*[@id="contact_message"]')
    _send_text('//*[@id="contact_message"]',question)
#    time.sleep (1)
    _wait_element('//*[@id="contact"]/div/div[2]/div[1]/form/button')
    _click('//*[@id="contact"]/div/div[2]/div[1]/form/button')
#    _wait_element
#    r=driver.find_element_by_css_selector('#contact > div.contact-block > div.form-block > form > button')
#    r.click()
#    _wait_element('//*[@id="contact"]/div/div[2]/div[1]/form/button')
#    driver.execute_script('document.evaluate(\'//*[@id="contact"]/div/div[2]/div[1]/form/button\', document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue.click();')
#    time.sleep(4)
#    _wait_element('//*[@id="contact"]/div[2]/div[1]')
    _wait_element('//*[@id="wrapper"]/main/div[2]/article/h1')
    _log(_get_text('//*[@id="wrapper"]/main/div[2]/article/h1'))
    return True





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


def _24xforex_reg():
    name241=_get_name()
    surname241=_get_surname()    


#    driver.maximize_window()
    driver.delete_all_cookies()
    
    driver.get("https://24xforex.com/ru/register")

#    time.sleep(10)
#    _log(driver.page_source)

    driver.execute_script("window.open('about:blank', 'tab2');")
    driver.switch_to.window("tab2")
    driver.get('https://temp-mail.io/en')
#    _wait_element('//*[@id="email"]')
    time.sleep(3)
#    _log(driver.page_source)
    email=driver.find_element_by_id('email').get_attribute('value')
#    _log(email)
    driver.switch_to.window(driver.window_handles[0])
    _wait_element('//*[@id="live_name"]')
    e=driver.find_element_by_id('live_email')
    e.send_keys(email)

    name1=driver.find_element_by_xpath('//*[@id="live_name"]')
    name1.send_keys(name241)

    last_name=driver.find_element_by_xpath('//*[@id="live_last_name"]')
    last_name.send_keys(surname241)
    
    select=driver.find_element_by_xpath('/html/body/div[1]/section[1]/div/div/form/div[2]/div/div[1]')
    select.click()

    select=driver.find_element_by_xpath('/html/body/div[1]/section[1]/div/div/form/div[2]/div/div[2]/ul/li[3]')
    select.click()

    select=driver.find_element_by_xpath('/html/body/div[1]/section[1]/div/div/form/div[1]/div[1]')
    select.click()

    countries=[11,15,20,27,52,53,55,61,65,70,74,78,90,98,103,108,110,116,117,119,132,143,146,153,163,169,170,188,189,201,202,205,213,218,219,221,75]
    crandom=random.choice(countries)
#    print (crandom)
    co=driver.find_element_by_xpath('/html/body/div[1]/section[1]/div/div/form/div[1]/div[2]/ul/li['+str(crandom)+']')
#    print (co.text)
    ph=PhoneNumber(co.text)
    tn=ph.get_number(full=False)
#    _log (tn)
    co.click()

    tns=str(tn)
    phone=driver.find_element_by_id('live_phone')
    phone.send_keys(tns)

    select=driver.find_element_by_xpath('/html/body/div[1]/section[1]/div/div/form/div[3]/label')
    select.click()
    
    select=driver.find_element_by_xpath('/html/body/div[1]/section[1]/div/div/form/div[4]/label')
    select.click()
    
    driver.execute_script('document.getElementById("live_check").checked=true;')
    b=driver.find_element_by_xpath('/html/body/div[1]/section[1]/div/div/form/button')
    b.click()
#    time.sleep(10)
#    _log(driver.page_source)

    driver.switch_to.window(driver.window_handles[1])

    try:
        r = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="__layout"]/div/aside/div[1]/div[2]/div/div/ul/li/div[1]')))
    except:
        print ("timeout")
        driver.close()
        driver.quit()
        pass
    r.click()
    print ("found")
    try:
        r = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="__layout"]/div/main/div/div[1]/div/div[1]/article/div/div[3]/span/div/center/table/tbody/tr/td/table/tbody/tr[3]/td/table/tbody/tr/td/div/p[6]/a')))
    except:
        print ("timeout clicking")
        driver.close()
        driver.quit()
        pass


    r.click()
    time.sleep(1)
    r=_get_text('//*[@id="__layout"]/div/main/div/div[1]/div/div[1]/article/div/div[3]/span/div/center/table/tbody/tr/td/table/tbody/tr[3]/td/table/tbody/tr/td')
    _log(r)
    return True




def ingo_reg():
#    driver.maximize_window()
    driver.delete_all_cookies()
    driver.get("https://ingoinvest.com/ru/register")

#    time.sleep(10)
#    _log(driver.page_source)

    driver.execute_script("window.open('about:blank', 'tab2');")
    driver.switch_to.window("tab2")
    driver.get('https://temp-mail.io/en')
    time.sleep(3)
#    _log(driver.page_source)
    email=driver.find_element_by_id('email').get_attribute('value')
    _log(email)
    driver.switch_to.window(driver.window_handles[0])
    e=driver.find_element_by_xpath('//*[@id="live_email"]')
    e.send_keys(email)

    name1=driver.find_element_by_xpath('//*[@id="live_name"]')
    name1.send_keys(name)

    last_name=driver.find_element_by_xpath('//*[@id="live_last_name"]')
    last_name.send_keys(surname)
    

    select=driver.find_element_by_xpath('//*[@id="wrapper"]/main/div[2]/article/form/div[4]/div/div[1]')
    select.click()

    select=driver.find_element_by_xpath('//*[@id="wrapper"]/main/div[2]/article/form/div[4]/div/div[2]/ul/li[5]')
    select.click()

    select=driver.find_element_by_xpath('//*[@id="wrapper"]/main/div[2]/article/form/div[4]/div/div[1]')
    select.click()
    
    
#    sys.exit()
#    select=driver.find_element_by_xpath('/html/body/div[1]/section[1]/div/div/form/div[1]/div[1]')
#    select.click()

    countries=[11,15,20,27,52,53,55,61,70,74,78,90,98,103,108,110,116,117,119,132,143,146,153,163,170,188,189,201,202,205,213,218,219,221,75]
    crandom=random.choice(countries)
    print (crandom)
    co=driver.find_element_by_xpath('//*[@id="wrapper"]/main/div[2]/article/form/div[4]/div/div[2]/ul/li['+str(crandom)+']')
    print (co.text)
    ph=PhoneNumber(co.text)
    tn=ph.get_number(full=False)
    _log (tn)
    co.click()

    tns=str(tn)
    phone=driver.find_element_by_id('live_phone')
    phone.send_keys(tns)
#checkbox1
    select=driver.find_element_by_xpath('//*[@id="wrapper"]/main/div[2]/article/form/div[8]/label')
    select.click()
    
    select=driver.find_element_by_xpath('//*[@id="wrapper"]/main/div[2]/article/form/div[9]/label')
    select.click()
    _click('//*[@id="wrapper"]/main/div[2]/article/form/div[7]/div/div[1]/div[1]')
    _click('//*[@id="wrapper"]/main/div[2]/article/form/div[7]/div/div[2]/ul/li[4]')
    print ("before live check")    
    driver.execute_script('document.getElementById("live_check").checked=true;')
    b=driver.find_element_by_xpath('//*[@id="wrapper"]/main/div[2]/article/form/button')
    b.click()
    time.sleep(10)
#    _log(driver.page_source)
#    sys.exit()
    driver.switch_to.window(driver.window_handles[1])
#    time.sleep(100000)
    try:
#        r = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="__layout"]/div/aside/div[1]/div[2]/div/div/ul/li/div[1]')))
        r = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="__layout"]/div/aside/div[1]/div[2]/div/div/ul/li/div[5]/span')))
    except:
        print ("timeout")
        driver.close()
        driver.quit()
        pass
    r.click()
    print ("found")
    try:
        r = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="__layout"]/div/main/div/div[1]/div/div[1]/article/div/div[3]/span/div/center/table/tbody/tr/td/table/tbody/tr[3]/td/table/tbody/tr/td/div/p[6]/a')))

    except:
        print ("timeout clicking")
        driver.close()
        driver.quit()
        pass


    r.click()
    time.sleep(1)
    r=driver.find_element_by_xpath('//*[@id="__layout"]/div/main/div/div[1]/div/div[1]/article/div/div[3]/span/div/center/table/tbody/tr/td/table/tbody/tr[3]/td/table/tbody/tr/td').text
    _log (r)


#    sys.exit()
    return True



def ptrend_reg():
#   import json
    co2=random.choice(['RU','FR','AT','AZ','AM','BY','BE','BG','GB','DE','GR','GE','DK','ES','IT','KZ','KG','LU','MC','NL','NO','PT','RU','RS','SK','TR','UZ','FI','FR','HR','CZ','CH','SE'])
#    phone_rus=PhoneNumber("Russia").get_number(full=False)
    phone_rus=PhoneNumber(co2).get_number(full=False)

    pass1='abFgfarG'+password
    payload= {"fullName": "\u0421\u0432\u0435\u0442\u043b\u0430\u043d\u0430 \u0410\u041d\u0434\u0440\u0435\u0435\u0432\u0430","email": "svertka54542002@gmail.com","country": "RU",  "Lang": "ru",  "countryPrefix": "",  "phone": "7524443502",  "password": "f6d3vwW3ViVwm4w",  "password repeatPassword": "f6d3vwW3ViVwm4w",  "linkID": "",  "checkbox": "on",  "firstName": "\u0421\u0432\u0435\u0442\u043b\u0430\u043d\u0430",  "lastName": "\u0410\u041d\u0434\u0440\u0435\u0435\u0432\u0430"}#good    payload= '{"fullName": "'+str((name+" "+surname).encode('ascii','backslashreplace')).replace('b\'','').replace("\\\\","\\").replace('\'','')+"\",\"email\": \""+email+'","country": "RU",  "Lang": "ru",  "countryPrefix": "",  "phone": "'+phone_rus+'",  "password": "'+pass1+'",  "password repeatPassword": "'+pass1+'",  "linkID": "",  "checkbox": "on",  "firstName": "'+str(name.encode('ascii','backslashreplace')).replace('b\'','').replace("\\\\","\\").replace('\'','')+'",  "lastName": "'+str(surname.encode('ascii','backslashreplace')).replace('b\'','').replace("\\\\","\\").replace('\'','')+'"}'
    payload= '{"fullName": "'+str((name+" "+surname).encode('ascii','backslashreplace')).replace('b\'','').replace("\\\\","\\").replace('\'','')+"\",\"email\": \""+email+'","country": "'+co2+'",  "Lang": "ru",  "countryPrefix": "",  "phone": "'+phone_rus+'",  "password": "'+pass1+'",  "password repeatPassword": "'+pass1+'",  "linkID": "",  "checkbox": "on",  "firstName": "'+str(name.encode('ascii','backslashreplace')).replace('b\'','').replace("\\\\","\\").replace('\'','')+'",  "lastName": "'+str(surname.encode('ascii','backslashreplace')).replace('b\'','').replace("\\\\","\\").replace('\'','')+'"}'


    _log(payload)
    result = os.popen('curl -s --header "Content-Type: application/json"  --request POST  --data \''+payload+'\'  https://prtrend.org/wp-json/xcritical/1.0/registration').read()
    _log(result)
    return True


def ptrend_chat(emailp,passwordp):
    driver.delete_all_cookies()
 
#    emailp="oksana700998@ru.ru"
#    passwordp="abFgfarG042805"
    driver.get("https://prtrend.org/authorization/")
    _wait_element('/html/body/div[2]/div/div[2]/div/form/div[1]/input')
    _send_text('/html/body/div[2]/div/div[2]/div/form/div[1]/input',emailp)
    _send_text('/html/body/div[2]/div/div[2]/div/form/div[2]/input',passwordp)
    _click('/html/body/div[2]/div/div[2]/div/form/button')
#    time.sleep(20)

    _wait_element('//*[@id="Capa_1"]')
    _click('//*[@id="Capa_1"]')
    _wait_element('/html/body/div[4]/div/div[3]/textarea')
    _send_text('/html/body/div[4]/div/div[3]/textarea',get_greet())
    webdriver.ActionChains(driver).send_keys(Keys.ENTER).perform()
    time.sleep(random.randint(3,10))
    q1=_get_question()
    _send_text('/html/body/div[4]/div/div[3]/textarea',q1)
    webdriver.ActionChains(driver).send_keys(Keys.ENTER).perform()
    _log(_get_text('/html/body/div[4]/div/div[2]'))
    time.sleep(random.randint(3,10))
    q2=ai(q1)
    _send_text('/html/body/div[4]/div/div[3]/textarea',q2)
    webdriver.ActionChains(driver).send_keys(Keys.ENTER).perform()
    time.sleep(random.randint(10,60))
    _log(_get_text('/html/body/div[4]/div/div[2]'))
    _log ("bored") 
#    time.sleep(1000)
#    maxi_chat()
    return True

#not working on their side
def ptrend_email():
    name241=_get_name()
    surname241=_get_surname()    
    f=_get_final_name(name241, surname241)
    email241=_get_email_from_final_name(f)
    driver.delete_all_cookies()
    driver.get("https://prtrend.org/kontakty/")
    _wait_element('/html/body/div[2]/div/div[2]/section/form/div[1]/input')
    _send_text('/html/body/div[2]/div/div[2]/section/form/div[1]/input',name241)
    _send_text('/html/body/div[2]/div/div[2]/section/form/div[2]/input',surname241)
    _send_text('/html/body/div[2]/div/div[2]/section/form/div[3]/input',email241)
    _send_text('/html/body/div[2]/div/div[2]/section/form/div[4]/input',get_phone_full())
    q1="aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    while (len(q1)>38):
        q1=_get_question()    
    q1=	q1.replace(',','').replace('.','').replace('?','').replace('!','').replace(':','').replace(';','').replace('(','').replace(')','').replace('0','').replace('1','').replace('2','').replace('3','').replace('4','').replace('5','').replace('6','').replace('7','').replace('8','')
    q1=q1.replace('9','')
    _send_text('/html/body/div[2]/div/div[2]/section/form/div[5]/input',q1)
    _send_text('/html/body/div[2]/div/div[2]/section/form/div[6]/textarea',ai(q1))
    _click('/html/body/div[2]/div/div[2]/section/form/button')    
    maxi_chat()
    time.sleep(1000)


    return True

def ptrend_chat_noreg():
    global q_ptrend_chat_noreg
    name241=_get_name()
    surname241=_get_surname()    
    f=_get_final_name(name241, surname241)
    email241=_get_email_from_final_name(f)

    driver.delete_all_cookies()
    driver.get("https://prtrend.org/kontakty/")
    time.sleep(random.randint(2,5))
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(random.randint(2,5))
    driver.execute_script("window.scrollTo(0, 0)")
    time.sleep(random.randint(2,5))
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    ban="ban"
    try:
        _wait_element5('//*[@id="cf-wrapper"]')
    except:
        ban="noban"
        pass
    if (ban!='noban'):
        q_ptrend_chat_noreg=0
        _log("diablinng q_ptrend_chat_noreg because of ban")


#    driver.save_screenshot("/test/screenshot.png")



    _wait_element('//*[@id="AskMeChatBot"]/div/div/img')
#    _click('//*[@id="AskMeChatBot"]/div/div/img')
    driver.execute_script('document.evaluate(\'//*[@id="AskMeChatBot"]/div/div/img\', document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue.click();')

#    _wait_element('//*[@id="AskMeChatBot"]/div/div')
#    _click('//*[@id="AskMeChatBot"]/div/div')


    _wait_element('//*[@id="AskMeChatBot"]/div/div[2]/div[2]/div[1]/div[2]/input')
    _send_text('//*[@id="AskMeChatBot"]/div/div[2]/div[2]/div[1]/div[2]/input',email241)
    _wait_element('//*[@id="AskMeChatBot"]/div/div[2]/div[2]/div[2]/div')
    _click('//*[@id="AskMeChatBot"]/div/div[2]/div[2]/div[2]/div')

    _wait_element('//*[@id="AskMeChatBot"]/div/div[2]/div[2]/div[1]/div[2]/input')
    _send_text('//*[@id="AskMeChatBot"]/div/div[2]/div[2]/div[1]/div[2]/input',f)
    _wait_element('//*[@id="AskMeChatBot"]/div/div[2]/div[2]/div[2]/div[1]')
    _click('//*[@id="AskMeChatBot"]/div/div[2]/div[2]/div[2]/div[1]')

    _wait_element('//*[@id="input-field"]')

    _send_text('//*[@id="input-field"]',get_greet())
    time.sleep(5)
    _wait_element('//*[@id="send-button"]/img')
    _click('//*[@id="send-button"]/img')

    time.sleep(random.randint(10,20))
    q1=_get_question()
    _send_text('//*[@id="input-field"]',q1)
    _click('//*[@id="send-button"]/img')

    for i in range(1,random.randint(3,6)):
        time.sleep(random.randint(10,20))
        questiont=data[random.randint(1,len(data)-1)].replace('\n', '')
        _send_text('//*[@id="input-field"]',questiont)
        time.sleep(random.randint(3,10))
        for y1 in range (1,100):
            _send_text('//*[@id="input-field"]',Keys.BACKSPACE)
            _send_text('//*[@id="input-field"]',Keys.DELETE)

        dialogue=_get_text('//*[@id="body-box"]/div/div')
        _log("ptrent dia: "+dialogue)
        q1=ai(q1)
        _send_text('//*[@id="input-field"]',q1)
        _click('//*[@id="send-button"]/img')
    _log("ptrend chat bored")        
#        stack.append(greet)


#    time.sleep(1000)
    return True

def lime_reg():
    driver.delete_all_cookies()
    driver.get("https://limefx.com/registration/")
    r=driver.find_element_by_xpath('//*[@id="RForm-0"]/form/div[1]/input')
    r.send_keys(name)
    r=driver.find_element_by_xpath('//*[@id="RForm-0"]/form/div[2]/input')
    r.send_keys(surname)

    _click('//*[@id="RForm-0"]/form/div[7]/select')
    _click('/html/body/section/div/div[2]/div[1]/div/div/form/div[7]/select/option[157]')
#    e=driver.find_element_by_id('//*[@id="RForm-0"]/form/div[5]/input')
#    e.send_keys("testing1235")

    ph=PhoneNumber('RU')
    tn=ph.get_number(full=False)
    print (tn)
    r=driver.find_element_by_xpath('//*[@id="txtPhone"]')
    r.send_keys(tn)
#    driver.execute_script("window.open('about:blank', 'tab2');")
#    driver.switch_to.window("tab2")
#    driver.get('https://temp-mail.io/en')
#    time.sleep(3)


#    _log(driver.page_source)
#    email=driver.find_element_by_id('email').get_attribute('value')
#    _log(email)
#    driver.switch_to.window(driver.window_handles[0])
#    time.sleep(3)
#    _click('//*[@id="RForm-0"]/form/div[4]/input')
#    _wait_element('//*[@id="RForm-0"]/form/div[4]/input')

    characters = "01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    bpassword="".join(random.sample(characters, 20))

    e=driver.find_element_by_xpath('//*[@id="RForm-0"]/form/div[4]/input')
    e.send_keys(email)
#    password=""
#    for i in range (1,4):
#        password=password+random.choice('abcdefghijklmnopqruvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
#    for i in range (1,3):
#        password=password+random.choice('0123456789')
    r=driver.find_element_by_xpath('//*[@id="RForm-0"]/form/div[5]/input')
    r.send_keys(bpassword)
    r=driver.find_element_by_xpath('//*[@id="RForm-0"]/form/div[6]/input')
    r.send_keys(bpassword)
    _log("lime: " +email+" "+bpassword)
    _wait_element('//*[@id="RForm-0"]/form/div[8]/button')
    _click('//*[@id="RForm-0"]/form/div[8]/button')
#    time.sleep(5)
#    _log(driver.page_source)
    time.sleep(10)
    driver.get('https://myaccountnew.limefx.com/personal-data/personal-data')
    time.sleep(10)
    _log("reg maybe ok")
#    _log(driver.page_source)

def lime_email():
    co2=['Австрия','Азербайджан','Армения','Бельгия','Болгария','Великобритания','Венгрия','Германия','Греция','Грузия','Дания','Испания','Италия','Казахстан','Кипр','Латвия','Литва','Молдова','Монако','Нидерланды','Норвегия','Польша','Португалия','Российская Федерация','Румыния','Словакия','Словения','Таджикистан','Узбекистан','Франция','Хорватия','Чешская Республика','Швейцария','Швеция']
    co2_choice=random.choice(co2)
    co2_dict={'Австрия':'AT','Азербайджан':'AZ','Армения':'AM','Бельгия':'BE','Болгария':'BG','Великобритания':'GB','Венгрия':'HU','Германия':'DE','Греция':'GR','Грузия':'GE','Дания':'DK','Испания':'ES','Италия':'IT','Казахстан':'KZ','Кипр':'CY','Латвия':'LV','Литва':'LT','Молдова':'MD','Монако':'MC','Нидерланды':'NL','Норвегия':'NO','Польша':'PL','Португалия':'PT','Российская Федерация':'RU','Румыния':'RO','Словакия':'SK','Словения':'SI','Таджикистан':'TJ','Узбекистан':'UZ','Франция':'FR','Хорватия':'HR','Чешская Республика':'CZ','Швейцария':'CH','Швеция':'SE'}
    co2_code=co2_dict[co2_choice]
    _log(co2_choice+co2_code)
#    sys.exit()
    driver.delete_all_cookies()
    driver.get("https://limefx.com/about-us/feedback/")
    r=driver.find_element_by_xpath('//*[@id="wpcf7-f5877-o1"]/form/div[2]/div[1]/div[1]/span/input')
    r.send_keys(name)
    r=driver.find_element_by_xpath('//*[@id="wpcf7-f5877-o1"]/form/div[2]/div[1]/div[2]/span/input')
    r.send_keys(surname)
    _click('//*[@id="wpcf7-f5877-o1"]/form/div[2]/div[3]/div[1]/span/select')
    _click('//*[@id="wpcf7-f5877-o1"]/form/div[2]/div[3]/div[1]/span/select/option[text()=\''+co2_choice+'\']')
    _send_text('//*[@id="wpcf7-f5877-o1"]/form/div[2]/div[2]/div[1]/span/input',email)
    ph=PhoneNumber(co2_code)
    tn=ph.get_number(full=True)
    _send_text('//*[@id="wpcf7-f5877-o1"]/form/div[2]/div[2]/div[2]/span/input',tn)
    _send_text('//*[@id="wpcf7-f5877-o1"]/form/div[2]/div[3]/div[2]/span/input',question)
    q2=question
    dice=random.choice([1,2,3,4,5])
    if (dice==3):
        q2=question2
    _log(q2)
    _send_text('//*[@id="wpcf7-f5877-o1"]/form/div[2]/div[3]/div[3]/span/textarea',q2)
#    time.sleep(1000)
    _click('//*[@id="wpcf7-f5877-o1"]/form/div[2]/div[4]/input')
    _wait_element('//*[@id="wpcf7-f5877-o1"]/form/div[3]')
    _log(driver.find_element_by_xpath('//*[@id="wpcf7-f5877-o1"]/form/div[3]').text)



def plus_reg():
    driver.delete_all_cookies()
    driver.get("https://pulse-trade.com/register")
    _send_text('//*[@id="front_promo"]/div/div/form/div[1]/div[2]/div[1]/input',name)
    _send_text('//*[@id="front_promo"]/div/div/form/div[1]/div[2]/div[2]/input',surname)
    _send_text('//*[@id="front_promo"]/div/div/form/div[1]/div[1]/div[1]/input', email)
    password=random.choice(['A','B','C','D','E','F'])
    for i in range (1,6):
        password=password+random.choice('abcdefghijklmnopqruvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    for i in range (1,4):
        password=password+random.choice('0123456789')
    password=password+'*'
    _log(email)
    _log (password)
    _send_text('//*[@id="front_promo"]/div/div/form/div[1]/div[1]/div[2]/input',password)
    _send_text('//*[@id="front_promo"]/div/div/form/div[1]/div[1]/div[3]/input',password)
    _click('//*[@id="front_promo"]/div/div/form/div[2]/div/input')
    co2=['Австрия','Азербайджан','Армения','Бельгия','Болгария','Великобритания','Венгрия','Германия','Греция','Грузия','Дания','Испания','Италия','Казахстан','Кипр','Латвия','Литва','Молдова','Монако','Нидерланды','Норвегия','Польша','Португалия','Российская Федерация','Румыния','Словакия','Словения','Таджикистан','Узбекистан','Франция','Хорватия','Чешская Республика','Швейцария','Швеция']
    co2_choice=random.choice(co2)
    co2_dict={'Австрия':'AT','Азербайджан':'AZ','Армения':'AM','Бельгия':'BE','Болгария':'BG','Великобритания':'GB','Венгрия':'HU','Германия':'DE','Греция':'GR','Грузия':'GE','Дания':'DK','Испания':'ES','Италия':'IT','Казахстан':'KZ','Кипр':'CY','Латвия':'LV','Литва':'LT','Молдова':'MD','Монако':'MC','Нидерланды':'NL','Норвегия':'NO','Польша':'PL','Португалия':'PT','Российская Федерация':'RU','Румыния':'RO','Словакия':'SK','Словения':'SI','Таджикистан':'TJ','Узбекистан':'UZ','Франция':'FR','Хорватия':'HR','Чешская Республика':'CZ','Швейцария':'CH','Швеция':'SE'}
    co2_code=co2_dict[co2_choice]
    ph=PhoneNumber(co2_code)
    tn=ph.get_number(full=True)
    _send_text('//*[@id="front_promo"]/div/div/form/div[1]/div[2]/div[4]/input',tn)

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(random.randint(1,3))
    _click('//*[@id="front_promo"]/div/div/form/div[2]/div/input')
    driver.execute_script("window.scrollTo(0, 0);")
    _click('//*[@id="front_promo"]/div/div/form/div[2]/div/input')

    action = webdriver.ActionChains(driver)
    element = driver.find_element_by_xpath('//*[@id="front_promo"]/div/div/form/div[1]/div[2]/div[1]/input') # or your another selector here
#    action.move_to_element(element)
    human_like_mouse_move(action, element)
    action.perform()
    time.sleep(random.randint(1,3))
    _click('//*[@id="front_promo"]/div/div/form/div[2]/div/input')
    element = driver.find_element_by_xpath('//*[@id="front_promo"]/div/div/form/div[1]/div[2]/div[2]/input') # or your another selector here
    time.sleep(random.randint(1,3))
    _click('//*[@id="front_promo"]/div/div/form/div[2]/div/input')
    human_like_mouse_move(action, element)
    element = driver.find_element_by_xpath('//*[@id="front_promo"]/div/div/form/div[1]/div[1]/div[1]/input') # or your another selector here
    human_like_mouse_move(action, element)
    time.sleep(1.4)
    _click('//*[@id="front_promo"]/div/h1')
#    check_box=    WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.ID,"front_promo")))
#    human_like_mouse_move(action, check_box)
    _wait_element('//*[@id="recaptcha-anchor"]/div[1]')



    _click('//*[@id="recaptcha-anchor"]/div[1]')
    time.sleep(3)
    _click('//*[@id="front_promo"]/div/div/form/button')
    _wait_element('//*[@id="system_message"]/div[1]/div/div/div[2]')
    r=driver.find_element_by_xpath('//*[@id="system_message"]/div[1]/div/div/div[2]').text
    _log(r)

def plus_email():    
    driver.delete_all_cookies()
    driver.get("https://pulse-trade.com/contacts")
    _send_text('//*[@id="rec246689055"]/div/div/div[3]/div[1]/form/div[1]/input', final_name)
    _send_text('//*[@id="rec246689055"]/div/div/div[3]/div[1]/form/div[2]/input', email)
    _send_text('//*[@id="rec246689055"]/div/div/div[3]/div[1]/form/div[3]/textarea',question)
    _click('//*[@id="rec246689055"]/div/div/div[3]/div[1]/form/div[4]/input')
    _wait_element('//*[@id="system_message"]/div[1]/div/div/div[2]')
    r=driver.find_element_by_xpath('//*[@id="system_message"]/div[1]/div/div/div[2]').text
    _log(r)
#    time.sleep(1000)


#chat unavailable
def ingo_chat_online():
    driver.get("https://ingoinvest.com/ru")

    #click on banner j i v oc hat
    _wait_element('//*[@id="jvlabelWrap"]/jdiv[1]')
    _click('//*[@id="jvlabelWrap"]/jdiv[1]')

    #name
    _wait_element('//*[@id="jcont"]/jdiv[3]/jdiv/jdiv[3]/jdiv/jdiv/jdiv[2]/form/jdiv[1]/input')
    _send_text('//*[@id="jcont"]/jdiv[3]/jdiv/jdiv[3]/jdiv/jdiv/jdiv[2]/form/jdiv[1]/input', final_name)

#phone
    _wait_element('//*[@id="jcont"]/jdiv[3]/jdiv/jdiv[3]/jdiv/jdiv/jdiv[2]/form/jdiv[2]/input')
    _send_text('//*[@id="jcont"]/jdiv[3]/jdiv/jdiv[3]/jdiv/jdiv/jdiv[2]/form/jdiv[2]/input',phone_full)

#emial
    _wait_element('//*[@id="jcont"]/jdiv[3]/jdiv/jdiv[3]/jdiv/jdiv/jdiv[2]/form/jdiv[3]/input')
    _send_text('//*[@id="jcont"]/jdiv[3]/jdiv/jdiv[3]/jdiv/jdiv/jdiv[2]/form/jdiv[3]/input',email)

#message
    _wait_element('//*[@id="jcont"]/jdiv[3]/jdiv/jdiv[3]/jdiv/jdiv/jdiv[2]/form/jdiv[4]/textarea')
    _send_text('//*[@id="jcont"]/jdiv[3]/jdiv/jdiv[3]/jdiv/jdiv/jdiv[2]/form/jdiv[4]/textarea',question)

    _click('//*[@id="jcont"]/jdiv[3]/jdiv/jdiv[3]/jdiv/jdiv/jdiv[2]/form/jdiv[5]')

    time.sleep(1000)
    return True




def jivochat_online(url):
    question=_get_question()
    driver.delete_all_cookies()
    driver.get(url)
    #click on banner jivochat
    _wait_element('//*[@id="jvlabelWrap"]/jdiv[1]')
    _click('//*[@id="jvlabelWrap"]/jdiv[1]')

    _wait_element('//*[@id="jcont"]/jdiv[3]/jdiv/jdiv[3]/jdiv[1]/jdiv[1]/textarea')
    _send_text('//*[@id="jcont"]/jdiv[3]/jdiv/jdiv[3]/jdiv[1]/jdiv[1]/textarea',question)
    webdriver.ActionChains(driver).send_keys(Keys.ENTER).perform()
#    jivochat_3questions()
#    time.sleep(1000)


    #name
  
    _wait_element('//*[@id="scrollbar-container"]/jdiv[1]/jdiv/jdiv[3]/jdiv/jdiv/jdiv/jdiv/jdiv[1]/input')
    _send_text('//*[@id="scrollbar-container"]/jdiv[1]/jdiv/jdiv[3]/jdiv/jdiv/jdiv/jdiv/jdiv[1]/input', final_name)

#phone
    _wait_element('//*[@id="scrollbar-container"]/jdiv[1]/jdiv/jdiv[3]/jdiv/jdiv/jdiv/jdiv/jdiv[2]/input')
    _send_text('//*[@id="scrollbar-container"]/jdiv[1]/jdiv/jdiv[3]/jdiv/jdiv/jdiv/jdiv/jdiv[2]/input',phone_full)

#emial
    _wait_element('//*[@id="scrollbar-container"]/jdiv[1]/jdiv/jdiv[3]/jdiv/jdiv/jdiv/jdiv/jdiv[3]/input')
    _send_text('//*[@id="scrollbar-container"]/jdiv[1]/jdiv/jdiv[3]/jdiv/jdiv/jdiv/jdiv/jdiv[3]/input',email)
    _click('//*[@id="scrollbar-container"]/jdiv[1]/jdiv/jdiv[3]/jdiv/jdiv/jdiv/jdiv/jdiv[4]')


    #main start here
    q1=question
    for i in range(1,random.randint(2,10)):
        q1=ai(q1)    
        _send_text('//*[@id="jcont"]/jdiv[3]/jdiv/jdiv[3]/jdiv[1]/jdiv[1]/textarea',q1)
        webdriver.ActionChains(driver).send_keys(Keys.ENTER).perform()
        time.sleep(random.randint(1,10))
        print(_get_text('//*[@id="jcont"]/jdiv[3]/jdiv/jdiv[2]'))
    time.sleep(20)
    _log(_get_text('//*[@id="jcont"]/jdiv[3]/jdiv/jdiv[2]'))
#message
#   
#    _wait_element('//*[@id="jcont"]/jdiv[3]/jdiv/jdiv[3]/jdiv/jdiv/jdiv[2]/form/jdiv[4]/textarea')
#    _send_text('//*[@id="jcont"]/jdiv[3]/jdiv/jdiv[3]/jdiv/jdiv/jdiv[2]/form/jdiv[4]/textarea',q1)

#    _click('//*[@id="jcont"]/jdiv[3]/jdiv/jdiv[3]/jdiv/jdiv/jdiv[2]/form/jdiv[5]')

#    time.sleep(1000)
    return True





def maxi_reg():
    global q_maxi_reg
    global maxi_phone
    driver.delete_all_cookies()
    driver.get("https://maximarkets.org/registration/")

    ban="ban"
    try:
        _wait_element5('//*[@id="cf-wrapper"]')
    except:
        ban="noban"
        pass
    if (ban!='noban'):
        q_maxi_reg=0
        _log("diablinng q_maxi_reg because of CF ban")


    question=_get_question()
    name=_get_name()
    surname=_get_surname()
    final_name=_get_final_name(name,surname)
    email=_get_email_from_final_name(final_name)


#    _wait_element('//*[@id="open-account"]/a')
#    _wait_element('//*[@id="infinite-mobile-menu"]/a')
#    _click('//*[@id="infinite-mobile-menu"]/a')
#    time.sleep(3)
 #   _wait_element('//*[@id="menu-main-navigation"]/li[1]/div[1]/div/a')
#    _click('//*[@id="menu-main-navigation"]/li[1]/div[1]/div/a')
#    _wait_element('//*[@id="modalReg"]/div[2]/div/div/div[1]/div[1]')
#    _click('//*[@id="modalReg"]/div[2]/div/div/div[1]/div[1]')
    bph=PhoneNumber('BE')
    maxi_phone=bph.get_number(full=False)
    bpassword=''
    for i in range (1,6):
        bpassword=bpassword+random.choice('abcdefghijklmnopqruvwxyz')
    bpassword=bpassword+random.choice('ABCFDGGJKJETET')
    for i in range (1,4):
        bpassword=bpassword+random.choice('0123456789')
    print(bpassword)
#    _send_text('//*[@id="formPassword2"]','londoN123')
    _send_text('//*[@id="formPassword2"]',bpassword)
    _send_text('/html/body/div[5]/div[1]/div[7]/div[1]/div[1]/div/form/div[3]/div/div[2]/label/input',maxi_phone)
    _send_text('/html/body/div[5]/div[1]/div[7]/div[1]/div[1]/div/form/div[1]/div[1]/input',name)
    _send_text('/html/body/div[5]/div[1]/div[7]/div[1]/div[1]/div/form/div[1]/div[2]/input',surname)
    _send_text('//*[@id="formEmail"]',email)
    _click('/html/body/div[5]/div[1]/div[7]/div[1]/div[1]/div/form/div[5]/label/i')
    time.sleep(3)
    _click('/html/body/div[5]/div[1]/div[7]/div[1]/div[1]/div/form/div[8]/button')
    _wait_element('/html/body/div[5]/div[1]/h1')
    print(driver.find_element_by_xpath('/html/body/div[5]/div[1]/h1').text)
#    time.sleep(10)



def maxi_chat():    
    global maxi_phone
    stack=[]
#    driver.delete_all_cookies()
#    driver.get("https://maximarkets.org")
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    _wait_element('//*[@id="AskMeChatBot"]/div/div/img')
    _click('//*[@id="AskMeChatBot"]/div/div/img')

    _wait_element('//*[@id="AskMeChatBot"]/div/div[2]/div/div[2]/input')
    _send_text('//*[@id="AskMeChatBot"]/div/div[2]/div/div[2]/input',final_name)

    _wait_element('//*[@id="AskMeChatBot"]/div/div[2]/div/div[4]/input')
    _send_text('//*[@id="AskMeChatBot"]/div/div[2]/div/div[4]/input',email)

    _wait_element('//*[@id="AskMeChatBot"]/div/div[2]/div/button')
    _click('//*[@id="AskMeChatBot"]/div/div[2]/div/button')

    _wait_element('//*[@id="input-field"]')



    greet=get_greet()
    maxi_dice=random.randint(1,7)
    if ((maxi_dice==2)or(maxi_dice==1)):
        _send_text('//*[@id="input-field"]',greet)
        time.sleep(3)
        _wait_element('//*[@id="send-button"]/img')
        _click('//*[@id="send-button"]/img')
        stack.append(greet)


    prefix=random.choice(['','','','','','вот','почти','Вот','Вот,','Почти','Только что','только что','Зачем-то','Почему-то','Как-то','Недавно','Несколько минут назад','5 минут назад','15 минут назад','30 минут назад'])

    intro=random.choice(['Являюсь клиентом вашей комании ',
'зарегистрировалась',\
'зарегистрировалась 1 день назад',\
'зарегистрировалась 2 дня назад',\
'зарегистрировалась 3 дня назад',\
'зарегистрировалась 4 дня назад',\
'зарегистрировалась 5 дней назад',\
'зарегистрировалась 6 дней назад',\
'зарегистрировалась 7 дней назад',\
'зарегистрировалась 8 дней назад',\
'прошла регистрацию',\
'прошла официальную регистрацию',\
'я активный парнтер компании',\
'зарегистрировалась на портале',\
'являюсь полноценным клиентом',\
'стала полноценным клиентом',\
'я клиент компании',\
'я клиентка компании',\
'являюсь вип-клиентом компании',\
'я зарегистрированный пользовалтель',\
'я зарегистрированный активный пользовалтель',\
'я прошла то ли регистрацию, то ли верификацию',\
'Зарегистрировалась на платформе',\
'Зарегистрировалась на markets',\
'Являюсь клиенткой maximarkets',\
'зарегистрировалась на сайте макрект',\
'зарегистрировалась на сайте маркетс',\
'зарегистрировалась на сайте markets',\
'зарегистрировалась на вашем сайте',\
'зарегистрировалась',\
'зарегистрировалась на вашем официальном сайте','являюсь вашей клиенткой'])

    maxi_dice=random.randint(1,6)
    if (maxi_dice==2):
        time.sleep(random.randint(3,10))
        _send_text('//*[@id="input-field"]',prefix+" "+intro)
        stack.append(prefix+" "+intro)
        time.sleep(3)
        _wait_element('//*[@id="send-button"]/img')
        _click('//*[@id="send-button"]/img')
#    _click('//*[@id="send-button"]/img')
#    time.sleep(random.randint(30,60))
    em=random.choice(['E-mail при регистрации','у меня аккаунт:','моя почта', 'по адресу',\
'мой почтовый адрес','моя официальная почта',\
'я у вас зарегистрировалась по почте',\
'моя личная почта',\
'мой почтовый ящик',\
'мой финансовый почтовый ящик',\
'мой идентификатор почты',\
'email:',\
'адрес моей почты:',\
'вы можете найти мой аккаунт по почте',\
'вы можете найти мой аккаунт по email',\
'вы можете найти мой аккаунт по e-mail',\
'e-mail:',\
'мой E-mail:',\
'мой e-mail который я указала при регистрации:',\
'мой email'])

    maxi_dice=random.randint(1,5)
    if (maxi_dice==2):
        time.sleep(random.randint(3,10))
        _send_text('//*[@id="input-field"]',em+" "+email)
        stack.append(em+" "+email)
        _wait_element('//*[@id="send-button"]/img')
        _click('//*[@id="send-button"]/img')

        myself=random.choice(['Я',\
'я',\
'я,',\
'меня зовут',\
'Меня зовут',\
'моё имя',\
'Моё имя',\
'мое имя',\
'я зарегистрировалась как',\
'Я зарегистрировалась как',\
'Мои данные',\
'мои данные',\
'Мои паспортные данные',\
'мои паспортные данные',\
'Моё ФИО',\
'Мое ФИО',\
'мои имя, фамилия',\
'Мои имя, фамилия'])

        _send_text('//*[@id="input-field"]',myself+" "+final_name)
        stack.append(em+" "+email)
        _wait_element('//*[@id="send-button"]/img')
        _click('//*[@id="send-button"]/img')


    maxi_dice=random.randint(1,5)
    if (maxi_dice==2):
        time.sleep(random.randint(3,10))
        pm=random.choice(['мой номер телефона', 'Актуальный телефон', 'мой телефон', 'телефон:''мобильный телефон','телефонный номер',\
'личный телефон','мой личный телефон',\
'Сообщаю вам мой телефон для идентификации',\
'идентификация по телефону',\
'Мой телефонный номер',\
'Мой номер',\
'Телефон, по которому я регистрировалась',\
'Мой регистрационный номер',\
'Мой регистрационный номер телефона',\
'Мой регистрационный номер в системе',\
'Мой регистрационный номер в портале',\
'Мой регистрационный номер в системе макси',\
'мой номер',\
'Мой номер телефона в системе',\
'Мой номер телефона при регистрации',\
'Мой номер телефона в портале',\
'Мой номер телефона в maxi',\
'Phone','мобильный номер'])
        print(maxi_phone)
        _send_text('//*[@id="input-field"]',pm+" "+maxi_phone)
        stack.append(pm+" "+maxi_phone)
        _click('//*[@id="send-button"]/img')
    bored=0
    while (bored<4):
        print("bored "+str(bored))

        for y in range (1,4):
            questiont=data[random.randint(1,len(data)-1)].replace('\n', '')
            _send_text('//*[@id="input-field"]',questiont)
            time.sleep(random.randint(3,10))
            for y1 in range (1,100):
                _send_text('//*[@id="input-field"]',Keys.BACKSPACE)
                _send_text('//*[@id="input-field"]',Keys.DELETE)



        questiont=data[random.randint(1,len(data)-1)].replace('\n', '')
        _send_text('//*[@id="input-field"]',questiont)
        _click('//*[@id="send-button"]/img')
        stack.append(questiont)
        bored=bored+1
        dialogue=driver.find_element_by_xpath('//*[@id="body-box"]/div/div').text
        w=random.randint(5,60)
        for i in range(1,w):   
            dialogue1=driver.find_element_by_xpath('//*[@id="body-box"]/div/div').text
            print("DIA  before------------vvvvv----------------")
            print(dialogue)
            print("DIA 1 below VVVVVVVVVVVVVVVVVVVVV-------------")
            print(dialogue1)
            if (dialogue1 != dialogue):
                _log ("mosh typed")
                _log ("stack dump")
                print(stack)
                for line in dialogue1.splitlines():
                    if ((line not in stack) and (len(line)>25)):
                        print("this is answer: "+line)
                        stack.append(line)
                        answer=ai(line)
                        _send_text('//*[@id="input-field"]',answer)
                        _click('//*[@id="send-button"]/img')
                        stack.append(answer)
                        bored=0
                        i=w-1
            time.sleep(1)
    time.sleep(20)
    _log(dialogue1)
    return True 


def umarkets_reg():
    question=_get_question()
    name=_get_name()
    surname=_get_surname()
    final_name=_get_final_name(name,surname)
    email=_get_email_from_final_name(final_name)

    global maxi_phone
    driver.delete_all_cookies()
    driver.get("https://umarkets.info/ru/registration/")
    countries=[2,14,21,23,26,52,59,60,61,77,78,81,87,88,105,132,137,154,155,157,176,179,180,186,198,201,206,208,212,215,218,219,224]
    country=random.choice(countries)
    _click('//*[@id="RForm-0"]/form/div[7]/select/option['+str(country)+']')
    co2_choice=_get_text('//*[@id="RForm-0"]/form/div[7]/select/option['+str(country)+']')
    co2_code=co2_dict[co2_choice]
    ph=PhoneNumber(co2_code)
    maxi_phone=ph.get_number(full=False)
    _log(co2_code)
    _log(maxi_phone)
    try:
        _click('/html/body/div[1]/div[1]/div/div/button')
    except:
        pass

#    time.sleep(1000)
#    _wait_element('//*[@id="open-account"]/a')
#    _wait_element('//*[@id="infinite-mobile-menu"]/a')
#    _click('//*[@id="infinite-mobile-menu"]/a')
#    time.sleep(3)
 #   _wait_element('//*[@id="menu-main-navigation"]/li[1]/div[1]/div/a')
#    _click('//*[@id="menu-main-navigation"]/li[1]/div[1]/div/a')
#    _wait_element('//*[@id="modalReg"]/div[2]/div/div/div[1]/div[1]')
#    _click('//*[@id="modalReg"]/div[2]/div/div/div[1]/div[1]')
#    bph=PhoneNumber('BE')
#    maxi_phone=bph.get_number(full=False)
    characters = "01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    bpassword="".join(random.sample(characters, 20))
#    for i in range (1,6):
#        bpassword=bpassword+random.choice('abcdefghijklmnopqruvwxyz')
#    bpassword=bpassword+random.choice('ABCFDGGJKJETET')
#    for i in range (1,4):
#        bpassword=bpassword+random.choice('0123456789')
    print(bpassword)
#    _send_text('//*[@id="formPassword2"]','londoN123')
    _send_text('//*[@id="RForm-0"]/form/div[5]/input',bpassword)
    _send_text('//*[@id="RForm-0"]/form/div[6]/input',bpassword)

    _send_text('//*[@id="txtPhone"]',maxi_phone)

    _send_text('//*[@id="RForm-0"]/form/div[1]/input',name)
    _send_text('//*[@id="RForm-0"]/form/div[2]/input',surname)
    _send_text('//*[@id="RForm-0"]/form/div[4]/input',email)

    _click('//*[@id="RForm-0"]/form/div[9]/button')
    _log("umarkets reg "+email+" "+bpassword)
    return True



def marketbull_reg():
    global maxi_phone
    driver.delete_all_cookies()
    driver.get("https://client.marketbull.co.uk/sign-up")
    time.sleep(3)
    _wait_element('//*[@id="root"]/div/div/div/div/div[2]/form/div[1]/div/div[1]/div[1]/div[1]/input')
    _send_text('//*[@id="root"]/div/div/div/div/div[2]/form/div[1]/div/div[1]/div[1]/div[1]/input',name)

    _send_text('//*[@id="root"]/div/div/div/div/div[2]/form/div[1]/div/div[1]/div[2]/div[1]/input',surname)
    _send_text('//*[@id="root"]/div/div/div/div/div[2]/form/div[1]/div/div[1]/div[3]/div[1]/input',email)

    _send_text('//*[@id="root"]/div/div/div/div/div[2]/form/div[1]/div/div[1]/div[4]/div[1]/input','HongKong123')
    _send_text('//*[@id="root"]/div/div/div/div/div[2]/form/div[1]/div/div[1]/div[6]/div[1]/input',tnf)

    _click('//*[@id="root"]/div/div/div/div/div[2]/form/div[1]/div/div[2]/label')
    _click('//*[@id="root"]/div/div/div/div/div[2]/form/div[1]/div/div[3]/label')
    _click('//*[@id="root"]/div/div/div/div/div[2]/form/div[1]/div/div[4]/label')
    _click('//*[@id="root"]/div/div/div/div/div[2]/form/div[1]/div/div[5]/label')

    _click('//*[@id="root"]/div/div/div/div/div[2]/form/div[2]/button')
    time.sleep(1000)

def tradelabs_call():
    driver.maximize_window()
    driver.delete_all_cookies()
    driver.get("https://www.trade-labs.com/?lang=ru")
    _click('//*[@id="nav-menu-item-18877"]/a/span[1]')
    _wait_element('//*[@id="wpcf7-f18878-o1"]/form/p/span[2]/input')
    _send_text('//*[@id="wpcf7-f18878-o1"]/form/p/span[2]/input',final_name)
    _send_text('//*[@id="wpcf7-f18878-o1"]/form/p/span[3]/input',phone_full)
    _click('//*[@id="wpcf7-f18878-o1"]/form/p/input')
    _wait_element('//*[@id="wpcf7-f18878-o1"]/form/div[2]')
    print(_get_text('//*[@id="wpcf7-f18878-o1"]/form/div[2]'))
#    time.sleep(1000)
    return True
#    time.sleep(1000)

def global_chat():

    driver.delete_all_cookies()
#    time.sleep(60)

    driver.get("https://trade.globalallianceltd.com/registration-ru")
#    driver.get('https://globalliance.io/ru/')
#    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#    _wait_element('//*[@id="primary-menu"]/li[9]/div/a[2]')
 #   _click('//*[@id="primary-menu"]/li[9]/div/a[2]')
    _wait_element('//*[@id="user-fname-reg"]')
    _send_text('//*[@id="user-fname-reg"]',name)


    ph=PhoneNumber('RU')
    tn=ph.get_number(full=True)



    r=driver.find_element_by_xpath('//*[@id="user-phone-reg"]/input')
    _click('//*[@id="user-phone-reg"]/input')
    _send_text('//*[@id="user-phone-reg"]/input',Keys.BACKSPACE)
    _send_text('//*[@id="user-phone-reg"]/input',Keys.DELETE)
    _send_text('//*[@id="user-phone-reg"]/input',Keys.BACKSPACE)
    _send_text('//*[@id="user-phone-reg"]/input',Keys.DELETE)
    _send_text('//*[@id="user-phone-reg"]/input',Keys.BACKSPACE)
    _send_text('//*[@id="user-phone-reg"]/input',Keys.DELETE)
    _send_text('//*[@id="user-phone-reg"]/input',Keys.BACKSPACE)
    _send_text('//*[@id="user-phone-reg"]/input',Keys.DELETE)




#    r.clear()
#    time.sleep(2)
    _send_text('//*[@id="user-phone-reg"]/input',phone_full)


    _send_text('//*[@id="user-lname-reg"]',surname)
    _send_text('//*[@id="user-email-reg"]', email)




    password1="Global"+password
    _send_text('//*[@id="user-password-reg"]',password1)
    _click('//*[@id="user-birthday-reg"]')

    _wait_element('//*[@id="app"]/div[5]/div/div/div/div[2]/div[1]/div[1]/input')
    _click('//*[@id="app"]/div[5]/div/div/div/div[2]/div[1]/div[1]/input')
    bday=random.randint(1,27)
    _send_text('//*[@id="app"]/div[5]/div/div/div/div[2]/div[1]/div[1]/input',str(bday))

    _wait_element('//*[@id="app"]/div[5]/div/div/div/div[2]/div[1]/div[2]/input')
    _click('//*[@id="app"]/div[5]/div/div/div/div[2]/div[1]/div[2]/input')


    _wait_element('//*[@id="app"]/div[5]/div/div/div/div[2]/div[1]/div[2]/ul/section')
    _click('//*[@id="app"]/div[5]/div/div/div/div[2]/div[1]/div[2]/ul/section')

    byear=random.randint(1950,2000)
    _send_text('//*[@id="app"]/div[5]/div/div/div/div[2]/div[1]/div[3]/input',byear)

    _wait_element('//*[@id="app"]/div[5]/div/div/div/div[2]/div[2]/button[1]')
    _click('//*[@id="app"]/div[5]/div/div/div/div[2]/div[2]/button[1]')



    _wait_element('//*[@id="app"]/div[5]/div/section/div[1]/div/div[2]/div/form/div[8]/button/span')
    _click('//*[@id="app"]/div[5]/div/section/div[1]/div/div[2]/div/form/div[8]/button/span')

    #chat inside trade apph2.py//*[@id="right-sidebar"]/section/div[1]/button[7]

#    _wait_element('//*[@id="right-sidebar"]/section/div[1]/button[7]/span')
#    _wait_element('//*[@id="top-nav"]/div[2]/div[5]/div/div[1]/p[2]')
#    uid=_get_text('//*[@id="top-nav"]/div[2]/div[5]/div/div[1]/p[2]')
#    _log("global reg OK: "+email+" "+password1+" "+uid)
#    time.sleep(2000)
#    _click('//*[@id="right-sidebar"]/section/div[1]/button[7]/span')
 #   driver.execute_script('document.evaluate(\'//*[@id="right-sidebar"]/section/div[1]/button[7]\', document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue.click();')
#    time.sleep(5)  
#    _click('//*[@id="right-sidebar"]/section/div[1]/button[7]/span')
#    _wait_element('//*[@id="center"]/div[2]/div/div/div[2]/div[1]')
#    _click('//*[@id="center"]/div[2]/div/div/div[2]/div[1]')
#    _send_text('//*[@id="center"]/div[2]/div/div/div[2]/div[1]',question)
#    webdriver.ActionChains(driver).send_keys(Keys.ENTER).perform()
#    q2=ai(question)
 #   _send_text('//*[@id="center"]/div[2]/div/div/div[2]/div[1]',q2)
#    webdriver.ActionChains(driver).send_keys(Keys.ENTER).perform()
#    q3=ai(q2)
#    _send_text('//*[@id="center"]/div[2]/div/div/div[2]/div[1]',q3)
#    webdriver.ActionChains(driver).send_keys(Keys.ENTER).perform()
#    time.sleep(2)
#    _log(_get_text('//*[@id="center"]/div[2]/div/div/div[1]/section'))

#    time.sleep(3000)

    #chat here offline
#    _wait_element('//*[@id="jvlabelWrap"]/jdiv[2]')
#    _click('//*[@id="jvlabelWrap"]/jdiv[2]')

    #online
    _wait_element('//*[@id="jvlabelWrap"]/jdiv[1]')
    _click('//*[@id="jvlabelWrap"]/jdiv[1]')

    _wait_element('//*[@id="jcont"]/jdiv[3]/jdiv/jdiv[3]/jdiv/jdiv/jdiv/form/jdiv[1]/input')
    _send_text('//*[@id="jcont"]/jdiv[3]/jdiv/jdiv[3]/jdiv/jdiv/jdiv/form/jdiv[1]/input',final_name)

    _wait_element('//*[@id="jcont"]/jdiv[3]/jdiv/jdiv[3]/jdiv/jdiv/jdiv/form/jdiv[2]/input')
    _send_text('//*[@id="jcont"]/jdiv[3]/jdiv/jdiv[3]/jdiv/jdiv/jdiv/form/jdiv[2]/input',email)

    _wait_element('//*[@id="jcont"]/jdiv[3]/jdiv/jdiv[3]/jdiv/jdiv/jdiv/form/jdiv[3]/textarea')
    _send_text('//*[@id="jcont"]/jdiv[3]/jdiv/jdiv[3]/jdiv/jdiv/jdiv/form/jdiv[3]/textarea',question)
    _wait_element('//*[@id="jcont"]/jdiv[3]/jdiv/jdiv[3]/jdiv/jdiv/jdiv/form/jdiv[4]')
    _click('//*[@id="jcont"]/jdiv[3]/jdiv/jdiv[3]/jdiv/jdiv/jdiv/form/jdiv[4]')
#    webdriver.ActionChains(driver).send_keys(Keys.ENTER).perform()
    time.sleep(5)
    _wait_element('//*[@id="jcont"]/jdiv[3]/jdiv/jdiv[3]/jdiv[1]/jdiv[1]/textarea')
    q2=ai(question)    
    _send_text('//*[@id="jcont"]/jdiv[3]/jdiv/jdiv[3]/jdiv[1]/jdiv[1]/textarea',q2)
    webdriver.ActionChains(driver).send_keys(Keys.ENTER).perform()
    
    for i in range(1,5):
        try:
            _log(_get_text('//*[@id="jcont"]/jdiv[3]/jdiv/jdiv[1]/jdiv/jdiv/jdiv/jdiv[2]/jdiv/jdiv/jdiv[2]'))
            if ('Agents' not in _get_text('//*[@id="jcont"]/jdiv[3]/jdiv/jdiv[1]/jdiv/jdiv/jdiv/jdiv[2]/jdiv/jdiv/jdiv[2]')): 
                _log("-=mosh typed=-")
#            _log(_get_text('//*[@id="jcont"]/jdiv[3]/jdiv/jdiv[1]/jdiv/jdiv/jdiv/jdiv[2]/jdiv/jdiv[2]/jdiv[1]'))
                i=1
        except:
            pass
        time.sleep(random.randint(30,60))
        q3=ai(q2)    
        _send_text('//*[@id="jcont"]/jdiv[3]/jdiv/jdiv[3]/jdiv[1]/jdiv[1]/textarea',q3)
        webdriver.ActionChains(driver).send_keys(Keys.ENTER).perform()
        q2=q3



#//*[@id="jcont"]/jdiv[3]/jdiv/jdiv[3]/jdiv[1]/jdiv[2]/jdiv
     #offline
#    _wait_element('//*[@id="jcont"]/jdiv[3]/jdiv/jdiv[3]/jdiv[1]/jdiv[1]/textarea')
#    _send_text('//*[@id="jcont"]/jdiv[3]/jdiv/jdiv[3]/jdiv[1]/jdiv[1]/textarea',question)
#    webdriver.ActionChains(driver).send_keys(Keys.ENTER).perform()

#    _wait_element('//*[@id="scrollbar-container"]/jdiv[1]/jdiv/jdiv[4]/jdiv/jdiv/jdiv/jdiv/jdiv[1]/input')
#    _send_text('//*[@id="scrollbar-container"]/jdiv[1]/jdiv/jdiv[4]/jdiv/jdiv/jdiv/jdiv/jdiv[1]/input',final_name)
#    _send_text('//*[@id="scrollbar-container"]/jdiv[1]/jdiv/jdiv[4]/jdiv/jdiv/jdiv/jdiv/jdiv[2]/input',email)
#    _click('//*[@id="scrollbar-container"]/jdiv[1]/jdiv/jdiv[4]/jdiv/jdiv/jdiv/jdiv/jdiv[3]')

#    q2=ai(question)    
#    _wait_element('//*[@id="jcont"]/jdiv[3]/jdiv/jdiv[3]/jdiv[1]/jdiv[1]/textarea')
#    _send_text('//*[@id="jcont"]/jdiv[3]/jdiv/jdiv[3]/jdiv[1]/jdiv[1]/textarea',q2)
 #   webdriver.ActionChains(driver).send_keys(Keys.ENTER).perform()

#    q3=ai(q2)    
#    _wait_element('//*[@id="jcont"]/jdiv[3]/jdiv/jdiv[3]/jdiv[1]/jdiv[1]/textarea')
#    _send_text('//*[@id="jcont"]/jdiv[3]/jdiv/jdiv[3]/jdiv[1]/jdiv[1]/textarea',q3)
#    webdriver.ActionChains(driver).send_keys(Keys.ENTER).perform()

    _log(_get_text('//*[@id="scrollbar-container"]/jdiv[1]/jdiv'))
#    time.sleep(120)
#    time.sleep(1000)
    return True

def global_spam():
    driver.delete_all_cookies()
#    time.sleep(60)

    driver.get("https://trade.globalallianceltd.com/registration-ru")
    _wait_element('//*[@id="app"]/div[5]/div/section/div[1]/div/div[1]/div[1]')
    _click('//*[@id="app"]/div[5]/div/section/div[1]/div/div[1]/div[1]')
    _send_text('//*[@id="user-email"]','lilija840032@yandex.az')
    _send_text('//*[@id="user-password"]','Global840032')
    _click('//*[@id="app"]/div[5]/div/section/div[1]/div/div[2]/div/form/div[3]/button/span')
    time.sleep(5)  
    driver.execute_script('document.evaluate(\'//*[@id="right-sidebar"]/section/div[1]/button[7]\', document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue.click();')

#    _wait_element('//*[@id="right-sidebar"]/section/div[1]/button[7]/span')
#    _click('//*[@id="right-sidebar"]/section/div[1]/button[7]/span')
    _wait_element('//*[@id="center"]/div[2]/div/div/div[2]/div[1]')
    _click('//*[@id="center"]/div[2]/div/div/div[2]/div[1]')
    _send_text('//*[@id="center"]/div[2]/div/div/div[2]/div[1]',question)
    webdriver.ActionChains(driver).send_keys(Keys.ENTER).perform()
    q3=question
    for i in range(1,20000):
        q2=ai(q3)
        _send_text('//*[@id="center"]/div[2]/div/div/div[2]/div[1]',q2)
        webdriver.ActionChains(driver).send_keys(Keys.ENTER).perform()
        q3=q2
        time.sleep(2)        


def global_offline_chat():
    driver.delete_all_cookies()
    driver.get("https://trade.globalallianceltd.com/registration-ru")
    _wait_element('//*[@id="jvlabelWrap"]/jdiv[2]')
    _click('//*[@id="jvlabelWrap"]/jdiv[2]')
    _wait_element('//*[@id="jcont"]/jdiv[3]/jdiv/jdiv[3]/jdiv[1]/jdiv[1]/textarea')
    _send_text('//*[@id="jcont"]/jdiv[3]/jdiv/jdiv[3]/jdiv[1]/jdiv[1]/textarea',question)
    webdriver.ActionChains(driver).send_keys(Keys.ENTER).perform()
    _wait_element('//*[@id="scrollbar-container"]/jdiv[1]/jdiv/jdiv[4]/jdiv/jdiv/jdiv/jdiv/jdiv[1]/input')
    _send_text('//*[@id="scrollbar-container"]/jdiv[1]/jdiv/jdiv[4]/jdiv/jdiv/jdiv/jdiv/jdiv[1]/input',final_name)
    _send_text('//*[@id="scrollbar-container"]/jdiv[1]/jdiv/jdiv[4]/jdiv/jdiv/jdiv/jdiv/jdiv[2]/input',email)
    _click('//*[@id="scrollbar-container"]/jdiv[1]/jdiv/jdiv[4]/jdiv/jdiv/jdiv/jdiv/jdiv[3]')

    q2=ai(question)    
    _wait_element('//*[@id="jcont"]/jdiv[3]/jdiv/jdiv[3]/jdiv[1]/jdiv[1]/textarea')
    _send_text('//*[@id="jcont"]/jdiv[3]/jdiv/jdiv[3]/jdiv[1]/jdiv[1]/textarea',q2)
    webdriver.ActionChains(driver).send_keys(Keys.ENTER).perform()

    q3=ai(q2)    
    _wait_element('//*[@id="jcont"]/jdiv[3]/jdiv/jdiv[3]/jdiv[1]/jdiv[1]/textarea')
    _send_text('//*[@id="jcont"]/jdiv[3]/jdiv/jdiv[3]/jdiv[1]/jdiv[1]/textarea',q3)
    webdriver.ActionChains(driver).send_keys(Keys.ENTER).perform()


    time.sleep(10)


def _get_email():
    domain=random.choice(domains)
    password=""
    for i in range (1,7):
        password=password+random.choice('01234567890')
    username=translit(final_name, reversed=True).replace(" ", "_").replace("'","").lower()+password
    email=username+"@"+domain
    return email

def _get_email_from_final_name(final_name):
    domain=random.choice(domains)
    password=""
    for i in range (1,random.randint(5,8)):
        password=password+random.choice('01234567890')
    word=random.choice(wordlist10000).replace("\n","")
    word2=random.choice(wordlist10000).replace("\n","")
    dice=random.choice([1,2,3,4])
    if (dice==1):
        username=translit(final_name, reversed=True).replace(" ", "_").replace("'","").lower()+password
    if (dice==2):
        username=(word+word2).replace(" ", "_").replace("'","").lower()+password
    if (dice==3):
        username=(word+translit(final_name, reversed=True)).replace(" ", "_").replace("'","").lower()+password
    if (dice==4):
        username=(translit(final_name, reversed=True)+word).replace(" ", "_").replace("'","").lower()+password


#    print (username)
    email=username+"@"+domain
    return email



def _get_name():
    name=names[random.randint(1,len(names)-1)].replace('\n', '')
    return name

def _get_surname():
    surname=surnames[random.randint(1,len(surnames)-1)].replace('\n', '')
    return surname

def get_final_name():
    name=names[random.randint(1,len(names)-1)].replace('\n', '')
    surname=surnames[random.randint(1,len(surnames)-1)].replace('\n', '')
    dice=random.choice([1,2,3])
#    _log (dice)
    if (dice==1):
        final_name=name
    if (dice==2):
        final_name=name+" "+surname
    if (dice==3):
        final_name=surname+" "+name
    return final_name

def _get_final_name(name, surname):
    dice=random.choice([1,2,3])
#    _log (dice)
    if (dice==1):
        final_name=name
    if (dice==2):
        final_name=name+" "+surname
    if (dice==3):
        final_name=surname+" "+name
    return final_name


def _get_question():
    question=data[random.randint(1,len(data)-1)].replace('\n', '')
    return question


def get_phone_full():
    country=countries[random.randint(1,len(countries)-1)].replace('\n', '')
#    _log(country)

    #phone # depends on conutry
    ph=PhoneNumber(country)

    tn2=ph.get_number(full=True)
    phone_full=ph.get_number()
    return phone_full


#    _log(name)


def st24online_phone():
    driver.delete_all_cookies()
    driver.get('https://st24online.com/contact/?lang=ru#')
    _wait_element('/html/body/div[1]/div/header/div/div/div/div[1]/div[1]/span/i')
    _click('/html/body/div[1]/div/header/div/div/div/div[1]/div[1]/span/i')
    _wait_element('//*[@id="mobile-menu-item-784"]/a/span')
    _click('//*[@id="mobile-menu-item-784"]/a/span')
    for i in range(1,random.randint(100,200)):
        final_name=get_final_name()
        phone_full=get_phone_full()
        _wait_element('//*[@id="drop_down_callBack"]/p[1]/span/input')
        _clear('//*[@id="drop_down_callBack"]/p[1]/span/input')
        _clear('//*[@id="drop_down_callBack"]/p[2]/span/input')
        _send_text('//*[@id="drop_down_callBack"]/p[1]/span/input',final_name)
        _send_text('//*[@id="drop_down_callBack"]/p[2]/span/input',phone_full)
        _click('//*[@id="drop_down_callBack"]/p[3]/input')
        _wait_element('//*[@id="wpcf7-f777-o1"]/form/div[3]')
        print(final_name+phone_full+_get_text('//*[@id="wpcf7-f777-o1"]/form/div[3]'))
    time.sleep(10)
    return True

def st24online_reg():
    name241=_get_name()
    surname241=_get_surname()    
    f=_get_final_name(name241, surname241)
    email24=_get_email_from_final_name(f)
    driver.delete_all_cookies()
    driver.get('https://st24online.com/contact/?lang=ru#')
    _wait_element('/html/body/div[1]/div/header/div/div/div/div[1]/div[1]/span/i')
    _click('/html/body/div[1]/div/header/div/div/div/div[1]/div[1]/span/i')

    _wait_element('//*[@id="mobile-menu-item-786"]/a/span')
    _click('//*[@id="mobile-menu-item-786"]/a/span')
    _wait_element('//*[@id="frm_register"]/input[3]')
    _send_text('//*[@id="frm_register"]/input[3]',surname241)
    _send_text('//*[@id="frm_register"]/input[4]',name241)
    _send_text('//*[@id="emailRegister"]',email24)
    characters = "01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    bpassword="".join(random.sample(characters, 10))

    _send_text('//*[@id="passwordRegister"]',bpassword )
    _send_text('//*[@id="confirm_password"]',bpassword)

#    _click('//*[@id="country"]')
    c1=random.choice(co2)
    c11=co2_dict[c1]


    _click('//*[@id="'+c11+'"]')

    ph=PhoneNumber(c11)
    st24_ph=ph.get_number(full=False)

#    _clear('//*[@id="telephone"]')
    _send_text('//*[@id="telephone"]',st24_ph)
    _click('//*[@id="terms_conditions"]')
    _click('//*[@id="checkbox2"]')
#    time.sleep(10)
    _click('//*[@id="frm_register"]/button')
    _wait_element60('//*[@id="my-header"]/div[1]/a[2]/span/span[2]/span[1]')
    print(_get_text('//*[@id="my-header"]/div[1]/a[2]/span/span[2]/span[1]'))
    _log("#st24 "+name241+" "+surname241+" "+email24+" "+bpassword)
    _cred("#st24",email24,bpassword)
    return True
 


def st24online_email():
    driver.delete_all_cookies()
    driver.get('https://st24online.com/contact/?lang=ru#')
    _wait_element('//*[@id="wpcf7-f767-p761-o2"]/form/div[4]/span/textarea')
    q3=question
    for i in range (1,random.randint(10,70)):

        name24=_get_name()
        surname24=_get_surname()
        email24=_get_email()
        _clear('//*[@id="wpcf7-f767-p761-o2"]/form/div[2]/div[1]/div/span/input')
        _send_text('//*[@id="wpcf7-f767-p761-o2"]/form/div[2]/div[1]/div/span/input',name24)

        _clear('//*[@id="wpcf7-f767-p761-o2"]/form/div[2]/div[2]/div/span/input')
        _send_text('//*[@id="wpcf7-f767-p761-o2"]/form/div[2]/div[2]/div/span/input',surname24)

        _clear('//*[@id="wpcf7-f767-p761-o2"]/form/div[3]/div[1]/div/span/input')
        _send_text('//*[@id="wpcf7-f767-p761-o2"]/form/div[3]/div[1]/div/span/input',email24)

        _clear('//*[@id="wpcf7-f767-p761-o2"]/form/div[4]/span/textarea')
        q2=ai(question)
        _send_text('//*[@id="wpcf7-f767-p761-o2"]/form/div[3]/div[2]/div/span/input',q2)
        _send_text('//*[@id="wpcf7-f767-p761-o2"]/form/div[4]/span/textarea',q3)
        _click('//*[@id="wpcf7-f767-p761-o2"]/form/div[5]/input')
        _wait_element('//*[@id="wpcf7-f767-p761-o2"]/form/div[6]')
        _log(_get_text('//*[@id="wpcf7-f767-p761-o2"]/form/div[6]'))
        q3=ai(" ")
    return True


def toptrade_email():

    driver.delete_all_cookies()
    driver.get('https://toptrade.group/ru/contacts/')
    _wait_element('//*[@id="wpcf7-f4493-p3896-o1"]/form/p[1]/span/input')
    
    for i in range (1,random.randint(10,70)):

        name241=_get_name()
        surname241=_get_surname()    
        f=_get_final_name(name241, surname241)
        email24=_get_email_from_final_name(f)
        q1=_get_question()
        _clear('//*[@id="wpcf7-f4493-p3896-o1"]/form/p[1]/span/input')
        _clear('//*[@id="wpcf7-f4493-p3896-o1"]/form/p[2]/span/input')
        _clear('//*[@id="wpcf7-f4493-p3896-o1"]/form/p[3]/span/textarea')
        _send_text('//*[@id="wpcf7-f4493-p3896-o1"]/form/p[1]/span/input',name241)
        _send_text('//*[@id="wpcf7-f4493-p3896-o1"]/form/p[2]/span/input',email24)
        _send_text('//*[@id="wpcf7-f4493-p3896-o1"]/form/p[3]/span/textarea',q1)
        _click('//*[@id="wpcf7-f4493-p3896-o1"]/form/p[4]/input')
        _wait_element('//*[@id="wpcf7-f4493-p3896-o1"]/form/div[2]')
        print(_get_text('//*[@id="wpcf7-f4493-p3896-o1"]/form/div[2]'))
        q1=ai(q1)
    return True


def cryptogazprom_reg():
    driver.delete_all_cookies()
    for i in range(1,random.randint(1,100)):
        name241=_get_name()
        surname241=_get_surname()    
        f=_get_final_name(name241, surname241)
        email24=_get_email_from_final_name(f)
        phone_full=get_phone_full()

        driver.get('https://crypto-gazprom.com/')
        _wait_element('//*[@id="form2"]/div[1]/input')
        _clear('//*[@id="form2"]/div[1]/input')
        _send_text('//*[@id="form2"]/div[1]/input',name241)
        _clear('//*[@id="form2"]/div[2]/input')
        _send_text('//*[@id="form2"]/div[2]/input',surname241)
        _clear('//*[@id="form2"]/div[3]/input')
        _send_text('//*[@id="form2"]/div[3]/input',email24)
        _clear('//*[@id="form2"]/div[4]/input')
        _send_text('//*[@id="form2"]/div[4]/input', phone_full)
        _click('//*[@id="form2"]/div[5]/button')
        _wait_element('/html/body/div/div/p[2]')
        print(_get_text('/html/body/div/div/p[2]'))
#        time.sleep(1000)
    #reg done doing random doc
#    _wait_element('//*[@id="my-header"]/div[4]/div/a/span/i')
#    _click('//*[@id="my-header"]/div[4]/div/a/span/i')


 #   time.sleep(1000)


def gravity_reg():
    global q_gravity_reg
    driver.delete_all_cookies()
    name241=_get_name()
    surname241=_get_surname()    
    f=_get_final_name(name241, surname241)
    email24=_get_email_from_final_name(f)
    phone_full=get_phone_full()

    driver.get('https://clients.gravity-trade.com/ru')
    _wait_element('//*[@id="form-field-firstName"]')

    _send_text('//*[@id="form-field-firstName"]',name241)
    _send_text('//*[@id="form-field-lastName"]',surname241)
    _click('//*[@id="form-field-address__countryCode"]')
    countries=[11,14,15,20,21,28,34,45,55,57,58,59,64,68,73,74,80,81,84,98,104,106,107,112,115,117,119,124,125,126,128,142,144,145,153,155,162,173,174,148,179,179,179,179,190,192,197,198,204,210,211,214,223,224,230,234]
    crandom=random.choice(countries)
#    crandom=234



#    print (crandom)
    xp='//*[@id="form-field-address__countryCode"]/option['+str(crandom)+']'
    co=_get_text(xp)
#    co=driver.find_element_by_xpath('/html/body/div[1]/section[1]/div/div/form/div[1]/div[2]/ul/li['+str(crandom)+']')
#    print (co.text)
    ph=PhoneNumber(co)
    tn=ph.get_number(full=True)
    

    _click(xp)
#    _log(tn)
    _send_text('//*[@id="form-field-contacts__phone"]',tn)
    _send_text('//*[@id="form-field-contacts__email"]',email24)

    characters = "01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    pass1="".join(random.sample(characters, random.randint(9,14)))
    pass1=pass1+random.choice('0123456789')
    _send_text('//*[@id="form-field-password"]',pass1)
    _click('//*[@id="form-field-field_4"]')
    _click('//*[@id="form-field-field_1"]')
    _click('//*[@id="form-field-field_2"]')
    _click('//*[@id="form-field-field_3"]')
    _click('//*[@id="cp-crm-sign-up-form"]/div[1]/div[14]/button/span/span[2]')
    try:
        _wait_element5('//*[@id="cp-crm-sign-up-form"]/div[2]')
        ban=_get_text('//*[@id="cp-crm-sign-up-form"]/div[2]')
    except:
        ban="noban"
        pass
    _log(ban)
    if (ban!='noban'):
        q_gravity_reg=0
        _log("diablinng q_gravity reg")
    if (ban=="noban"):
   #     _log ("noban")
        _cred('#gravity',email24,pass1)
        time.sleep(6)
        _wait_element('//*[@id="support-callback"]')
        _click('//*[@id="support-callback"]')

        driver.switch_to.frame("iFrameResizer0")
        _wait_element('//*[@id="root"]/div/section/div[2]/div/button')
        _click('//*[@id="root"]/div/section/div[2]/div/button')
        _wait_element('//*[@id="root"]/div/section/div[2]/p[1]')
        _log(_get_text('//*[@id="root"]/div/section/div[2]/p[1]'))
#    time.sleep(2000)
#    driver.save_screenshot("/test/screenshot.png")
    return True


socket.setdefaulttimeout(10)
ptrade_done=0

def check_proxy(pip):
    global ptrend_people
    try:  
        co2=random.choice(['RU','FR','AT','AZ','AM','BY','BE','BG','GB','DE','GR','GE','DK','ES','IT','KZ','KG','LU','MC','NL','NO','PT','RU','RS','SK','TR','UZ','FI','FR','HR','CZ','CH','SE'])
        phone_rus=PhoneNumber(co2).get_number(full=False)
        name241=_get_name()
        surname241=_get_surname()    
        f=_get_final_name(name241, surname241)
        email241=_get_email_from_final_name(f)

#        pass1='abFgfarG'+password
        characters = "01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
        pass1="".join(random.sample(characters, 14))

        payload= '{"fullName": "'+str((name241+" "+surname241).encode('ascii','backslashreplace')).replace('b\'','').replace("\\\\","\\").replace('\'','')+"\",\"email\": \""+email241+'","country": "'+co2+'",  "Lang": "ru",  "countryPrefix": "",  "phone": "'+phone_rus+'",  "password": "'+pass1+'",  "password repeatPassword": "'+pass1+'",  "linkID": "",  "checkbox": "on",  "firstName": "'+str(name241.encode('ascii','backslashreplace')).replace('b\'','').replace("\\\\","\\").replace('\'','')+'",  "lastName": "'+str(surname241.encode('ascii','backslashreplace')).replace('b\'','').replace("\\\\","\\").replace('\'','')+'"}'

      
        proxy_handler = urllib.request.ProxyHandler({'https': pip})        
        opener = urllib.request.build_opener(proxy_handler)
        opener.addheaders = [('User-agent', 'Mozilla/5.0')]
        urllib.request.install_opener(opener)        
        sock=urllib.request.urlopen('https://prtrend.org')  # change the url address here
#        print(pip)
        req='curl -s --header "Content-Type: application/json"  --request POST  --data \''+payload+'\'  --proxy "'+pip+'"  https://prtrend.org/wp-json/xcritical/1.0/registration'
 #       print(req)

        result = os.popen(req).read()
#        print(result)
        if ("leadGuid" in result):
            print(":::::::::::: reg OK::::::::::::::")
            print(pip)
            _cred("#Ptrend",email241,pass1)
            ptrend_people[email241]=pass1
        
    except urllib.error.HTTPError as e:        
        return e
    except Exception as detail:
        return detail
    return 0


def threaded_proxy():
    socket.setdefaulttimeout(10)
                                                                                                                                        	
    response = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=https&timeout=7000&anonymity=elite&ssl=yes')
    q=[]
    for line in response.text.splitlines():
#        print (line)
        q.append(line)
#    print (q)
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

















#os.system('pkill chrome')

#random question
with open('phrases.txt', 'r',encoding="utf-8") as file:
    data = file.readlines()

with open('names_f.txt', 'r',encoding="utf-8") as file:
    names = file.readlines()

with open('surnames_f.txt', 'r',encoding="utf-8") as file:
    surnames = file.readlines()

with open('countries.txt', 'r',encoding="utf-8") as file:
    countries = file.readlines()

with open('wordlist10000.txt', 'r',encoding="utf-8") as file:
    wordlist10000 = file.readlines()


while True:

#    maxi_phone=''

    question=data[random.randint(1,len(data)-1)].replace('\n', '')
    question2=data[random.randint(1,len(data)-1)].replace('\n', '')
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

    tn2=ph.get_number(full=True)
    phone_full=ph.get_number()

    
    #    _log(tnf)

    #random full name choice
    dice=random.choice([1,2,3])
#    _log (dice)
    if (dice==1):
        final_name=name
    if (dice==2):
        final_name=name+" "+surname
    if (dice==3):
        final_name=surname+" "+name
    _log(final_name)

    dice=random.choice([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,21,22,23,20])
    if (dice==5):
        tick=nyse[random.randint(1,len(nyse)-1)].replace('\n', '')
        question="Мне аналитик посоветовал купить акции "+tick+" А ОНИ СЕГОДНЯ ОБВАЛИЛИСЬ! ВЕРНИТЕ МНЕ МОИ ДЕНЬГИ!!!"

    if (dice==6):
        card=str(random.randint(1000,9999))
        question="По поводу пополнения торгвого счета карточкой "+random.choice(['Visa ', 'Mastercard ', 'Мир ']) +card

    if (dice==7):
        hour=str(random.randint(1,23))
        minute=str(random.randint(1,59))
        question="Перезвоните мне по поводу активации счёта завтра в "+hour+':'+minute

    if (dice==8):
        name2=names[random.randint(1,len(names)-1)].replace('\n', '')
        question="Мне звонила ваш менеджер "+name2+" по поводу активации, оборвалось, перезвоните"

    if (dice==9):
        question=get_greet()



#    _log(question)


    #email
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
#    plus_reg()
#    try:
#        plus_reg()
#    except:
#        _log("plus reg fail")
#        pass
#    ai()
#    g=ai('Здравствуйте, я создам запрос, с вами свяжется ваш менеджер.')
#    print (g)
#    sys.exit()

#    while True:
#        driver = webdriver.Chrome(PATH, options=chrome_options)
#        tradelabs_call()
#        driver.close()
#        driver.quit()


#proxy here

#    socket.setdefaulttimeout(180)
                                                                                                                                            	
#    response = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=https&timeout=1000&anonymity=all&status=alive&ssl=yes&limit=10&lastupdated')
#    q=[]
#    for line in response.text.splitlines():
#        print (line)
#        q.append(line)
#    print (q)
#    proxyList = ['140.82.61.218:8080','178.32.47.218:17501'] # there are two sample proxy ip
#    proxyList =q






#    proxies = q
#    threads = []
#    good_proxy=[]
#    for proxy in proxies:
 #       thread = Thread( target=check_proxy, args=(proxy.strip(), ))
#        thread.start()
#        threads.append(thread)

#    for thread in threads:
#        thread.join()

#    print (good_proxy)
#    pp=random.choice(good_proxy)

#    prox = Proxy()
#    prox.proxy_type = ProxyType.MANUAL

    #good
    p="208.127.60.176:8080"
    #good

    #experiment bD
#    p="175.215.8.145:3128"

#    p=pp
#    print ("PROXY: "+p)
    # Proxy IP & Port
    prox.http_proxy = p
    #prox.socks_proxy = p
    prox.ssl_proxy = p
    chrome_options.add_argument('--ignore-certificate-errors')
    # Configure capabilities 
    capabilities = webdriver.DesiredCapabilities.CHROME
#    prox.add_to_capabilities(capabilities)

#proxy here









    _log("--------------DEV no try here--------------")
#
    if (docker==1):
        driver = webdriver.Remote("http://172.17.0.1:4444/wd/hub", options=chrome_options, desired_capabilities=capabilities)
    else:
        driver = webdriver.Chrome(PATH, options=chrome_options, desired_capabilities=capabilities)
#    ptrend_people={}
    _log('do nothing in dev')
#    threaded_proxy()
#    print(ptrend_people)
#    for key in ptrend_people:
#    toptrade_email()
#    jivochat_online("https://everestforex.club/about")
#    ev()
#        _log(key)
#    gravity_reg()
#    ptrend_chat_noreg()
#        _log(ptrend_people[key])
#        ptrend_chat(key,ptrend_people[key])
#    ptrend_chat()
#    cryptogazprom_reg()
#    _24xforex_email()
#    _24xforex_email()
    driver.close()
    driver.quit()

#    driver = webdriver.Chrome(PATH, options=chrome_options, desired_capabilities=capabilities)    
#   driver.get('https://whatismyip.host/')
#    ingo_chat_online()
#    maxi_reg()
#    maxi_chat()
#    time.sleep(1000)


#----------prod
    if (q_toptrade_email>0):
        _log("--------------toptrade email begin------------")
        if (docker==1):
            driver = webdriver.Remote("http://172.17.0.1:4444/wd/hub", options=chrome_options, desired_capabilities=capabilities)
        else:
            driver = webdriver.Chrome(PATH, options=chrome_options, desired_capabilities=capabilities)

        try:
            if True:
                try:
    #                print ("ingo email skip")
                    toptrade_email()
                except:
                    pass
            driver.close()
            driver.quit()
        except:
            _log("toptrade email fail")
            try:
                driver.close()
                driver.quit()
            except:
                pass
            pass
        _log("--------------toptrade email end--------------")







    if (q_everest_chat>0):
        _log("--------------everest chat  begin------------")
#        if (docker==1):
#            driver = webdriver.Remote("http://172.17.0.1:4444/wd/hub", options=chrome_options, desired_capabilities=capabilities)
#        else:
#            driver = webdriver.Chrome(PATH, options=chrome_options, desired_capabilities=capabilities)

#        driver = webdriver.Chrome(PATH, options=chrome_options)
        try:
            for i in range (1,random.randint(15,30)+q_everest_chat):
                try:
    #                print ("ingo email skip")
                    driver = webdriver.Chrome(PATH, options=chrome_options, desired_capabilities=capabilities)
                    jivochat_online("https://everestforex.club/about")
                    driver.close()
                    driver.quit()

                except:
                    _log(" everest chat failed in cycle")
                    driver.close()
                    driver.quit()
                    pass
            driver.close()
            driver.quit()
        except:
            _log("everest chat failed  fail")
            try:
                driver.close()
                driver.quit()
            except:
                pass
            pass
        _log("--------------everest chat  end--------------")









    if (q_gravity_reg>0):
        _log("--------------Gravity reg begin------------")
        if (docker==1):
            driver = webdriver.Remote("http://172.17.0.1:4444/wd/hub", options=chrome_options, desired_capabilities=capabilities)
        else:
            driver = webdriver.Chrome(PATH, options=chrome_options, desired_capabilities=capabilities)

#        driver = webdriver.Chrome(PATH, options=chrome_options)
        try:
            for i in range (1,random.randint(15,30)+q_gravity_reg):
                try:
    #                print ("ingo email skip")
                    gravity_reg()
                except:
                    _log(" Gravity reg failed in cycle")
                    driver.close()
                    driver.quit()
                    pass
            driver.close()
            driver.quit()
        except:
            _log("Gravity reg general fail")
            try:
                driver.close()
                driver.quit()
            except:
                pass
            pass
        _log("--------------Gravity reg end--------------")





    if (q_ptrend_chat_noreg>0):
        _log("--------------Ptrend chat noreg begin------------")
        if (docker==1):
            driver = webdriver.Remote("http://172.17.0.1:4444/wd/hub", options=chrome_options, desired_capabilities=capabilities)
        else:
            driver = webdriver.Chrome(PATH, options=chrome_options, desired_capabilities=capabilities)

#        driver = webdriver.Chrome(PATH, options=chrome_options)
        try:
            for i in range (1,random.randint(5,10)+q_ptrend_chat_noreg):
                try:
    #                print ("ingo email skip")
                    ptrend_chat_noreg()
                except:
                    _log(" ptrend chat noreg failed in cycle")
                    driver.close()
                    driver.quit()
                    pass
            driver.close()
            driver.quit()
        except:
            _log("ptrend chat noreg general fail")
            try:
                driver.close()
                driver.quit()
            except:
                pass
            pass
        _log("--------------ptrend chat noreg end--------------")









    if ((q_threaded_proxy)>0 and (mode =='PROD')):
        if (docker==1):
            driver = webdriver.Remote("http://172.17.0.1:4444/wd/hub", options=chrome_options, desired_capabilities=capabilities)
        else:
            driver = webdriver.Chrome(PATH, options=chrome_options, desired_capabilities=capabilities)

            _log("--------------threaded proxy begin------------")
            try:
                ptrend_people={}
                threaded_proxy()
                print(ptrend_people)
                for key in ptrend_people:
                    _log(key)
                    _log(ptrend_people[key])
                    ptrend_chat(key,ptrend_people[key])

            except:
                pass
            _log("--------------threaded proxy end------------")







    if (q_cryptogazprom_reg>0):
        _log("--------------cryptogazprom_reg begin------------")
        if (docker==1):
            driver = webdriver.Remote("http://172.17.0.1:4444/wd/hub", options=chrome_options, desired_capabilities=capabilities)
        else:
            driver = webdriver.Chrome(PATH, options=chrome_options, desired_capabilities=capabilities)

        try:
            if True:
                try:
    #                print ("ingo email skip")
                    cryptogazprom_reg()
                except:
                    pass
            driver.close()
            driver.quit()
        except:
            _log("cryptogazprom_reg fail")
            try:
                driver.close()
                driver.quit()
            except:
                pass
            pass
        _log("--------------cryptogazprom_reg end--------------")









    if (q_ingo_reg>0):
        for i in range (1, random.randint(1,q_ingo_reg+5)):

            _log("--------------ingo reg begin------------")
            if (docker==1):
                driver = webdriver.Remote("http://172.17.0.1:4444/wd/hub", options=chrome_options, desired_capabilities=capabilities)
            else:
                driver = webdriver.Chrome(PATH, options=chrome_options, desired_capabilities=capabilities)
            try:
                ingo_reg()
                driver.close()
                driver.quit()
            except:
                _log("ingo reg fail")
                try:
                    driver.close()
                    driver.quit()
                except:
                    pass
                pass
            _log("--------------ingo reg end--------------")

    if (q_24xforex_reg>0):
        for i in range (1, random.randint(1,q_24xforex_reg+5)):
            _log("--------------24xforex reg begin------------")
            if (docker==1):
                driver = webdriver.Remote("http://172.17.0.1:4444/wd/hub", options=chrome_options, desired_capabilities=capabilities)
            else:
                driver = webdriver.Chrome(PATH, options=chrome_options, desired_capabilities=capabilities)

            try:
                _24xforex_reg()
                driver.close()
                driver.quit()
            except:
                _log("24xforex reg fail")
                try:
                    driver.close()
                    driver.quit()
                except:
                    pass
                pass
            _log("--------------24xforex reg end--------------")




    if (q_24xforex_email>0):
        _log("--------------24 x forex email begin------------")
        if (docker==1):
            driver = webdriver.Remote("http://172.17.0.1:4444/wd/hub", options=chrome_options, desired_capabilities=capabilities)
        else:
            driver = webdriver.Chrome(PATH, options=chrome_options, desired_capabilities=capabilities)

        try:
            for i in range (1,random.randint(10,20)):
                try:
    #                print ("ingo email skip")
                    _24xforex_email()
                except:
                    pass
            driver.close()
            driver.quit()
        except:
            _log("24x forex email fail")
            try:
                driver.close()
                driver.quit()
            except:
                pass
            pass
        _log("--------------24x forex email end--------------")


    if (q_ingo_email>0):
        _log("--------------Ingo email begin------------")
        if (docker==1):
            driver = webdriver.Remote("http://172.17.0.1:4444/wd/hub", options=chrome_options, desired_capabilities=capabilities)
        else:
            driver = webdriver.Chrome(PATH, options=chrome_options, desired_capabilities=capabilities)

        try:
            for i in range (1,random.randint(10,20)):
                try:
    #                print ("ingo email skip")
                    ingo_email()
                except:
                    pass
            driver.close()
            driver.quit()
        except:
            _log("ingo email fail")
            try:
                driver.close()
                driver.quit()
            except:
                pass
            pass
        _log("--------------Ingo email end--------------")


    if (q_maxi_reg>0):
        _log("--------------maxi reg begin------------")
        if (docker==1):
            driver = webdriver.Remote("http://172.17.0.1:4444/wd/hub", options=chrome_options, desired_capabilities=capabilities)
        else:
            driver = webdriver.Chrome(PATH, options=chrome_options, desired_capabilities=capabilities)

        try:
            for i in range (1,random.randint(5,10)):
                try:
    #                print ("ingo email skip")
                    maxi_reg()
                    
                except:
                    pass
            try:
                maxi_chat()
            except:
                _log("maxi chat failed")
            driver.close()
            driver.quit()
        except:
            _log("maxi reg fail")
            try:
                driver.close()
                driver.quit()
            except:
                pass
            pass
        _log("--------------maxi reg end--------------")



    #off, not working now
    if (q_umarkets_reg>0):
        _log("--------------umarkets reg begin------------")
        if (docker==1):
            driver = webdriver.Remote("http://172.17.0.1:4444/wd/hub", options=chrome_options, desired_capabilities=capabilities)
        else:
            driver = webdriver.Chrome(PATH, options=chrome_options, desired_capabilities=capabilities)

#        driver = webdriver.Chrome(PATH, options=chrome_options)
        try:
            for i in range (1,random.randint(5,10)):
                try:
    #                print ("ingo email skip")
                    umarkets_reg()
                except:
                    pass
            try:
                maxi_chat()
            except:
                _log(" chat failed")
            driver.close()
            driver.quit()
        except:
            _log("umarketsreg fail")
            try:
                driver.close()
                driver.quit()
            except:
                pass
            pass
        _log("--------------umarkets reg end--------------")




    if (q_st24online_reg>0):
        _log("--------------st24online_reg begin------------")
        if (docker==1):
            driver = webdriver.Remote("http://172.17.0.1:4444/wd/hub", options=chrome_options, desired_capabilities=capabilities)
        else:
            driver = webdriver.Chrome(PATH, options=chrome_options, desired_capabilities=capabilities)

#        driver = webdriver.Chrome(PATH, options=chrome_options)
        try:
            for i in range (1,random.randint(5,10)+q_st24online_reg):
                try:
    #                print ("ingo email skip")
                    st24online_reg()
                except:
                    _log(" st24online_reg failed in cycle")
                    driver.close()
                    driver.quit()
                    pass
            driver.close()
            driver.quit()
        except:
            _log("st24online_reg general fail")
            try:
                driver.close()
                driver.quit()
            except:
                pass
            pass
        _log("--------------st24online_reg end--------------")


    if (q_st24online_phone>0):
        _log("--------------st24 phone begin------------")
        if (docker==1):
            driver = webdriver.Remote("http://172.17.0.1:4444/wd/hub", options=chrome_options, desired_capabilities=capabilities)
        else:
            driver = webdriver.Chrome(PATH, options=chrome_options, desired_capabilities=capabilities)

        try:
            if True:
                try:
    #                print ("ingo email skip")
                    st24online_phone()
                except:
                    pass
            driver.close()
            driver.quit()
        except:
            _log("st24 phone fail")
            try:
                driver.close()
                driver.quit()
            except:
                pass
            pass
        _log("--------------st24 phone end--------------")


    if (q_st24online_email>0):
        _log("--------------st24 email begin------------")
        if (docker==1):
            driver = webdriver.Remote("http://172.17.0.1:4444/wd/hub", options=chrome_options, desired_capabilities=capabilities)
        else:
            driver = webdriver.Chrome(PATH, options=chrome_options, desired_capabilities=capabilities)

        try:
            if True:
                try:
    #                print ("ingo email skip")
                    st24online_email()
                except:
                    pass
            driver.close()
            driver.quit()
        except:
            _log("st24 email fail")
            try:
                driver.close()
                driver.quit()
            except:
                pass
            pass
        _log("--------------st24 email end--------------")



 
