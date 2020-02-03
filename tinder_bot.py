from selenium import webdriver
from time import sleep

from secrets import username, passwords

class TinderBot():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get('https://tinder.com')

        sleep(5)

        fb_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/div[2]/button')
        fb_btn.click()

        # s2itch to login pupup
        base_window = self.driver.window_handles[0]
        popup = self.driver.window_handles[1]

        self.driver.switch_to.window(self.driver.window_handles[1])

        email_in = self.driver.find_element_by_xpath('//*[@id="email"]')
        email_in.send_keys(username)

        pw_in = self.driver.find_element_by_xpath('//*[@id="pass"]')
        pw_in.send_keys(passwords)

        login_btn = self.driver.find_element_by_xpath('//*[@id="u_0_0"]') 
        login_btn.click()

        self.driver.switch_to.window(base_window)

        sleep(3)

        gps_btn_allow = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')        
        gps_btn_allow.click()

        sleep(2)

        denni_push = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        denni_push.click()

bot = TinderBot()
bot.login()