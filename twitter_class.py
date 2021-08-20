from selenium import webdriver
import time

#___FIRST DOWNLOAD SELENIUM CHROMEDRIVER AND USE SPECIFIC PATH
#___https://chromedriver.chromium.org/downloads
webdriver_chrome_path = r"C:\Users\przem\Documents\Python Scripts\chromedriver.exe"

#___SPECIFY YOUR LOGIN DETAILS
TWITTER_MAIL = "YOUR_USERNAME OR EMAIL"
TWITTER_PASS = "YOUR PASSWORD"

class InternetSpeedTwitterBot:

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=webdriver_chrome_path)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        speed_website = "https://www.speedtest.net/"
        self.driver.get(speed_website)
        cookies_consent = self.driver.find_element_by_id("_evidon-banner-acceptbutton")
        cookies_consent.click()
        go_button = self.driver.find_element_by_class_name("start-text")
        go_button.click()
        time.sleep(40)
        down_speed = self.driver.find_element_by_class_name("download-speed").text
        up_speed = self.driver.find_element_by_class_name("upload-speed").text
        return down_speed, up_speed

    def tweet_at_provider(self, message):
        twitter_login = "https://twitter.com/login?lang=pl"
        self.driver.get(twitter_login)
        time.sleep(1)
        login = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input')
        # login.click()
        login.send_keys(TWITTER_MAIL)
        password = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input')
        # password.click()
        password.send_keys(TWITTER_PASS)
        login = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div/div')
        login.click()
        time.sleep(3)
        tweet_text = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div')
        tweet_text.send_keys(message)
        send_tweet = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]')
        send_tweet.click()

