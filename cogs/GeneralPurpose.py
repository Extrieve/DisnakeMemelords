from disnake.ext import commands
from numpy import random
import disnake
import requests
import json
import sys, os
import validators

class GeneralPurpose(commands.Cog):

    cwd = os.getcwd()
    sys.path.append(f'{cwd}..')
    from config import ame_token, ame_endpoints, bg_key
    Templates = commands.option_enum(ame_endpoints)

    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name='avatar', description='Get the avatar of a user.')
    async def avatar(self, inter, *, user: disnake.Member = None):
        """Get the avatar of a user."""
        if user is None:
            user = inter.author
        await inter.send(user.avatar.url)
        
    
    @commands.slash_command(name='shorten-url', description='Shorten any URL')
    async def shorten(self, inter, url):
        
        if not validators.url(url):
            return await inter.response.send_message('Please provide a valid URL', ephemeral=True)

        base_url = 'https://gotiny.cc/api'
        headers = {'Accept': 'application/json'}
        params = {'input': url}
        r = requests.post(base_url, headers=headers, json=params)

        if r.status_code != 200:
            return await inter.response.send_message('Something went wrong', ephemeral=True)

        data = json.loads(r.text)
        res = 'https://gotiny.cc/' + data[0]['code']
        await inter.response.send_message(res)


    @commands.slash_command(name='meme-generator' ,description='Generate a meme with the available templates')
    async def meme_generator(self, inter, img_url: str, template: Templates):
        
        if not validators.url(img_url):
            return await inter.response.send_message('Please provide a valid URL', ephemeral=True)
        
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
        
        if not validators.url(qr_url):
            return await inter.response.send_message('Please provide a valid URL', ephemeral=True)

        url = 'http://api.qrserver.com/v1/read-qr-code/?fileurl='
        r = requests.get(url + qr_url)

        if r.status_code != (200 or 204):
            return await inter.response.send_message(f'Error: {r.status_code}')

        data = r.json()
        return await inter.response.send_message(data[0]['symbol'][0]['data'])


    @commands.slash_command(name='remove-background', description='Remoe the background of an image')
    async def remove_background(self, inter, img_url: str):
        if not validators.url(img_url):
            return await inter.response.send_message('Please provide a valid URL', ephemeral=True)

        base_url = 'https://api.remove.bg/v1.0/removebg'
        headers = {'X-Api-Key': self.bg_key}
        data = {'image_url': img_url}
        r = requests.post(base_url, headers=headers, data=data)

        if r.status_code != (200 or 201):
            return await inter.response.send_message(f"Error: {r.status_code}")

        # save request as a png
        with open(f'bg_removed.png', 'wb') as f:
            f.write(r.content)
        
        # send image
        await inter.response.send_message(file=disnake.File(f'bg_removed.png'))

    

def setup(bot):
    bot.add_cog(GeneralPurpose(bot))