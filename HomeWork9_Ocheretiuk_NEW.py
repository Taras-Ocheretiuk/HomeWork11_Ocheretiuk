from selenium import webdriver
from selenium.webdriver import Keys
import time

driver = webdriver.Chrome()
driver.maximize_window()

sites = ["https://itvdn.com/ua", "https://qalight.ua/", "https://dou.ua/", "https://www.nixsolutions.com/ua/", "https://ain.ua/", "https://savelife.in.ua/", "https://careers.temabit.com/", "https://www.softserveinc.com/uk-ua", "https://intecracy.com/ua/", "https://evo.company/"]

for url in sites:
    driver.get(url)

    if url == "https://itvdn.com/ua":
        about_button = driver.find_element("xpath", "/html/body/div[1]/div[2]/div[1]/ul/li[1]/a/div/span[2]")
        about_button.click()
        time.sleep(2)

        about_button = driver.find_element("xpath", "/html/body/div[3]/div[2]/div/div[2]/ul/li[1]/div[1]")
        about_button.click()
        time.sleep(2)

        about_button = driver.find_element("xpath", "/html/body/div[3]/div[2]/div/div[2]/ul/li[1]/div[2]/ul/li[2]")
        about_button.click()
        time.sleep(2)

    elif url == "https://qalight.ua/":
        about_button = driver.find_element("xpath","/html/body/div[3]/div/div[2]/div/div[3]/ul/li[2]/a")
        about_button.click()
        time.sleep(2)

        about_button = driver.find_element("xpath", "/html/body/div[3]/div/div[4]/div/ul/li[3]/a/img")
        about_button.click()
        time.sleep(2)

        about_button = driver.find_element("xpath", "/html/body/div[4]/div[2]/div[3]/div/div[1]/div[1]/div/div/div[4]/div/div[2]/div[2]/a")
        about_button.click()
        time.sleep(2)

    elif url == "https://dou.ua/":
        about_button = driver.find_element("xpath", "/html/body/div[1]/header/ul/li[6]/a")
        about_button.click()
        time.sleep(2)

        input_dou_position = driver.find_element("xpath","/html/body/div[2]/div[1]/div[1]/div[2]/form/span/input")
        input_dou_position.send_keys("automation")
        time.sleep(1)

        about_button = driver.find_element("xpath", "/html/body/div[2]/div[1]/div[1]/div[2]/form/span/label/input")
        about_button.click()
        time.sleep(2)

        about_button = driver.find_element("xpath", "/html/body/div[2]/div[1]/div[1]/div[2]/form/input")
        about_button.click()
        time.sleep(2)

    elif url == "https://www.nixsolutions.com/ua/":
        about_button = driver.find_element("xpath", "/html/body/div[1]/div[2]/div/div[1]/div[1]/ul[2]/li[1]/a")
        about_button.click()
        time.sleep(2)

        about_button = driver.find_element("xpath", "/html/body/div[1]/div[2]/div/div[1]/div[1]/ul[2]/li[2]/a")
        about_button.click()
        time.sleep(2)

        about_button = driver.find_element("xpath", "/html/body/div[1]/div[2]/div/div[1]/div[1]/ul[2]/li[3]/a")
        about_button.click()
        time.sleep(2)

    elif url == "https://ain.ua/":
        about_button = driver.find_element("xpath", "/html/body/div[1]/div[1]/header/div/div[2]/div[2]/div[2]/div/div/a[3]")
        about_button.click()
        time.sleep(2)

        about_button = driver.find_element("xpath", "/html/body/div[1]/div[1]/header/div/div[2]/div[2]/div[1]/nav/ul/li[4]/a")
        about_button.click()
        time.sleep(2)

        about_button = driver.find_element("xpath", "/html/body/div[1]/div[2]/div/div[1]/div[1]/div[2]/div/div[1]/div[2]/a")
        about_button.click()
        time.sleep(2)

    elif url == "https://savelife.in.ua/":
        about_button = driver.find_element("xpath", "/html/body/header/nav[1]/div/div[2]/div/div[2]/ul/li[2]/a")
        about_button.click()
        time.sleep(2)

        about_button = driver.find_element("xpath", "/html/body/header/nav[2]/div/ul/li[2]/a")
        about_button.click()
        time.sleep(2)

        about_button = driver.find_element("xpath", "/html/body/div[1]/main/div[2]/div[1]/article/a/div/img")
        about_button.click()
        time.sleep(2)

    elif url == "https://careers.temabit.com/":
        about_button = driver.find_element("xpath", "/html/body/div[1]/div[1]/header/div[2]/div/div/div/div/div[2]/div[1]/nav/ul/li[8]/a/div/span/span")
        about_button.click()
        time.sleep(2)

        about_button = driver.find_element("xpath", "/html/body/div[1]/div[1]/header/div[2]/div/div/div/div/div[2]/div[1]/nav/ul/li[4]/a/div/span")
        about_button.click()
        time.sleep(3)

        about_button = driver.find_element("xpath", "/html/body/div[1]/div[1]/div[2]/div/div/div[1]/div/div/div/ul/li[2]/a")
        about_button.click()
        time.sleep(3)

    elif url == "https://www.softserveinc.com/uk-ua":
        about_button = driver.find_element("xpath", "/html/body/div/div[1]/header/div/div/button[2]")
        about_button.click()
        time.sleep(2)

        about_button = driver.find_element("xpath", "/html/body/div/div/header/div[2]/ul[1]/li[4]/a")
        about_button.click()
        time.sleep(2)

        about_button = driver.find_element("xpath", "/html/body/div/div/header/div[2]/div/ul/li[2]/ul/li[1]/a")
        about_button.click()
        time.sleep(2)

    elif url == "https://intecracy.com/ua/":
        about_button = driver.find_element("xpath", "/html/body/div[1]/div/header/div/div/div/div[2]/div/div[1]/div[1]/div/div/ul/li[2]/a/img")
        about_button.click()
        time.sleep(4)

        about_button = driver.find_element("xpath", "/html/body/div[1]/div/header/div/div/div/div[2]/div/div[1]/nav/ul/li[4]/a")
        about_button.click()
        time.sleep(2)

        about_button = driver.find_element("xpath", "/html/body/div[1]/div/section[2]/div/main/div/div[2]/div/section[1]/div/div/div[1]/div/div/div[2]/div/div/a")
        about_button.click()
        time.sleep(2)

    elif url == "https://evo.company/":
        about_button = driver.find_element("xpath", "/html/body/header/div[2]/div/div[2]/div/ul/li[3]/a")
        about_button.click()
        time.sleep(5)

        about_button = driver.find_element("xpath", "/html/body/main/div/div[2]/div/ul/li[3]/a")
        about_button.click()
        time.sleep(5)

        about_button = driver.find_element("xpath", "/html/body/main/div/div[2]/div/div/div/div[2]/a")
        about_button.click()
        time.sleep(2)