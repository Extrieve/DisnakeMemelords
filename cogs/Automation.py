from disnake.ext import commands
from selenium import webdriver
from Screenshot import Screenshot_Clipping
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from PIL import Image
import disnake
import asyncio
import os
import validators

class Automation(commands.Cog):
    """Automation Cog dedicated to scrape data using Selenium and/or BeautifulSoup."""

    chrome_options = webdriver.ChromeOptions()

    resolution = "--window-size=1920,1080"
    chrome_options.add_argument(resolution)
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    service = Service(os.environ.get("CHROMEDRIVER_PATH"))
    driver = webdriver.Chrome(service=service, chrome_options=chrome_options)

    regions = {'na': ('North America', '🇺🇸'), 'euw': ('Europe West', '🇪🇺'), 'br': (
        'Brazil', '🇧🇷'), 'las': ('LAS', '🇵🇪'), 'lan': ('LAN', '🇲🇽')}

    flags = [item[1] for item in regions.values()]
    # regions_copy = regions.copy()
    Regions = commands.option_enum([item for item in regions.keys()])

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
        

    @commands.slash_command(name='opgg-livematch', description='Get the live match of an op.gg summoner')
    async def opgg_livematch(self, inter, summoner, region: Regions): 

        return await inter.response.send_message(f'{summoner} {region}', ephemeral=True)
        # TODO: Implement the rest of the functionality


def setup(bot):
    bot.add_cog(Automation(bot))