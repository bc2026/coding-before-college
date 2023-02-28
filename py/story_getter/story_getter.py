from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import os.path

options = Options()
options.headless = True

url = r"http://www.textfiles.com/etext/FICTION/"
driver = webdriver.Firefox(options=options)
driver.get(url)

savePath = r'/home/bc/Desktop/dev/py/story_getter/stories'

start = 0

stories = []
principal_names = []
colCount = len(driver.find_elements_by_xpath('//tr[@valign="TOP"]'))

while(start < colCount):
    start_string = str(start + 2)
    storyName = driver.find_element_by_xpath("/html/body/p[2]/table/tbody/tr["+start_string+"]/td[1]/a")
    storyName = storyName.text
    stories.append(storyName)
    
    principal_names.append(storyName[:storyName.find(".txt")])
    
    linkText = driver.find_element_by_link_text(storyName)
    linkText.click()

    path = savePath + "/" + storyName + ".txt"

    storyText = driver.find_element_by_xpath('/html/body').text
    h = open(path, "w")
    h.write(storyText)
    print("Wrote story: {}".format(path))
    driver.get("http://www.textfiles.com/etext/FICTION/")

    start += 1
    