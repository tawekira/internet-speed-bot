import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

PROMISED_DOWN = 150
PROMISED_UP = 10
TWITTER_EMAIL = os.environ["TWITTER_EMAIL"]
TWITTER_PASSWORD = os.environ["TWITTER_PASSWORD"]
PHONE_NUMBER = os.environ["PHONE_NUMBER"]
INTERNET_PROVIDER_HANDLE = "RainTawekira"
class InternetSpeedTwitterBot:
    def __init__(self):
        self.down = 0
        self.up = 0
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options= chrome_options)
    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        start = self.driver.find_element(By.CSS_SELECTOR, value= ".start-text")
        start.click()
        time.sleep(15)
        def extract():
            download = self.driver.find_element(By.CSS_SELECTOR, value= ".download-speed").text
            upload = self.driver.find_element(By.CSS_SELECTOR, value= ".upload-speed").text
            try:
                self.down = float(download)
                self.up = float(upload)
                print(f"down: {self.down}")
                print(f"up: {self.up}")
            except:
                time.sleep(15)
                extract()

        extract()
    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/")
        time.sleep(1)
        sign_in = self.driver.find_element(By.XPATH, value= '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div/div/div[3]/div[5]/a/div/span/span')
        sign_in.click()
        time.sleep(5)
        enter = self.driver.find_element(By.CSS_SELECTOR, value= "input")
        enter.click()
        enter.send_keys(TWITTER_EMAIL)
        enter.send_keys(Keys.ENTER)
        time.sleep(2)
        try:

            security = self.driver.find_element(By.CSS_SELECTOR, value= "span span").text
            print(security)
            number = self.driver.find_element(By.CSS_SELECTOR, value="input")
            number.send_keys(PHONE_NUMBER)
            number.send_keys(Keys.ENTER)
            time.sleep(2)
        finally:

            password = self.driver.find_element(By.NAME, value= "password")
            password.send_keys(TWITTER_PASSWORD)
            password.send_keys(Keys.ENTER)
            time.sleep(5)
            tweet = self.driver.find_element(By.XPATH, value= '//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a/div')
            tweet.click()
            time.sleep(2)
            enter = self.driver.find_element(By.CSS_SELECTOR, value= ".DraftEditor-editorContainer div div div div")
            enter.send_keys(f"Hey @{INTERNET_PROVIDER_HANDLE}, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?")
            webdriver.ActionChains(self.driver).key_down(Keys.CONTROL).send_keys(Keys.ENTER).perform()
            print("Tweet sent")




internet_speed_twitter_bot = InternetSpeedTwitterBot()
internet_speed_twitter_bot.get_internet_speed()
if PROMISED_DOWN>internet_speed_twitter_bot.down or PROMISED_UP>internet_speed_twitter_bot.up:
    internet_speed_twitter_bot.tweet_at_provider()