from disnake.ext import commands, tasks
import disnake
import random
import json
import sys, os
import validators
import aiohttp
from PIL import Image
from io import BytesIO

class GeneralPurpose(commands.Cog):

    time_interval = random.randint(5, 15)

    cwd = os.getcwd()
    sys.path.append(f'{cwd}..')
    from config import ame_token, bg_key
    from setup import ame_endpoints
    from setup import speech_bubble
    Templates = commands.option_enum(ame_endpoints)
    movie_clips = json.load(open(f'db/movies_db.json', encoding='utf8'))

    def __init__(self, bot):
        self.bot = bot
        # self.test1.start()

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

        async with aiohttp.ClientSession() as session:
            async with session.post(base_url, json=params, headers=headers) as resp:
                if resp.status != 200:
                    return await inter.response.send_message('Something went wrong', ephemeral=True)
                data = await resp.json()
                print(data)
                res = 'https://gotiny.cc/' + data[0]['code']
                await inter.response.send_message(res)


    @commands.slash_command(name='meme-generator' ,description='Generate a meme with the available templates')
    async def meme_generator(self, inter, img_url: str, template: Templates) -> None:

        await inter.response.defer(with_message='Loading...', ephemeral=False)
        
        if not validators.url(img_url):
            return await inter.response.send_message('Please provide a valid URL', ephemeral=True)
        
        base_url = "https://v1.api.amethyste.moe"
        headers = {'Authorization': f'Bearer {self.ame_token}'}
        data = {'url': img_url}

        async with aiohttp.ClientSession() as session:
            final_url = f'{base_url}/generate/{template}'
            async with session.post(final_url, data=data, headers=headers) as resp:
                if resp.status != 200:
                    return await inter.response.send_message('Something went wrong', ephemeral=True)
                data = await resp.content.read()

        bytes_io = BytesIO()
        image = Image.open(BytesIO(data))
        image.save(bytes_io, format='PNG')
        bytes_io.seek(0)
        dfile = disnake.File(bytes_io, filename=f'{template}.png')
        return await inter.followup.send(file=dfile)


    @commands.slash_command(description='Decode a QR code by providing a ')
    async def qr(self, inter, qr_url: str) -> None: 

        await inter.response.defer(with_message='Loading...', ephemeral=False)
        
        if not validators.url(qr_url):
            return await inter.followup.send('Please provide a valid URL', ephemeral=True)

        url = 'http://api.qrserver.com/v1/read-qr-code/?fileurl='
        async with aiohttp.ClientSession() as session:
            async with session.get(f'{url}{qr_url}') as resp:
                if resp.status != 200:
                    return await inter.response.send_message('Something went wrong', ephemeral=True)
                data = await resp.json()

        return await inter.followup.send(data[0]['symbol'][0]['data'])


    @commands.slash_command(name='remove-background', description='Remove the background of an image')
    async def remove_background(self, inter, img_url: str) -> None:
        if not validators.url(img_url):
            return await inter.response.send_message('Please provide a valid URL', ephemeral=True)

        await inter.response.defer(with_message='Loading...', ephemeral=False)
        base_url = 'https://api.remove.bg/v1.0/removebg'
        headers = {'X-Api-Key': self.bg_key}
        data = {'image_url': img_url}

        async with aiohttp.ClientSession() as session:
            async with session.post(base_url, data=data, headers=headers) as resp:
                if resp.status != 200:
                    return await inter.response.send_message('Something went wrong', ephemeral=True)
                data = await resp.content.read()

        bytes_io = BytesIO()
        image = Image.open(BytesIO(data))
        image.save(bytes_io, format='PNG')
        bytes_io.seek(0)
        
        # send image
        await inter.followup.send(file=disnake.File(bytes_io, filename='bg_removed.png'))


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
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                if resp.status != 200:
                    return await inter.response.send_message('Something went wrong', ephemeral=True)
                data = await resp.json()

        title = data['data']['author']
        quote = data['data']['quote']
        embed = disnake.Embed(title=title, description=quote, color=0x00ff00)
        return await inter.followup.send(embed=embed)


    @tasks.loop(seconds=time_interval)
    async def test1(self) -> None:
        print('Waiting...')
        await self.bot.wait_until_ready()
        # send a message to the channel id = 953357475254505595
        rand_gid = random.choice(self.speech_bubble)
        self.time_interval = random.randint(5, 15)
        print(f'Time interval: {self.time_interval}')
        await self.bot.get_channel(953357475254505595).send(rand_gid)
        

    @commands.slash_command(name='channel-id', description='Get the channel ID')
    async def channel_id(self, inter) -> None:
        await inter.response.send_message(inter.channel.id)


def setup(bot):
    bot.add_cog(GeneralPurpose(bot))