import disnake
from disnake.ext import commands, tasks
from numpy import random
import requests
import json
import sys, os
import validators

class GeneralPurpose(commands.Cog):

    cwd = os.getcwd()
    sys.path.append(f'{cwd}..')
    ame_token = os.environ['ame_token']
    bg_key = os.environ['bg_key']
    from setup import ame_endpoints
    from setup import speech_bubble
    Templates = commands.option_enum(ame_endpoints)
    movie_clips = json.load(open(f'db/movies_db.json', encoding='utf8'))

    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name='avatar', description='Get the avatar of a user.')
    async def avatar(self, inter, *, user: disnake.Member = None) -> None:
        """Get the avatar of a user."""
        if user is None:
            user = inter.author
        await inter.send(user.avatar.url)
        
    
    @commands.slash_command(name='shorten-url', description='Shorten any URL')
    async def shorten(self, inter, url: str) -> None:
        
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
    async def meme_generator(self, inter, img_url: str, template: Templates) -> None:
        
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
    async def qr(self, inter, qr_url: str) -> None: 
        
        if not validators.url(qr_url):
            return await inter.response.send_message('Please provide a valid URL', ephemeral=True)

        url = 'http://api.qrserver.com/v1/read-qr-code/?fileurl='
        r = requests.get(url + qr_url)

        if r.status_code != (200 or 204):
            return await inter.response.send_message(f'Error: {r.status_code}')

        data = r.json()
        return await inter.response.send_message(data[0]['symbol'][0]['data'])


    @commands.slash_command(name='remove-background', description='Remove the background of an image')
    async def remove_background(self, inter, img_url: str) -> None:
        if not validators.url(img_url):
            return await inter.response.send_message('Please provide a valid URL', ephemeral=True)

        await inter.response.defer(with_message='Loading...', ephemeral=False)
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
        await inter.followup.send(file=disnake.File(f'bg_removed.png'))


    @commands.slash_command(name='movie-clip', description='Get a movie clip from the database')
    async def movie_clip(self, inter, movie: str) -> None:
        
        movie = movie.lower()
        flag = False
        for entry in self.movie_clips:
            if movie in entry.lower():
                movie = entry
                flag = True
                break
        
        if not flag:
            return await inter.response.send_message('No movie clip found', ephemeral=True)

        # get a random clip from the movie
        clip = random.choice(self.movie_clips[movie])
        return await inter.response.send_message(clip)


    @commands.slash_command(name='stoic', description='Get a stoic quote')
    async def stoic(self, inter) -> None:

        await inter.response.defer(with_message='Loading...', ephemeral=False)

        url = 'https://api.themotivate365.com/stoic-quote'
        r = requests.get(url)

        if r.status_code != 200:
            return await inter.followup.send('Something went wrong', ephemeral=True)

        data = r.json()
        title = data['data']['author']
        quote = data['data']['quote']
        embed = disnake.Embed(title=title, description=quote, color=0x00ff00)
        return await inter.followup.send(embed=embed)


    @tasks.loop(seconds=5)
    async def test1(self) -> None:
        print('Waiting...')
        await self.bot.wait_until_ready()
        # send a message to the channel id = 953357475254505595
        rand_gid = random.choice(self.speech_bubble)
        await self.bot.get_channel(953357475254505595).send(rand_gid)
        

    @commands.slash_command(name='channel-id', description='Get the channel ID')
    async def channel_id(self, inter) -> None:
        await inter.response.send_message(inter.channel.id, ephemeral=True)


def setup(bot):
    bot.add_cog(GeneralPurpose(bot))