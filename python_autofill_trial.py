from time import sleep
from selenium import webdriver

#instead of this >> driver = webdriver.Chrome('/Applications/chromedriver')
options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_argument("lang=ko_KR")
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")
options.add_argument("--no-sandbox")

driver = webdriver.Chrome('chromedriver', chrome_options=options)
driver.implicitly_wait(3)

url = 'https://docs.google.com/forms/d/e/1FAIpQLSeEtkMWe9eKQb6tMSYlLpE1YefDm4fDptLdwvk6Pqifr9ESPw/viewform'
driver.get(url)

sleep(2)
class_name = '#i5'
driver.find_element_by_css_selector(class_name).click()

sleep(2)
class_name1 = '.appsMaterialWizButtonPaperbuttonLabel.quantumWizButtonPaperbuttonLabel.exportLabel'
driver.find_element_by_css_selector(class_name1).click()
