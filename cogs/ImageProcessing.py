from PIL import Image, ImageFilter, ImageOps
from io import BytesIO
from disnake.ext import commands
import disnake
import validators
import requests


class ImageProcessing(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
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
    bot.add_cog(ImageProcessing(bot))