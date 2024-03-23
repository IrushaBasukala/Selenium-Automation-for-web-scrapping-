import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait,Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException,NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome()
# driver.get('https://techwithtim.net')
driver.get('https://finance.yahoo.com/')
print(driver.title)
dir(driver)

# search = driver.find_element_by_name('s')
# searchId="yfin-usr-qry"
search = driver.find_element(By.ID,'yfin-usr-qry');
search.clear();
search.send_keys('TSLA')
search.send_keys(Keys.ENTER)




# search.send_keys("tech with tim" + Keys.ENTER)
# link = driver.find_element(By.PARTIAL_LINK_TEXT,"Tech With Tim")
# link.click()

driver.quit()

