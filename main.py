from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from Lands import list_of_lands
from Single_page import single_page
from pagination import next_page
import csv



chrome_options = Options()
chrome_options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.6367.207 Safari/537.36')

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)
wait = WebDriverWait(driver, 10)

lands = list_of_lands(driver=driver)
sleep(1)

    


all_pages = []   

for land in lands :
    
    url = f"https://eacva.de/de/mitgliedschaft/mitgliedersuche?filter_nachname=&filter_vorname=&filter_firma=&filter_taetigkeitsgebiete=&filter_freitext=&filter_cva=0&filter_plz=&filter_ort=&filter_land={land}&filter_umkreissuche=&filter_order=&filter_order_Dir=&76cdaad2644d1dc01f1e70d718f090dc=1"

    driver.get(url)
    content = driver.page_source
    
    while True :

                    
                    page = single_page(content)
                    try :    
                        all_pages += page
                    except :
                            pass
                    try :
                        next_page(driver=driver)
                        content = driver.page_source
                    except :
                        break


print(all_pages)

data_fixed = [
    {k: (v if v != "" else " ") for k, v in row.items()}
    for row in all_pages
]


with open('output.csv', 'w', newline='', encoding='utf-8') as csvfile:
    # Get headers from keys of the first dict
    fieldnames = data_fixed[0].keys()
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data_fixed)


