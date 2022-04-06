from xml.dom.minidom import Element
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException   
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.webdriver.chrome.options import Options
import os

def runScript(keyword):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = os.environ.get('GOOGLE_CHROME_BIN')

    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")

    driver=webdriver.Chrome(executable_path=os.environ.get('CHROMEDRIVER_PATH'), chrome_options=chrome_options)

    url = "https://h-supertools.com/youtube/youtube-keyword-tool?searchTerm=" + keyword

    driver.get(url)
    driver.implicitly_wait(20)

    k1 = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div[2]/div[1]/div[3]/div/div/div/div[3]/div/div[3]/div[2]/table/tbody/tr[1]/td[1]").text
        vol1 = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div[2]/div[1]/div[3]/div/div/div/div[3]/div/div[3]/div[2]/table/tbody/tr[1]/td[2]").text
        diff1 = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div[2]/div[1]/div[3]/div/div/div/div[3]/div/div[3]/div[2]/table/tbody/tr[2]/td[3]").text
        
        k2 = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div[2]/div[1]/div[3]/div/div/div/div[3]/div/div[3]/div[2]/table/tbody/tr[2]/td[1]").text
        vol2 = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div[2]/div[1]/div[3]/div/div/div/div[3]/div/div[3]/div[2]/table/tbody/tr[2]/td[2]").text
        diff2 = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div[2]/div[1]/div[3]/div/div/div/div[3]/div/div[3]/div[2]/table/tbody/tr[2]/td[3]").text

        k3 = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div[2]/div[1]/div[3]/div/div/div/div[3]/div/div[3]/div[2]/table/tbody/tr[3]/td[1]").text
        vol3 = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div[2]/div[1]/div[3]/div/div/div/div[3]/div/div[3]/div[2]/table/tbody/tr[3]/td[2]").text
        diff3 = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div[2]/div[1]/div[3]/div/div/div/div[3]/div/div[3]/div[2]/table/tbody/tr[3]/td[3]").text

        k4 = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div[2]/div[1]/div[3]/div/div/div/div[3]/div/div[3]/div[2]/table/tbody/tr[4]/td[1]").text
        vol4 = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div[2]/div[1]/div[3]/div/div/div/div[3]/div/div[3]/div[2]/table/tbody/tr[4]/td[2]").text
        diff4 = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div[2]/div[1]/div[3]/div/div/div/div[3]/div/div[3]/div[2]/table/tbody/tr[4]/td[3]").text

        k5 = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div[2]/div[1]/div[3]/div/div/div/div[3]/div/div[3]/div[2]/table/tbody/tr[5]/td[1]").text
        vol5 = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div[2]/div[1]/div[3]/div/div/div/div[3]/div/div[3]/div[2]/table/tbody/tr[5]/td[2]").text
        diff5 = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div[2]/div[1]/div[3]/div/div/div/div[3]/div/div[3]/div[2]/table/tbody/tr[5]/td[3]").text

        k6 = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div[2]/div[1]/div[3]/div/div/div/div[3]/div/div[3]/div[2]/table/tbody/tr[6]/td[1]").text
        vol6 = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div[2]/div[1]/div[3]/div/div/div/div[3]/div/div[3]/div[2]/table/tbody/tr[6]/td[2]").text
        diff6 = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div[2]/div[1]/div[3]/div/div/div/div[3]/div/div[3]/div[2]/table/tbody/tr[6]/td[3]").text

        k7 = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div[2]/div[1]/div[3]/div/div/div/div[3]/div/div[3]/div[2]/table/tbody/tr[7]/td[1]").text
        vol7 = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div[2]/div[1]/div[3]/div/div/div/div[3]/div/div[3]/div[2]/table/tbody/tr[7]/td[2]").text
        diff7 = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div[2]/div[1]/div[3]/div/div/div/div[3]/div/div[3]/div[2]/table/tbody/tr[7]/td[3]").text

        k8 = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div[2]/div[1]/div[3]/div/div/div/div[3]/div/div[3]/div[2]/table/tbody/tr[8]/td[1]").text
        vol8 = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div[2]/div[1]/div[3]/div/div/div/div[3]/div/div[3]/div[2]/table/tbody/tr[8]/td[2]").text
        diff8 = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div[2]/div[1]/div[3]/div/div/div/div[3]/div/div[3]/div[2]/table/tbody/tr[8]/td[3]").text

        k9 = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div[2]/div[1]/div[3]/div/div/div/div[3]/div/div[3]/div[2]/table/tbody/tr[9]/td[1]").text
        vol9 = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div[2]/div[1]/div[3]/div/div/div/div[3]/div/div[3]/div[2]/table/tbody/tr[9]/td[2]").text
        diff9 = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div[2]/div[1]/div[3]/div/div/div/div[3]/div/div[3]/div[2]/table/tbody/tr[9]/td[3]").text

        k10 = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div[2]/div[1]/div[3]/div/div/div/div[3]/div/div[3]/div[2]/table/tbody/tr[10]/td[1]").text
        vol10 = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div[2]/div[1]/div[3]/div/div/div/div[3]/div/div[3]/div[2]/table/tbody/tr[10]/td[2]").text
        diff10 = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div[2]/div[1]/div[3]/div/div/div/div[3]/div/div[3]/div[2]/table/tbody/tr[10]/td[3]").text


        l1 = [k1,vol1,diff1]
        l2 = [k2,vol2,diff2]
        l3 = [k3,vol3,diff3]
        l4 = [k4,vol4,diff4]
        l5 = [k5,vol5,diff5]
        l6 = [k6,vol6,diff6]
        l7 = [k7,vol7,diff7]
        l8 = [k8,vol8,diff8]
        l9 = [k9,vol9,diff9]
        l10 = [k10,vol10,diff10]

        keyword_dict = {
            "Keyword_1" : l1,
            "Keyword_2" : l2,
            "Keyword_3" : l3,
            "Keyword_4" : l4,
            "Keyword_5" : l5,
            "Keyword_6" : l6,
            "Keyword_7" : l7,
            "Keyword_8" : l8,
            "Keyword_9" : l9,
            "Keyword_10" : l10,
        }
    driver.quit()

    return(keyword_dict)
