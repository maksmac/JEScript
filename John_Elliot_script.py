from selenium import webdriver
import time
import re
import random

def random_email_gen(email):
	user = re.sub('\@(.*)',"",email)
	provider = re.sub('(.*)\@',"",email)
	e_num = random.randint(1000,9999)
	l = list(user)
	period_ammount = random.randint(1,len(l)-1)
	for x in range(period_ammount):
		period_place = random.randint(1,len(l)-1)
		if((l[period_place-1] != ".")):
			l.insert(period_place, ".")

	final = ''.join(l)
	final = final + "+" + str(e_num) + "@" + provider
	return final





count = 0
runs = input("How many entries? ")
final_email = input("email: ")

while (count < int(runs)):
	options = webdriver.ChromeOptions()  # Optional argument, if not specified will search path.
	#options.add_argument('headless')
	options.add_argument('window-size=1900x900')
	driver = webdriver.Chrome('put path here')
	driver.get('https://www.johnelliott.co/pages/lebron-james-x-john-elliott-nikelab-icon-friends-family-giveaway')

	user_email = random_email_gen(final_email);
	print("entering: " + user_email)
	email_select =driver.find_element_by_css_selector('input[type=email]')
	email_select.send_keys(user_email)
	size_selector = driver.find_element_by_xpath('//*[@id="mce-SHOESIZE_msdd"]')
	size_selector.click()
	time.sleep(1)
	size_selector.find_element_by_xpath('//*[@id="mce-SHOESIZE_child"]/ul/li[10]/span').click()
	submit = driver.find_element_by_xpath('//*[@id="mc-embedded-subscribe-lebron-giveaway"]')
	submit.click()
	capatcha = driver.find_element_by_xpath('//*[@id="mc_embed_signup_scroll"]/div[4]/div[1]/div/div/iframe').click()
	time.sleep(15)
	driver.close()
	print("done")
	count+=1

