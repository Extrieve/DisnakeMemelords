from disnake.ext import commands
from selenium import webdriver
from Screenshot import Screenshot_Clipping
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from PIL import Image
import disnake
import validators
import time
import requests

class Automation(commands.Cog):
    """Automation Cog dedicated to scrape data using Selenium and/or BeautifulSoup."""

    opt = webdriver.ChromeOptions()
    opt.add_argument('--headless')
    opt.add_argument('--disable-gpu')
    opt.add_argument('--no-sandbox')
    opt.add_argument('--disable-dev-shm-usage')
    resolution = "--window-size=1920,1080"
    opt.add_argument(resolution)
    try:
        service = Service(r'/home/nick/Documents/chromedriver') # Linux path
        # service = Service(r'C:\Selenium\chromedriver.exe') # Windows Path
        driver = webdriver.Chrome(service=service, options=opt)
    except Exception:
        print('WebdriverException: Please check the path of the chromedriver')

    regions = {'na': ('North America', '🇺🇸'), 'euw': ('Europe West', '🇪🇺'), 'br': (
        'Brazil', '🇧🇷'), 'las': ('LAS', '🇵🇪'), 'lan': ('LAN', '🇲🇽')}

    flags = [item[1] for item in regions.values()]
    regions_copy = regions.copy()
    Regions = commands.option_enum([item for item in regions.keys()])

    def __init__(self, bot):
        self.bot = bot


    def get_download_url(self, video_url):
        url = 'https://en.y2mate.is/54/youtube-to-mp4.html'
        self.driver.get(url)
        self.driver.find_element_by_id('txtUrl').send_keys(video_url)
        self.driver.find_element_by_id('btnSubmit').click()

        # Wait until 'tableVideo' is loaded
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, 'tableVideo')))

        table = self.driver.find_element_by_class_name('tableVideo')

        # iterate through the table and save information
        for row in table.find_elements_by_tag_name('tr'):
            # the third element of the row is a button, which we click to download the video
            for td in row.find_elements_by_tag_name('td'):
                
                # if td contains button, click it
                if td.find_elements_by_tag_name('button'):
                    button = td.find_element(By.TAG_NAME, 'button')
                    button.click()
                    # wait 5 seconds and press the button again
                    time.sleep(5)
                    button = td.find_element(By.TAG_NAME, 'button')
                    # get a tag inside the button
                    a = button.find_element(By.TAG_NAME, 'a')
                    # get the href attribute of the a tag
                    href = a.get_attribute('href')
                    return href

        return None

    @commands.slash_command(name='twitter-embed-video', description='Get the embed video of a tweet')
    async def twitter_embed_video(self, inter, url: str) -> None:
        """Get the embed video of a tweet."""
        if not validators.url(url):
            return await inter.response.send_message('Please provide a valid URL', ephemeral=True)

        if 'twitter' not in url:
            return await inter.response.send_message('Please provide a valid Twitter URL', ephemeral=True)

        if '?' in url:
            url = url.split('?')[0]

        await inter.response.defer(with_message='Loading...', ephemeral=False)


        try:
            # wait until class 'card-text' is loaded
            site = 'https://www.savetweetvid.com/'
            self.driver.get(site)
            element = self.driver.find_element(By.NAME, 'url')
            element.send_keys(url)
            element.submit()
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'card-text'))
            )

            # store table tag
            table = self.driver.find_element(By.TAG_NAME, 'table')

            links = []
            # append the links inside the table to the list
            for row in table.find_elements(By.TAG_NAME, 'tr'):
                for link in row.find_elements(By.TAG_NAME, 'a'):
                    links.append(link.get_attribute('href'))

            self.driver.close()
            self.driver.quit()

            return await inter.followup.send(links[0], ephemeral=False)
        
        except Exception:
            url = url.replace('twitter', 'twxtter')
            return await inter.followup.send(f'Embbed server failed, using twxtter embbed...\n{url}', ephemeral=False)


    @commands.slash_command(name='youtube-mp4', description='Get the mp4 of a youtube video')
    async def youtube_mp4(self, inter, url: str) -> None:
        """Get the mp4 of a youtube video."""
        if not validators.url(url):
            return await inter.response.send_message('Please provide a valid URL', ephemeral=True)

        if 'youtube' not in url:
            return await inter.response.send_message('Please provide a valid YouTube URL', ephemeral=True)

        await inter.response.defer(with_message='Loading...', ephemeral=False)

        download_url = self.get_download_url(url)
        print(download_url)

        if download_url:
            r = requests.get(download_url, allow_redirects=True)
            with open('video.mp4', 'wb') as f:
                f.write(r.content)
                return await inter.followup.send(file=disnake.File('video.mp4'), ephemeral=False)
        
        return await inter.followup.send('Something went wrong', ephemeral=False)

    @commands.slash_command(name='opgg-livematch', description='Get the live match of an op.gg summoner')
    async def opgg_livematch(self, inter, summoner: str, region: Regions) -> None: 

        return await inter.response.send_message(f'{summoner} {region}', ephemeral=True)


def setup(bot):
    bot.add_cog(Automation(bot))
