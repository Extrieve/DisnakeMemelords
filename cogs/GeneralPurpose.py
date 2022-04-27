from disnake.ext import commands
from numpy import random
import disnake
import requests
import json
import sys, os

class GeneralPurpose(commands.Cog):

    cwd = os.getcwd()
    sys.path.append(f'{cwd}..')
    from config import ame_token, ame_endpoints
    Templates = commands.option_enum(ame_endpoints)

    def __init__(self, bot):
        self.bot = bot


    @commands.slash_command(name='avatar', description='Get the avatar of a user.')
    async def avatar(self, inter, *, user: disnake.Member = None):
        """Get the avatar of a user."""
        if user is None:
            user = inter.author
        await inter.send(user.avatar.url)

    @commands.slash_command(description='Get random duck image')
    async def duck(self, inter):
        await inter.response.send_message(requests.get('https://random-d.uk/api/v1/random').json()['url'])

    
    @commands.slash_command(description='Shorten any URL')
    async def shorten(self, inter, url):
        
        if not url:
            return await inter.response.send_message('Please provide a URL to shorten')

        return await inter.response.send_message('Maintenance, back soon!')
        # TODO: Finish the implementation with an API that's working


    @commands.slash_command(name='meme-generator' ,description='Generate a meme with the available templates')
    async def meme_generator(self, inter, template: Templates=None, img_url: str=None):
        if not template:
            return await inter.response.send_message('Please provide a template')
        
        if not img_url:
            return await inter.response.send_message('Please provide an image URL')
        
        base_url = "https://v1.api.amethyste.moe"
        headers = {'Authorization': f'Bearer {self.ame_token}'}
        data = {'url': img_url}
        r = requests.post(f'{base_url}/generate/{template}', headers=headers, data=data)

        if r.status_code != (200 or 201):
            return await inter.response.send_message(f"Error: {r.status_code}")

        # save request as a png
        with open(f'ame_{template}.png', 'wb') as f:
            f.write(r.content)
        
        # send image
        await inter.response.send_message(file=disnake.File(f'ame_{template}.png'))


    @commands.slash_command(description='Decode a QR code by providing a ')
    async def qr(self, inter, qr_url): 
        if not url:
            return await inter.response.send_message('Please provide a URL to decode')

        url = 'http://api.qrserver.com/v1/read-qr-code/?fileurl='
        r = requests.get(url + qr_url)

        if r.status_code != (200 or 204):
            return await inter.response.send_message(f'Error: {r.status_code}')

        data = r.json()
        return await inter.response.send_message(data[0]['symbol'][0]['data'])

    

    


def setup(bot):
    bot.add_cog(GeneralPurpose(bot))