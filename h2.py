from selenium import webdriver
# Option 1 - with ChromeOptions
chrome_options = webdriver.ChromeOptions()
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from phone_gen import PhoneNumber
#
#chrome_options.add_argument('--headless')
#chrome_options.add_argument('--no-sandbox') # required when running as root user. otherwise you would get no sandbox errors. 
import time,os,random,datetime,sys
chrome_options.add_argument('--disable-blink-features=AutomationControlled')

# Option 2 - with pyvirtualdisplay
from pyvirtualdisplay import Display 
display = Display(visible=0, size=(1024, 768)) 
display.start() 
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


def ingo_email():
    driver.get('https://ingoinvest.com/ru')
    time.sleep(7)

    e=driver.find_element_by_xpath('//*[@id="contact_email"]')
    e.send_keys(email)
#    time.sleep(1)
    name1=driver.find_element_by_xpath('//*[@id="contact_name"]')
    name1.send_keys(final_name)
    _click('//*[@id="contact_message"]')
    text1=driver.find_element_by_xpath('//*[@id="contact_message"]')
    text1.send_keys(question)
    time.sleep (1)
    _click('//*[@id="contact"]/div/div[2]/div[1]/form/button')
#    _wait_element
#    r=driver.find_element_by_css_selector('#contact > div.contact-block > div.form-block > form > button')
#    r.click()
#    _wait_element('//*[@id="contact"]/div/div[2]/div[1]/form/button')
#    driver.execute_script('document.evaluate(\'//*[@id="contact"]/div/div[2]/div[1]/form/button\', document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue.click();')
#    time.sleep(4)
#    _wait_element('//*[@id="contact"]/div[2]/div[1]')
    _wait_element('//*[@id="wrapper"]/main/div[2]/article/h1')
    r=driver.find_element_by_xpath('//*[@id="wrapper"]/main/div[2]/article/h1').text
    _log(r)
#    time.sleep(5)
#    _log(driver.page_source)




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


def _do_reg():
    driver.maximize_window()
    driver.delete_all_cookies()
    driver.get("https://24xforex.com/ru/register")

#    time.sleep(10)
    _log(driver.page_source)

    driver.execute_script("window.open('about:blank', 'tab2');")
    driver.switch_to.window("tab2")
    driver.get('https://temp-mail.io/en')
    time.sleep(3)
#    _log(driver.page_source)
    email=driver.find_element_by_id('email').get_attribute('value')
    _log(email)
    driver.switch_to.window(driver.window_handles[0])
    _wait_element('//*[@id="live_name"]')
    e=driver.find_element_by_id('live_email')
    e.send_keys(email)

    name1=driver.find_element_by_xpath('//*[@id="live_name"]')
    name1.send_keys(name)

    last_name=driver.find_element_by_xpath('//*[@id="live_last_name"]')
    last_name.send_keys(surname)
    
    select=driver.find_element_by_xpath('/html/body/div[1]/section[1]/div/div/form/div[2]/div/div[1]')
    select.click()

    select=driver.find_element_by_xpath('/html/body/div[1]/section[1]/div/div/form/div[2]/div/div[2]/ul/li[3]')
    select.click()

    select=driver.find_element_by_xpath('/html/body/div[1]/section[1]/div/div/form/div[1]/div[1]')
    select.click()

    countries=[11,15,20,27,52,53,55,61,65,70,74,78,90,98,103,108,110,116,117,119,132,143,146,153,163,169,170,188,189,201,202,205,213,218,219,221,75]
    crandom=random.choice(countries)
    print (crandom)
    co=driver.find_element_by_xpath('/html/body/div[1]/section[1]/div/div/form/div[1]/div[2]/ul/li['+str(crandom)+']')
    print (co.text)
    ph=PhoneNumber(co.text)
    tn=ph.get_number(full=False)
    _log (tn)
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
        r = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="__layout"]/div/aside/div[1]/div[2]/div/div/ul/li/div[1]')))
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

    countries=[11,15,20,27,52,53,55,61,65,70,74,78,90,98,103,108,110,116,117,119,132,143,146,153,163,169,170,188,189,201,202,205,213,218,219,221,75]
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

    dice=random.choice([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,21,22,23,20])
    if (dice==5):
        tick=nyse[random.randint(1,len(nyse)-1)].replace('\n', '')
        question="Мне аналитик посоветовал купить акции "+tick+" А ОНИ СЕГОДНЯ ОБВАЛИЛИСЬ! ВЕРНИТЕ МНЕ МОИ ДЕНЬГИ!!!"

    if (dice==6):
        card=str(random.randint(1000,9999))
        question="По поводу пополнения торгвого счета карточкой Visa "+card





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
#    ingo_reg()
#_do_email()
    try:
        ingo_reg()
    except:
        print("ingo reg failed")
        pass

    try:
        ingo_email()
    except:
        print ("ingo email fail")
        pass

#    try:
#        _do_chat()
#    except:
#        print ('chat failed')
#        pass

    try:
        _do_email()
    except:
        print ('email failed')
        pass

#    try:
#    _do_reg()
#    except:
#        print ('reg failed')
#        pass


    try:
        driver.delete_all_cookies()
    except:
        pass
    driver.close()
    driver.quit()
    os.system('pkill chrome')
