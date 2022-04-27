from disnake.ext import commands
from numpy import random
import requests
import json

class GeneralPurpose(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(description='Get random duck image')
    async def duck(self, inter):
        await inter.response.send_message(requests.get('https://random-d.uk/api/v1/random').json()['url'])

    
    @commands.slash_command(description='Shorten any URL')
    async def shorten(self, inter, url):
        
        if not url:
            return await inter.response.send_message('Please provide a URL to shorten')

        if not url.startswith('http'):
            url = 'http://' + url

        base_url = 'https://api.1pt.co/addURL'
        params = {'long': url}
        r = requests.get(base_url, params=params)

        if r.status_code != (200 or 201):
            return await inter.response.send_message('Something went wrong')

        output = r.json()['short']
        await inter.response.send_message(output)

    
    @commands.slash_command(description='Get a YoMomma joke')
    async def yomomma(self, inter):
        # get joke
        yomomma = requests.get('https://yomomma-api.herokuapp.com/jokes')
        if yomomma:
            return await inter.response.send_message(json.loads(yomomma.text)['joke'])
        else:
            return await inter.response.send_message('Sorry, there was an error getting yo momma')


    @commands.slash_command(description='Decode a QR code by providing a ')
    async def qr(self, inter, url): pass

    

    


def setup(bot):
    bot.add_cog(GeneralPurpose(bot))