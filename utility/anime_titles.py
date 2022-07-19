# from Screenshot import Screenshot_Clipping
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

opt = webdriver.ChromeOptions()
# opt.add_argument('--headless')
opt.add_argument('--disable-gpu')
# opt.add_argument('--no-sandbox')
# opt.add_argument('--disable-dev-shm-usage')
resolution = "--window-size=1920,1080"
opt.add_argument(resolution)

# Initialize the service object
# service = Service(r'C:\Selenium\chromedriver_win32\chromedriver.exe')
service = Service(r'/home/extrieve/Documents/chromedriver/chromedriver')
# path = r'C:\Selenium\chromedriver_win32\chromedriver.exe'
driver = webdriver.Chrome(service=service, options=opt)


url = 'https://animethemes.moe/year/2022/summer'
driver.get(url)

titles = []

forbidden = ['OP', 'ED', 'Spring 2022', 'Transparency', 'Donate', 'FAQ', 'Terms of Service', 'Privacy Policy',
             'Contact', '', 'SEARCH', 'CURRENT SEASON', 'MY PROFILE', '2021', '2022', 'WINTER', 'SPRING']

for title in driver.find_element(By.TAG_NAME, 'div').find_elements(By.TAG_NAME, 'a'):
    # print(title.text)
    if title.text not in forbidden:
        titles.append(title.text)

driver.close()
driver.quit()

titles = [title for title in titles if title not in forbidden]
print(titles)

titles = ['SUMMER', 'Bastard!! Ankoku no Hakaishin (ONA)', 'Summer 2022', 'Bucchigire!', 'Summer 2022', 'Cardfight!! Vanguard: will+Dress', 'Summer 2022', 'Chimimo', 'Summer 2022', 'Engage Kiss', 'Summer 2022', 'Extreme Hearts', 'Summer 2022', 'Hoshi no Samidare', 'Summer 2022', 'Isekai Meikyuu de Harem wo', 'Summer 2022', 'Isekai Ojisan', 'Summer 2022', 'Jashin-chan Dropkick X', 'Summer 2022', 'Kami Kuzu☆Idol', 'Summer 2022', 'Kanojo, Okarishimasu 2nd Season', 'Summer 2022', 'Kinsou no Vermeil: Gakeppuchi Majutsushi wa Saikyou no Yakusai to Mahou Sekaiwo Tsukisusumu', 'Summer 2022', 'Kumichou Musume to Sewagakari', 'Summer 2022', 'Luminous Witches', 'Summer 2022', 'Lycoris Recoil', 'Summer 2022', 'Made in Abyss: Retsujitsu no Ougonkyou',
          'Summer 2022', 'Mamahaha no Tsurego ga Motokano datta', 'Summer 2022', 'Prima Doll', 'Summer 2022', 'RWBY: Hyousetsu Teikoku', 'Summer 2022', 'Shadows House 2nd Season', 'Summer 2022', 'Shin Tennis no Ouji-sama: U-17 WORLD CUP', 'Summer 2022', 'Shoot! Goal to the Future', 'Summer 2022', 'Soredemo Ayumu wa Yosetekuru', 'Summer 2022', 'Tensei Kenja no Isekai Life: Dai-2 no Shokugyou wo Ete, Sekai Saikyou ni Narimashita', 'Summer 2022', 'Teppen!!!!!!!!!!!!!!!', 'Summer 2022', 'Tokyo Mew Mew New ♡', 'Summer 2022', 'Utawarerumono: Futari no Hakuoro', 'Summer 2022', 'Warau Arsnotoria Sun!', 'Summer 2022', 'Yofukashi no Uta', 'Summer 2022', 'Youkoso Jitsuryoku Shijou Shugi no Kyoushitsu e 2nd Season', 'Summer 2022', 'Yurei Deco', 'Summer 2022']
