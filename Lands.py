from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep

cities = []


def list_of_lands(driver) :
       
        wait = WebDriverWait(driver, 10)
        driver.get("https://eacva.de/de/mitgliedschaft/mitgliedersuche")

        wait.until(EC.presence_of_element_located((By.ID, "filter_land")))
        select_element = driver.find_element(By.ID, "filter_land")
        select_element.location_once_scrolled_into_view
        sleep(1)
        options = select_element.find_elements(By.TAG_NAME, "option")
        for option in options :
                cities.append(option.text.strip())

        return cities
