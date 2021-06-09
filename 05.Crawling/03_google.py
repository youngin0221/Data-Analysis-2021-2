import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('./chromedriver')
driver.get('http://www.google.com')
time.sleep(0.5)

search_box = driver.find_element_by_css_selector('.gLFyf.gsfi')
search_box.send_keys('ChromeDriver')
search_box.send_keys(Keys.ENTER)
time.sleep(1)

x = driver.find_element_by_css_selector('div#rso>giv.g')
for div in divs:
    try:
        title = div.find_element_by_css_selector('.LC20lb.DKV0Md').text
        content = div.find_element_by_css_selector('.aCOpRe').text
        print(title)
        print(content)
        print('=============================')
    except:
        pass

driver.close() 