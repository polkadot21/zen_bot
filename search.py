import webbrowser
import time
from selenium import webdriver

import random

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from http_request_randomizer.requests.proxy.requestProxy import RequestProxy
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import TimeoutException




req_proxy = RequestProxy()  # you may get different number of proxy when  you run this at each time
proxies = req_proxy.get_proxy_list()  # this will create proxy list

number_of_proxies = len(proxies)


google = "http://www.google.com"
yandex = 'http://www.yandex.ru'
zen = 'https://zen.yandex.ru/profile/editor/id/5f2e835e6204c24f181bd498'

for i in range(number_of_proxies):



    #start webdriver
    proxy = proxies[i].get_address()

    #split ip and port
    proxy = proxy.split(':')
    ip = proxy[0]
    port = proxy[1]


    options = FirefoxOptions()
    options.add_argument("--headless")
    profile = webdriver.FirefoxProfile()
    profile.set_preference("network.proxy.type", 1)
    profile.set_preference("network.proxy.http", ip)
    profile.set_preference("network.proxy.http_port", port)
    profile.set_preference("network.proxy.ssl", ip)
    profile.set_preference("network.proxy.ssl_port", port)

    # profile.set_preference('network.proxy.socks_port', port)
    # profile.set_preference('network.proxy.control_port', port_2)
    # profile.update_preferences()
    profile.update_preferences()

    driver = webdriver.Firefox(firefox_profile=profile,
                               #options=options,
                               executable_path='/Users/e.saurov/PycharmProjects/novoe_bakeevo/geckodriver')




    driver.get(zen)

    #search in yandex
    #que = driver.find_element_by_xpath('//*[@id="text"]')
    #que.send_keys("таунхаусы рядом с зеленоградом")
    #que.send_keys(Keys.RETURN)
    #time.sleep(random.randint(3, 10))

    xpath_bakeevopark = '/html/body/div[3]/div[1]/div[2]/div[1]/div[1]/ul/li[5]/div/h2/a'
    xpath_4_pages = '/html/body/div[3]/div[1]/div[2]/div[1]/div[1]/div[3]/div/a[3]'
    xpath_first_article = '/html/body/div[2]/div[1]/div[2]/div[2]/div/div[2]/div[5]/div[2]/div[2]/div/div/div/a'
    xpath_first_article_metrics = '/html/body/div[2]/div[1]/div[2]/div[2]/div/div[2]/div[5]/div[3]/div[2]/div/div/div/a'
    xpath_last_article = '/html/body/div[2]/div[1]/div[2]/div[2]/div/div[2]/div[5]/div[1]/div[1]/div/div/div/a'
    xpath_site = '/html/body/div[3]/article/div/div[2]/div[5]/div/p[1]/a'


    try:
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH, xpath_first_article))).click()
    except TimeoutException:
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH, xpath_first_article_metrics))).click()

    try:
        WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))
        next_window = driver.window_handles[1]
        driver.switch_to_window(next_window)
    except TimeoutException:
        time.sleep(random.randint(5, 10))
        WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))
        next_window = driver.window_handles[1]
        driver.switch_to_window(next_window)


    y = 150
    for timer in range(0, random.randint(30, 50)):

        driver.execute_script("window.scrollTo(0, " + str(y) + ")")
        y +=50
        time.sleep(3)

    try:
        WebDriverWait(driver, 1).until(EC.element_to_be_clickable(
            (By.XPATH, xpath_site))).click()
        time.sleep(random.randint(2,7))
    except ElementClickInterceptedException:
        xpath_subscribe = '/html/body/div[3]/div[1]/div[2]/div[1]/a/span[2]/span[3]/button/span'
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
            (By.XPATH, random.choice(xpath_subscribe)))).click()
        xpath_close = '/html/body/div[3]/div[1]/div[2]/div[1]/a/span[2]/button'
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
            (By.XPATH, xpath_close))).click()
        time.sleep(random.randint(1,5))
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
            (By.XPATH, xpath_site))).click()
        time.sleep(random.randint(2, 7))


    WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(3))
    next_window = driver.window_handles[2]
    driver.switch_to_window(next_window)




    #go down
    #driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    #WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
        #(By.XPATH, xpath_4_pages))).click()
    #time.sleep(random.randint(5,10))

    #go to website
    #WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
        #(By.XPATH, xpath_bakeevopark))).click()

    #change windows

    #WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))
    #next_window = driver.window_handles[1]
    #driver.switch_to_window(next_window)
    #time.sleep(random.randint(5, 10))




    #first algorithm (watch photos)
    xpath_photogalerie = '/html/body/nav/div/div[2]/ul/li[9]/a'
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
        (By.XPATH, xpath_photogalerie))).click()
    time.sleep(random.randint(5, 10))

    #exterior
    xpath_ext = '/html/body/div[5]/div/div/div[1]/a'
    xpath_next = '/html/body/div[5]/div/div/div/a[2]/span[1]/span'

    #interior
    xpath_int = '/html/body/div[5]/div/div/div[2]/a'

    #stroit
    xpath_stroit = '/html/body/div[5]/div/div/div[3]/a'

    photos_list = [xpath_ext, xpath_int, xpath_stroit]

    #choice ext, int or stroit in galery
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
        (By.XPATH, random.choice(photos_list)))).click()
    time.sleep(random.randint(5,10))

    #swipe photos
    for j in range(1, random.randint(3,8)):
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH, xpath_next))).click()

    driver.quit()

    print("done:", i + 1, "times")