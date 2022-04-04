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

    txt = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div[2]/div[1]/div[3]/div/div/div/div[3]/div/div[3]/div[2]/table/tbody/tr[1]/td[1]").text
    driver.quit()

    return(txt)
