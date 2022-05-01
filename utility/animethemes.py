from Screenshot import Screenshot_Clipping
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

opt = webdriver.ChromeOptions()
# opt.add_argument('--headless')
opt.add_argument('--disable-gpu')
# opt.add_argument('--no-sandbox')
# opt.add_argument('--disable-dev-shm-usage')
resolution = "--window-size=1920,1080"
opt.add_argument(resolution)

# Initialize the service object
service = Service(r'C:\Selenium\chromedriver_win32\chromedriver.exe')
# path = r'C:\Selenium\chromedriver_win32\chromedriver.exe'
driver = webdriver.Chrome(service=service, options=opt)


url = 'https://staging.animethemes.moe/wiki/year/2022/spring'

driver.get(url)

# wait until class 'sc-9dda2cb1-0 sc-9dda2cb1-2 cCwEUd mdvVS' is loaded
# WebDriverWait(driver, 10).until(EC.presence_of_element_located(
#     (By.CLASS_NAME, 'sc-d6e4af9-0 sc-245a8d1-1 gizjzL gYpFKh')))

divs = driver.find_element(By.TAG_NAME, 'div')
# print(divs)

# find every a tag inside divs
a_tags = divs.find_elements(By.TAG_NAME, 'a')

anime_links = []
# for each a tag, get the href attribute
for a in a_tags:
    # print(a.get_attribute('href'))
    ref = str(a.get_attribute('href'))
    if 'OP' in ref or 'ED' in ref:
        anime_links.append(ref)

driver.close()
driver.quit()

print(anime_links)