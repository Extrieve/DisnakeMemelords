from Screenshot import Screenshot_Clipping
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
service = Service(r'C:\Selenium\chromedriver_win32\chromedriver.exe')
# path = r'C:\Selenium\chromedriver_win32\chromedriver.exe'
driver = webdriver.Chrome(service=service, options=opt)


url = 'https://staging.animethemes.moe/wiki/year/2022/spring'
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

titles = ['Aharen-san wa Hakarenai', 'Ao Ashi', "Birdie Wing: Golf Girls' Story", 'Black★★Rock Shooter: Dawn Fall', 'Build Divide: Code White', 'Cap Kakumei Bottleman DX', 'Dance Dance Danseur', 'Date A Live IV', 'Deaimon', 'Estab-Life: Great Escape', 'Gaikotsu Kishi-sama, Tadaima Isekai e Odekakechuu', 'Gunjou no Fanfare', 'Healer Girl', 'Heroine Tarumono! Kiraware Heroine to Naisho no Oshigoto', 'Honzuki no Gekokujou: Shisho ni Naru Tame ni wa Shudan wo Erandeiraremasen 3rd Season', 'Insect Land', 'Kaginado Season 2', 'Kaguya-sama wa Kokurasetai: Ultra Romantic', 'Kawaii dake ja Nai Shikimori-san', 'Kingdom 4th Season', 'Koi wa Sekai Seifuku no Ato de', 'Komi-san wa, Comyushou desu. 2nd Season', 'Kono Healer, Mendokusai', 'Kunoichi Tsubaki no Mune no Uchi', 'ED1', 'Kyoukai Senki Part 2', 'Love All Play',
          'Love Live! Nijigasaki Gakuen School Idol Doukoukai 2nd Season', 'Machikado Mazoku: 2-choume', 'Magia Record: Mahou Shoujo Madoka☆Magica Gaiden (TV) Final Season - Asaki Yume no Akatsuki', 'ED1', 'Mahoutsukai Reimeiki', 'Meitantei Conan: Zero no Tea Time', 'Onipan!', 'Otome Game Sekai wa Mob ni Kibishii Sekai desu', 'Paripi Koumei', 'ED1', 'Rikei ga Koi ni Ochita no de Shoumei shitemita. r=1-sinθ (Heart)', 'RPG Fudousan', 'Shachiku-san wa Youjo Yuurei ni Iyasaretai.', 'Shadowverse Flame', 'Shijou Saikyou no Daimaou, Murabito A ni Tensei suru', 'Shokei Shoujo no Virgin Road', 'Spy x Family', 'Summer Time Render', 'Tate no Yuusha no Nariagari Season 2', 'Thermae Romae Novae', 'Tiger & Bunny 2', 'Tomodachi Game', 'Ultraman Season 2', 'Yatogame-chan Kansatsu Nikki 4th Season', 'Yu-Gi-Oh! Go Rush!!', 'Yuusha, Yamemasu']
