from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep

def next_page(driver) :

    wait = WebDriverWait(driver, 10)

    next_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a.next")))
    element = driver.find_element(By.CSS_SELECTOR, "a.next")

    element.location_once_scrolled_into_view

    sleep(0.5)

    next_link.click()
    sleep(0.5)
