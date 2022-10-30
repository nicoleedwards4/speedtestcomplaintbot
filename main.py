from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PROMISED_DOWN = 150
PROMISED_UP = 10

chrome_driver_path = "C:\Development\chromedriver.exe"
# driver = webdriver.Chrome(executable_path=chrome_driver_path)


class InternetSpeedTwitterBot:

    def __int__(self, driver_path):
        self.driver = webdriver.Chrome(executable_path=chrome_driver_path)
        self.up = None
        self.down = None

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        go_button = self.driver.find_element("css selector", "js-start-test test-mode-multi" )
        go_button.click()
        time.sleep(120)

        back_to_results_button = self.driver.find_element("xpath", '//*[@id="container"]/div/div[3]/div/div/div/div['
                                                                   '2]/div[3]/div[3]/div/div[8]/div/div/div[2]/a')
        back_to_results_button.click()

        self.down = self.driver.find_element("css selector", "result-data-large number result-data-value download-speed").text

        self.up = self.driver.find_element("css selector", "result-data-large number result-data-value upload-speed").text

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/home?lang=en")
        new_tweet_button = self.driver.find_element("xpath", '//*[@id="react-root"]/div/div/div['
                                                             '2]/header/div/div/div/div[1]/div[3]/a')
        new_tweet_button.click()

        message_input = self.driver.find_element("css selector", "public-DraftStyleDefault-block "
                                                                 "public-DraftStyleDefault-ltr")
        message_input.send_keys(f"@comcast why is my internet speed {self.up} up and {self.down} down when it's "
                                f"supposed to be {PROMISED_UP} up and {PROMISED_DOWN} down?")

        tweet_button = self.driver.find_element("css selector", "css-18t94o4 css-1dbjc4n r-l5o3uw r-42olwf r-sdzlij "
                                                                "r-1phboty r-rs99b7 r-19u6a5r r-2yi16 r-1qi8awa "
                                                                "r-1ny4l3l r-ymttw5 r-o7ynqc r-6416eg r-lrvibr")
        tweet_button.click()


bot = InternetSpeedTwitterBot()

bot.get_internet_speed()

if bot.up < PROMISED_UP or bot.down < PROMISED_DOWN:
    bot.tweet_at_provider()




