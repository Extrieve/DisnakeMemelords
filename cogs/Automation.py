from disnake.ext import commands
import disnake
from selenium import webdriver
from Screenshot import Screenshot_Clipping
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from PIL import Image
import asyncio
import os
import validators

class Automation(commands.Cog):
    """Automation Cog dedicated to scrape data using Selenium and/or BeautifulSoup."""

    opt = webdriver.ChromeOptions()
    opt.add_argument('--headless')
    opt.add_argument('--disable-gpu')
    opt.add_argument('--no-sandbox')
    opt.add_argument('--disable-dev-shm-usage')
    resolution = "--window-size=1920,1080"
    opt.add_argument(resolution)
    service = Service(r'C:\Selenium\chromedriver_win32\chromedriver.exe')
    driver = webdriver.Chrome(service=service, options=opt)

    regions = {'na': ('North America', '🇺🇸'), 'euw': ('Europe West', '🇪🇺'), 'br': (
        'Brazil', '🇧🇷'), 'las': ('LAS', '🇵🇪'), 'lan': ('LAN', '🇲🇽')}

    flags = [item[1] for item in regions.values()]
    # regions_copy = regions.copy()
    # Regions = commands.option_enum(regions_copy.keys())

    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name='twitter-embed-video', description='Get the embed video of a tweet')
    async def twitter_embed_video(self, inter, url):
        """Get the embed video of a tweet."""
        if not validators.url(url):
            return await inter.response.send_message('Please provide a valid URL', ephemeral=True)

        if 'twitter' not in url:
            return await inter.response.send_message('Please provide a valid Twitter URL', ephemeral=True)

        await inter.response.defer(with_message='Loading...', ephemeral=False)

        site = 'https://www.savetweetvid.com/'
        self.driver.get(site)
        element = self.driver.find_element(By.NAME, 'url')
        element.send_keys(url)
        element.submit()

        # wait until class 'card-text' is loaded
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
        


def setup(bot):
    bot.add_cog(Automation(bot))
