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

