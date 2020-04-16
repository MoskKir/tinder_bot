from selenium import webdriver
from time import sleep

from secrets import username, passwords

class TinderBot():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get('https://tinder.com')

        sleep(5)

        cookies_agree_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div/div[1]/div/button')
        cookies_agree_btn.click()

        sleep(2)
        fb_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[2]/button/span[2]')
        fb_btn.click()

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

        sleep(10)

        gps_btn_allow = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        gps_btn_allow.click()

        sleep(2)

        denni_push = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        denni_push.click()

        sleep(2)

        denni_world_popup = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button/span')
        denni_world_popup.click()

    def like(self):
        luis_btn = self.driver.find_element_by_xpath(
            '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
        luis_btn.click()

    def dislike(self):
        disluis_btn = self.driver.find_element_by_xpath()
        disluis_btn.click()

    def close_popup(self):
        sleep(5)
        add_to_main_popup = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button[2]')
        add_to_main_popup.click()

    def close_match(self):
        sleep(5)
        match_popup = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button[2]')
        match_popup.click()

    def swipe_right(self):
        from random import random
        left_count = 0
        right_count = 0
        while True:
            sleep(0.5)
            try:
                rand = random()
                if rand < .73:
                    self.like()
                    right_count = right_count + 1
                    print('{} right swipe'.format(right_count))
                else:
                    self.dislike()
                    left_count = left_count + 1
                    print('{} left swipe'.format(left_count))
            except Exception:
                try:
                    self.close_popup()
                except Exception:
                    self.close_match()


bot = TinderBot()
bot.login()
bot.swipe_right()
