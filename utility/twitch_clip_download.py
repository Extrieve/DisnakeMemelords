from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC

# Chromedriver path = '/c/Users/nicol/Documents/selenium/chromedriver.exe'
# service = Service(r'/c/Users/nicol/Documents/selenium/chromedriver.exe')
service = Service(r'C:\\Selenium\\chromedriver.exe')
driver = webdriver.Chrome(service=service)

clip_url = 'https://clips.twitch.tv/AbnegateDeafSageBrainSlug'
download_clip_url = 'https://clipsey.com/'

# find the input box where class='clip-url-input' and send the clip url
driver.get(download_clip_url)
input_box = driver.find_element_by_class_name('clip-url-input')
input_box.send_keys(clip_url)

# look for button with class='get-download-link-button' and click it
download_button = driver.find_element_by_class_name('get-download-link-button')
download_button.click()

# wait until img tab is visible
wait(driver, 10).until(EC.visibility_of_element_located((By.TAG_NAME, 'img')))

a_tags = driver.find_elements_by_tag_name('a')
for a in a_tags:
    # if a tag starts with 'https://clips-media-assets2.twitch.tv/' then print it and break
    if a.get_attribute('href').startswith('https://clips-media-assets2.twitch.tv/'):
        print(a.get_attribute('href'))
        break
