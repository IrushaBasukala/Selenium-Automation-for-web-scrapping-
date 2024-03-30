import time
from selenium import webdriver;
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



driver = webdriver.Chrome()
driver.get('https://twitter.com')
print(driver.title)

# time.sleep(5) 
# inslead of using sleep , we can use WebDriverWait, lets see how we can use it,
login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//a[@data-testid="loginButton"]')))

# login_button = driver.find_element(By.XPATH,'//a[@data-testid="loginButton"]') 
# because we have used WebDriverWait on login button, we are not gonna to use find_element because , it will get it done by EC and WebDriverWait
login_button.send_keys(Keys.RETURN);
time.sleep(10)
user_name = driver.find_element(By.XPATH,"//input[@type='text' and @name='text']")
user_name.send_keys('abc');
user_name.send_keys(Keys.RETURN)
time.sleep(5)
password = driver.find_element(By.XPATH,"//input[@type='password' and @name='password']")
password.send_keys("abc")
password.send_keys(Keys.RETURN)
time.sleep(10)

target = 'RONBupdates'
profile_url = f'https://twitter.com/{target}'
driver.get(profile_url)
time.sleep(5)

for _ in range(5):
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
    time.sleep(2)

tweets = driver.find_elements(By.XPATH, "//div[@data-testid='tweetText']")
print(f'Found {len(tweets)} tweets')

for tweet in tweets:
    tweet_text = tweet.text
    print(tweet_text);
    driver.execute_script("arguments[0].click();", tweet);
    time.sleep(5)
    comments = driver.find_elements(By.XPATH,"//div[@data-testid='tweetText']")
    print(f'Found {len(comments)} comments on the tweet')

    for comment in comments:
        comment_text = comment.text
        print(comment_text)


driver.quit()





