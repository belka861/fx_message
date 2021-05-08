from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.common.keys import Keys
import sys, random

# Import pandas
import pandas as pd
import time
import requests

from random_username.generate import generate_username

def _click(xpath):
	r=driver.find_element_by_xpath(xpath)
	r.click()
	return True


def _do_email():
	driver.get('https://24xforex.com/ru#contact')
	time.sleep(2)

	e=driver.find_element_by_xpath('//*[@id="contact_email"]')
	e.send_keys(email)
	time.sleep(1)
	name1=driver.find_element_by_xpath('//*[@id="contact_name"]')
	name1.send_keys(name)
	_click('//*[@id="contact_message"]')
	text1=driver.find_element_by_xpath('//*[@id="contact_message"]')
	text1.send_keys(t)
	_click('//*[@id="contact"]/div[2]/div[2]/form/button')
	time.sleep(7)



#with open('z.txt', 'r', encoding='utf-8', errors='ignore') as file:
#	data = file.read().replace('\n', '')


url = 'https://raw.githubusercontent.com/belka861/fx_message/main/phrases.txt'
r = requests.get(url, allow_redirects=True)
open('phrases.txt', 'wb').write(r.content)
with open ("phrases.txt", "r", encoding='utf-8', errors='ignore') as myfile:
	data=myfile.readlines()
s=data

#s=data.split()                   
print (len(s))
print (s[100])
#sys.exit()

#from tempMail2 import TempMail

#import requests

#url = "https://privatix-temp-mail-v1.p.rapidapi.com/request/mail/id/null/"

#headers = {
#    'x-rapidapi-key': "d0d95f3400msh04a0668232e66f2p175704jsn53624ac18a6c",
#    'x-rapidapi-host': "privatix-temp-mail-v1.p.rapidapi.com"
#    }

#response = requests.request("GET", url, headers=headers)

#print(response.text)
#tm = TempMail()
#tm.api_key="d0d95f3400msh04a0668232e66f2p175704jsn53624ac18a6c"
#email = tm.get_email_address("d0d95f3400msh04a0668232e66f2p175704jsn53624ac18a6c")  # v5gwnrnk7f@gnail.pw
#print (tm.get_mailbox(email))  # list of emails
#sys.exit()  


#while True:
#	r=random.randint(100, len(s)-20)
#	t=""
#	for i in range (0,10):
#		t=t+s[r+i]+" "
#	print (t)


while True:
	r=random.randint(1, len(s)-2)
#	t=""
#	for i in range (0,10):
#		t=t+s[r+i]+" "
	t=s[r]
	print (t)




# reading csv file 
	df=pd.read_csv("russian_surnames.csv", header=0, sep=';')
	max_sur=round(df.size/6-1)
	random_sur_id=random.randint(1, max_sur)

	surname=df['Surname'][random_sur_id]


	df=pd.read_csv("russian_names.csv", header=0, sep=';')
	max_sur=round(df.size/6-1)
	random_sur_id=random.randint(1, max_sur)
	name=df['Name'][random_sur_id]

	print (name, surname)

	domains=['mail.ru','yandex.ru', 'rambler.ru', 'outlook.com', 'gmail.com', 'hotmail.com', 'list.ru', 'bk.ru', 'inbox.ru', 'internet.ru',  'yahoo.com', 'aol.com', 'e1.ru','inbox.lv', 'dino.lv','human.lv', 'fit.lv','sok.lv', 'eclub.lv']
	password=""
	for i in range (1,5):
		password=password+random.choice('01234567890')

	username=generate_username(1)[0]+password
	domain=random.choice(domains)
	email=username+"@"+domain



#sex=df['Sex'][random_sur_id]
#print(surname, sex)
#sys.exit()

	PATH = 'C:\Program Files (x86)\chromedriver.exe'
	driver = webdriver.Chrome(PATH)
	driver.maximize_window()
	driver.delete_all_cookies()

	_do_email()
	driver.delete_all_cookies()
	driver.close()
	driver.quit()

def _do_chat():

	driver.get("https://24xforex.com/ru")
	time.sleep(10)
	_click('//*[@id="jvlabelWrap"]/jdiv[2]')
#//*[@id="jvlabelWrap"]/jdiv[1]
	time.sleep(5)
	r=driver.find_element_by_xpath('//*[@id="jcont"]/jdiv[3]/jdiv/jdiv[3]/jdiv[1]/jdiv[1]/textarea')
	
	r.send_keys(t)
	from selenium.webdriver.common.keys import Keys
	
	webdriver.ActionChains(driver).send_keys(Keys.ENTER).perform()
	time.sleep(5)
#	sys.exit()
#r=driver.find_element_by_xpath('//*[@id="primary-menu"]/li[9]/div/a[2]')
#r.click()

#driver.get("https://trade.globalallianceltd.com/registration-ru")


#driver.implicitly_wait(10)
#time.sleep(2)

#r=driver.find_element_by_xpath('//*[@id="app"]/div[5]/div/section/div[1]/div/div[1]/div[1]')
#r.click()

#driver.implicitly_wait(3)

#r=driver.find_element_by_xpath('//*[@id="app"]/div[5]/div/section/div[1]/div/div[1]/div[2]')
#r.click()

#from selenium.webdriver.common.keys import Keys

#webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
#sys.exit()
#driver.implicitly_wait(100)
#webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
#time.sleep(2)

#r=driver.find_element_by_xpath('//*[@id="top-nav"]/div[2]/div[4]/button')
#r.click()
#time.sleep(2)
#r=driver.find_element_by_xpath('//*[@id="app"]/div[5]/div/section/div[1]/div/div[1]/div[2]')
#r.click()
#time.sleep(2)

# create action chain object
#action = ActionChains(driver)
  
# context click the item
#action.context_click(on_element = element)
#driver.implicitly_wait(100)
#print ("right sidebar")
#sys.exit()
#print(driver.page_source)

	name1=driver.find_element_by_xpath('//*[@id="scrollbar-container"]/jdiv[1]/jdiv/jdiv[4]/jdiv/jdiv/jdiv/jdiv/jdiv[1]/input')
	name1.send_keys(name)
#sys.exit()
#time.sleep(2)

#	last_name=driver.find_element_by_xpath('//*[@id="live_last_name"]')
#	last_name.send_keys(surname)
	
#	select=driver.find_element_by_xpath('/html/body/div[1]/section[1]/div/div/form/div[2]/div/div[1]')
#	select.click()

#lang
#	select=driver.find_element_by_xpath('/html/body/div[1]/section[1]/div/div/form/div[2]/div/div[2]/ul/li[3]')
#	select.click()



#	select=driver.find_element_by_xpath('/html/body/div[1]/section[1]/div/div/form/div[1]/div[1]')
#	select.click()
#sys.exit()
#	co=driver.find_element_by_xpath('/html/body/div[1]/section[1]/div/div/form/div[1]/div[2]/ul/li[110]')
#	co.click()

#	time.sleep(1)
#time.sleep(2)
	tn=random.randint(1000000, 9999999)
#tns="+371"+str(tn)
#tns="+7925"+str(tn)
	tns="+3712"+str(tn)
	phone=driver.find_element_by_xpath('//*[@id="scrollbar-container"]/jdiv[1]/jdiv/jdiv[4]/jdiv/jdiv/jdiv/jdiv/jdiv[2]/input')
#phone.clear()
	phone.send_keys(tns)


#	select=driver.find_element_by_xpath('/html/body/div[1]/section[1]/div/div/form/div[3]/label')
#	select.click()
	
#	select=driver.find_element_by_xpath('/html/body/div[1]/section[1]/div/div/form/div[4]/label')
#	select.click()

#	driver.execute_script('document.getElementById("live_check").checked=true;')
#sys.exit()
#select=driver.find_element_by_css_selector('#live_check')
#select.click()
#WebElement we = driver.findElement(By.xpath("//span[contains(string(),'Remote PC')]"));
#Actions clickTriangle= new Actions(driver);
#clickTriangle.moveToElement(we).moveByOffset(-10, -5).click().perform();              



#time.sleep(2)
#birth=driver.find_element_by_id('user-birthday-reg')
#birth.click()
#time.sleep(2)
#day=driver.find_element_by_xpath('//*[@id="app"]/div[5]/div/section/div[1]/div[2]/div/div[2]/div[1]/div[1]/input')

#d=random.randint(1, 28)
#ds=str(d)
#if (d<10):
#	ds="0"+ds
#day.send_keys(ds)

#time.sleep(2)#

#month=driver.find_element_by_xpath('//*[@id="app"]/div[5]/div/section/div[1]/div[2]/div/div[2]/div[1]/div[2]/input')

#d=random.randint(1, 12)
#ds=str(d)
#if (d<10):
#	ds="0"+ds
#month.send_keys(ds)
#time.sleep(2)

#year=driver.find_element_by_xpath('//*[@id="app"]/div[5]/div/section/div[1]/div[2]/div/div[2]/div[1]/div[3]/input')
#d=random.randint(1960, 2000)
#year.send_keys(str(d))
#time.sleep(2)
#driver.implicitly_wait(5)
#butrt
#b=driver.find_element_by_xpath('//*[@id="app"]/div[5]/div/section/div[1]/div[2]/div/div[2]/div[2]/button[1]')
#b.click()
#time.sleep(2)
#driver.close()
#driver.quit()

#print(email)
	e=driver.find_element_by_xpath('//*[@id="scrollbar-container"]/jdiv[1]/jdiv/jdiv[4]/jdiv/jdiv/jdiv/jdiv/jdiv[3]/input')
	e.send_keys(email)
	time.sleep(1)
	_click('//*[@id="scrollbar-container"]/jdiv[1]/jdiv/jdiv[4]/jdiv/jdiv/jdiv/jdiv/jdiv[4]')
	time.sleep(3)
	return True




#time.sleep(2)
#password=""
#f#or i in range (1,8):
#	password=password+random.choice('abcdefghijklmnopqrstuvwxyz')
#for i in range (1,4):
#	password=password+random.choice('01234567890')
#print (password)

#password="global123"
#e=driver.find_element_by_xpath('//*[@id="user-password-reg"]')
#e.send_keys(password)
#time.sleep(2)
#b=driver.find_element_by_xpath('//*[@id="app"]/div[5]/div/section/div[1]/div/div[2]/div/form/div[8]/button')
#b.click()

#	b=driver.find_element_by_xpath('/html/body/div[1]/section[1]/div/div/form/button')
#	b.click()

#	time.sleep(20)
#print (email)
#print (password)

#	b=driver.find_element_by_xpath('//*[@id="Logout-button"]')
#	b.click()
#	sys.exit()
#import time
#time.sleep(10)


                                                                       

#try 2
#webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
#sys.exit()
#driver.implicitly_wait(100)
#webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()

 
