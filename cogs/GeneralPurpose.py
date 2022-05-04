from PIL import Image, ImageFilter, ImageOps
from io import BytesIO
import disnake
from disnake.ext import commands
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
    Templates = commands.option_enum(ame_endpoints)
    movie_clips = json.load(open(f'db/movies_db.json', encoding='utf8'))

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


    @commands.slash_command(name='remove-background', description='Remove the background of an image')
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

    
    @commands.slash_command(name='movie-clip', description='Get a movie clip from the database')
    async def movie_clip(self, inter, movie: str):
        
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

    
    @commands.slash_command(name='greyscale', description='Convert an image to greyscale')
    async def greyscale(self, inter, img_url: str):
        if not validators.url(img_url):
            return await inter.response.send_message('Please provide a valid URL', ephemeral=True)

        r = requests.get(img_url, stream = True)
        bytes_io = BytesIO()
        image = Image.open(BytesIO(r.content))
        image.convert('L').save(bytes_io, format='PNG')
        bytes_io.seek(0)
        dfile = disnake.File(bytes_io, filename='greyscale.png')
        return await inter.response.send_message(file=dfile)

    
    @commands.slash_command(name='reverse', description='Reverse an image')
    async def reverse(self, inter, img_url: str):
        if not validators.url(img_url):
            return await inter.response.send_message('Please provide a valid URL', ephemeral=True)

        r = requests.get(img_url, stream = True)
        bytes_io = BytesIO()
        image = Image.open(BytesIO(r.content))
        image.transpose(Image.FLIP_LEFT_RIGHT).save(bytes_io, format='PNG')
        bytes_io.seek(0)
        dfile = disnake.File(bytes_io, filename='reverse.png')
        return await inter.response.send_message(file=dfile)

    
    @commands.slash_command(name='flip-img', description='Flip an image')
    async def flip(self, inter, img_url: str):
        if not validators.url(img_url):
            return await inter.response.send_message('Please provide a valid URL', ephemeral=True)

        r = requests.get(img_url, stream = True)
        bytes_io = BytesIO()
        image = Image.open(BytesIO(r.content))
        image.transpose(Image.FLIP_TOP_BOTTOM).save(bytes_io, format='PNG')
        bytes_io.seek(0)
        dfile = disnake.File(bytes_io, filename='flip.png')
        return await inter.response.send_message(file=dfile)

    
    @commands.slash_command(name='rotate', description='Rotate an image')
    async def rotate(self, inter, img_url: str, angle: int):
        if not validators.url(img_url):
            return await inter.response.send_message('Please provide a valid URL', ephemeral=True)

        r = requests.get(img_url, stream = True)
        bytes_io = BytesIO()
        image = Image.open(BytesIO(r.content))
        image.rotate(angle).save(bytes_io, format='PNG')
        bytes_io.seek(0)
        dfile = disnake.File(bytes_io, filename='rotate.png')
        return await inter.response.send_message(file=dfile)

    
    @commands.slash_command(name='blur', description='Blur an image')
    async def blur(self, inter, img_url: str):
        if not validators.url(img_url):
            return await inter.response.send_message('Please provide a valid URL', ephemeral=True)

        r = requests.get(img_url, stream = True)
        bytes_io = BytesIO()
        image = Image.open(BytesIO(r.content))
        image.filter(ImageFilter.BLUR).save(bytes_io, format='PNG')
        bytes_io.seek(0)
        dfile = disnake.File(bytes_io, filename='blur.png')
        return await inter.response.send_message(file=dfile)


    @commands.slash_command(name='pixelate', description='Pixelate an image')
    async def pixelate(self, inter, img_url: str, size: int):
        if not validators.url(img_url):
            return await inter.response.send_message('Please provide a valid URL', ephemeral=True)

        r = requests.get(img_url, stream = True)
        bytes_io = BytesIO()
        image = Image.open(BytesIO(r.content))
        image.filter(ImageFilter.SMOOTH).save(bytes_io, format='PNG')
        bytes_io.seek(0)
        dfile = disnake.File(bytes_io, filename='pixelate.png')
        return await inter.response.send_message(file=dfile)


    @commands.slash_command(name='invert', description='Invert an image')
    async def invert(self, inter, img_url: str):
        if not validators.url(img_url):
            return await inter.response.send_message('Please provide a valid URL', ephemeral=True)

        r = requests.get(img_url, stream = True)
        bytes_io = BytesIO()
        image = Image.open(BytesIO(r.content))
        # convert to RGB
        image = image.convert('RGB')
        # invert colors
        r, g, b = image.split()
        r = ImageOps.invert(r)
        g = ImageOps.invert(g)
        b = ImageOps.invert(b)
        # merge
        image = Image.merge('RGB', (r, g, b))
        image.save(bytes_io, format='PNG')
        bytes_io.seek(0)
        dfile = disnake.File(bytes_io, filename='invert.png')
        return await inter.response.send_message(file=dfile)


def setup(bot):
    bot.add_cog(GeneralPurpose(bot))