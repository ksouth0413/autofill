from time import sleep
from selenium import webdriver

driver = webdriver.Chrome('/Applications/chromedriver')
url = 'https://docs.google.com/forms/d/e/1FAIpQLScPXUcpuiFE00JLPYsABzE9tN005FSQAdQJ8A0af_POVZbi1w/viewform'
driver.get(url)

sleep(2)
class_name1 = '.quantumWizTextinputPaperinputInput.exportInput'
driver.find_elements_by_css_selector(class_name1)[0].send_keys('308')
sleep(2)
driver.find_elements_by_css_selector(class_name1)[1].send_keys('김남훈')

sleep(2)
class_name2 = '#i13'
driver.find_element_by_css_selector(class_name2).click()

sleep(2)
class_name3 = '#i23'
driver.find_element_by_css_selector(class_name3).click()

sleep(2)
class_name4 = '#i34'
driver.find_element_by_css_selector(class_name4).click()

sleep(2)
class_name5 = '.appsMaterialWizButtonPaperbuttonLabel.quantumWizButtonPaperbuttonLabel.exportLabel'
driver.find_element_by_css_selector(class_name5).click()

