from time import sleep
from selenium import webdriver

driver = webdriver.Chrome('/Applications/chromedriver')
url = 'https://docs.google.com/forms/d/e/1FAIpQLSeEtkMWe9eKQb6tMSYlLpE1YefDm4fDptLdwvk6Pqifr9ESPw/viewform'
driver.get(url)

sleep(2)
class_name = '#i5'
driver.find_element_by_css_selector(class_name).click()

sleep(2)
class_name1 = '.appsMaterialWizButtonPaperbuttonLabel.quantumWizButtonPaperbuttonLabel.exportLabel'
driver.find_element_by_css_selector(class_name1).click()
