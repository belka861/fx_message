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

from random_username.generate import generate_username

def _click(xpath):
	r=driver.find_element_by_xpath(xpath)
	r.click()
	return True


with open('z.txt', 'r') as file:
	data = file.read().replace('\n', '')
s=data.split()                   
print (len(s))
print (s[100])


while True:
	r=random.randint(100, len(s)-20)
	t=""
	for i in range (0,10):
		t=t+s[r+i]+" "
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


	PATH = 'C:\Program Files (x86)\chromedriver.exe'
	driver = webdriver.Chrome(PATH)
	driver.maximize_window()
	driver.delete_all_cookies()
	driver.get("https://24xforex.com/ru")
	time.sleep(5)
	_click('//*[@id="jvlabelWrap"]/jdiv[2]')
	time.sleep(5)
	r=driver.find_element_by_xpath('//*[@id="jcont"]/jdiv[3]/jdiv/jdiv[3]/jdiv[1]/jdiv[1]/textarea')
	
	r.send_keys(t)
	from selenium.webdriver.common.keys import Keys
	
	webdriver.ActionChains(driver).send_keys(Keys.ENTER).perform()
	time.sleep(5)

	name1=driver.find_element_by_xpath('//*[@id="scrollbar-container"]/jdiv[1]/jdiv/jdiv[4]/jdiv/jdiv/jdiv/jdiv/jdiv[1]/input')
	name1.send_keys(name)
	tn=random.randint(1000000, 9999999)
#tns="+371"+str(tn)
#tns="+7925"+str(tn)
	tns="+3712"+str(tn)
	phone=driver.find_element_by_xpath('//*[@id="scrollbar-container"]/jdiv[1]/jdiv/jdiv[4]/jdiv/jdiv/jdiv/jdiv/jdiv[2]/input')
#phone.clear()
	phone.send_keys(tns)


	domains=['mail.ru','yandex.ru', 'rambler.ru', 'outlook.com', 'gmail.com', 'hotmail.com', 'list.ru', 'bk.ru', 'inbox.ru', 'internet.ru',  'yahoo.com', 'aol.com', 'e1.ru','inbox.lv', 'dino.lv','human.lv', 'fit.lv','sok.lv', 'eclub.lv']
	password=""
	for i in range (1,5):
		password=password+random.choice('01234567890')

	username=generate_username(1)[0]+password
	domain=random.choice(domains)
	email=username+"@"+domain
#print(email)
	e=driver.find_element_by_xpath('//*[@id="scrollbar-container"]/jdiv[1]/jdiv/jdiv[4]/jdiv/jdiv/jdiv/jdiv/jdiv[3]/input')
	e.send_keys(email)
	time.sleep(1)
	_click('//*[@id="scrollbar-container"]/jdiv[1]/jdiv/jdiv[4]/jdiv/jdiv/jdiv/jdiv/jdiv[4]')
	time.sleep(10)

#	b=driver.find_element_by_xpath('//*[@id="Logout-button"]')
#	b.click()
	driver.delete_all_cookies()
	driver.close()
	driver.quit()
#	sys.exit()
#import time
#time.sleep(10)




