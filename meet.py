from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import pyttsx3

id = "malhaar144211@dps45gurgaon.org"
password = "he110dps"

chromedriver = r"C:\Users\Malhaar\Downloads\chromedriver_win32 (1)\chromedriver.exe"
driver = webdriver.Chrome(chromedriver)

def login():
    driver.get("https://mail.google.com/mail/u/0/#inbox")

    driver.find_element_by_id("identifierId").send_keys(id)
    driver.find_element_by_xpath("""//*[@id="identifierNext"]/span""").click()
    sleep(10)

    driver.find_element_by_xpath("""//*[@id="password"]/div[1]/div/div[1]/input""").send_keys(password)
    driver.find_element_by_xpath("""//*[@id="passwordNext"]/span/span""").click()
    sleep(120)


def close_last_tab():

    if (len(driver.window_handles) == 2):

        driver.switch_to.window(window_name=driver.window_handles[0])

        driver.close()

        driver.switch_to.window(window_name=driver.window_handles[0])


def participants():
    elem = driver.find_element_by_xpath("""//*[@id="ow4"]/div[1]/div/div[4]/div[3]/div[6]/div[3]/div/div[2]/div[1]/span/span/div/div/span[2]""")
    val = float(elem.get_attribute('innerHTML'))
    print(val)
    if val < 15:
        engine = pyttsx3.init()
        engine.setProperty('rate', 150)
        engine.say("Aborting meeting in 6...5...4...3...2...1")
        engine.runAndWait()
        driver.close()
    sleep(2)

login()
close_last_tab()
while True:
    participants()
