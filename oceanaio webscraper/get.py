from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import os.path
from webdriver_manager.firefox import GeckoDriverManager
import time

url = r"https://ocean-aio-private.hyper.co/login?redirect=%2Fguides%2Fnmr-methods-0yAp"

options = Options()
# options.headless = True
driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=options)
driver.get(url)
#find email button
email_xpath = '//*[@id="__next"]/div/main/div/div/div[5]/button'


# click email button
email_button = driver.find_element_by_xpath(email_xpath)
email_button.click()

#fill email box
disc_box = driver.find_element_by_xpath('//*[@id="__next"]/div/main/div/div/div[5]/a')
disc_box.click()

disc_email = driver.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div/div/div/form/div/div/div[1]/div[2]/div[1]/div/div[2]/input')
disc_pass = driver.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div/div/div/form/div/div/div[1]/div[2]/div[2]/div/input')

email = "bc2tothe11@gmail.com"
password_ds = "#24k)YMkf*iYmYs"

disc_email.send_keys(email)
disc_pass.send_keys(password_ds)



# continue button
cont_box = driver.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div/div/div/form/div/div/div[1]/div[2]/button[2]')
cont_box.click()






