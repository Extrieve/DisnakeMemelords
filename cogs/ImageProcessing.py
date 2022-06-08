from PIL import Image, ImageFilter, ImageOps
from io import BytesIO
from disnake.ext import commands
import disnake
import validators
import aiohttp


class ImageProcessing(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.slash_command(name='greyscale', description='Convert an image to greyscale')
    async def greyscale(self, inter, img_url: str) -> None:
        if not validators.url(img_url):
            return await inter.response.send_message('Please provide a valid URL', ephemeral=True)

        async with aiohttp.ClientSession() as session:
            async with session.get(img_url) as resp:
                if resp.status != 200:
                    return await inter.response.send_message('Something went wrong', ephemeral=True)
                data = await resp.content.read()
        
        bytes_io = BytesIO()
        image = Image.open(BytesIO(data))
        image.convert('L').save(bytes_io, format='PNG')
        bytes_io.seek(0)
        dfile = disnake.File(bytes_io, filename='greyscale.png')
        return await inter.response.send_message(file=dfile)

    
    @commands.slash_command(name='reverse', description='Reverse an image')
    async def reverse(self, inter, img_url: str) -> None:
        if not validators.url(img_url):
            return await inter.response.send_message('Please provide a valid URL', ephemeral=True)

        async with aiohttp.ClientSession() as session:
            async with session.get(img_url) as resp:
                if resp.status != 200:
                    return await inter.response.send_message('Something went wrong', ephemeral=True)
                data = await resp.content.read()
        
        bytes_io = BytesIO()
        image = Image.open(BytesIO(data))
        image.transpose(Image.FLIP_LEFT_RIGHT).save(bytes_io, format='PNG')
        bytes_io.seek(0)
        dfile = disnake.File(bytes_io, filename='reverse.png')
        return await inter.response.send_message(file=dfile)

    
    @commands.slash_command(name='flip-img', description='Flip an image')
    async def flip(self, inter, img_url: str) -> None:
        if not validators.url(img_url):
            return await inter.response.send_message('Please provide a valid URL', ephemeral=True)

        async with aiohttp.ClientSession() as session:
            async with session.get(img_url) as resp:
                if resp.status != 200:
                    return await inter.response.send_message('Something went wrong', ephemeral=True)
                data = await resp.content.read()

        bytes_io = BytesIO()
        image = Image.open(BytesIO(data))
        image.transpose(Image.FLIP_TOP_BOTTOM).save(bytes_io, format='PNG')
        bytes_io.seek(0)
        dfile = disnake.File(bytes_io, filename='flip.png')
        return await inter.response.send_message(file=dfile)

    
    @commands.slash_command(name='rotate', description='Rotate an image')
    async def rotate(self, inter, img_url: str, angle: int) -> None:
        if not validators.url(img_url):
            return await inter.response.send_message('Please provide a valid URL', ephemeral=True)

        async with aiohttp.ClientSession() as session:
            async with session.get(img_url) as resp:
                if resp.status != 200:
                    return await inter.response.send_message('Something went wrong', ephemeral=True)
                data = await resp.content.read()

        bytes_io = BytesIO()
        image = Image.open(BytesIO(data))
        image.rotate(angle).save(bytes_io, format='PNG')
        bytes_io.seek(0)
        dfile = disnake.File(bytes_io, filename='rotate.png')
        return await inter.response.send_message(file=dfile)

    
    @commands.slash_command(name='blur', description='Blur an image')
    async def blur(self, inter, img_url: str) -> None:
        if not validators.url(img_url):
            return await inter.response.send_message('Please provide a valid URL', ephemeral=True)

        async with aiohttp.ClientSession() as session:
            async with session.get(img_url) as resp:
                if resp.status != 200:
                    return await inter.response.send_message('Something went wrong', ephemeral=True)
                data = await resp.content.read()
        
        bytes_io = BytesIO()
        image = Image.open(BytesIO(data))
        image.filter(ImageFilter.BLUR).save(bytes_io, format='PNG')
        bytes_io.seek(0)
        dfile = disnake.File(bytes_io, filename='blur.png')
        return await inter.response.send_message(file=dfile)


    @commands.slash_command(name='pixelate', description='Pixelate an image')
    async def pixelate(self, inter, img_url: str) -> None:
        if not validators.url(img_url):
            return await inter.response.send_message('Please provide a valid URL', ephemeral=True)

        async with aiohttp.ClientSession() as session:
            async with session.get(img_url) as resp:
                if resp.status != 200:
                    return await inter.response.send_message('Something went wrong', ephemeral=True)
                data = await resp.content.read()
        
        bytes_io = BytesIO()
        image = Image.open(BytesIO(data))
        image.filter(ImageFilter.SMOOTH).save(bytes_io, format='PNG')
        bytes_io.seek(0)
        dfile = disnake.File(bytes_io, filename='pixelate.png')
        return await inter.response.send_message(file=dfile)


    @commands.slash_command(name='invert', description='Invert an image')
    async def invert(self, inter, img_url: str) -> None:
        if not validators.url(img_url):
            return await inter.response.send_message('Please provide a valid URL', ephemeral=True)

        async with aiohttp.ClientSession() as session:
            async with session.get(img_url) as resp:
                if resp.status != 200:
                    return await inter.response.send_message('Something went wrong', ephemeral=True)
                data = await resp.content.read()
        
        bytes_io = BytesIO()
        image = Image.open(BytesIO(data))
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


    @commands.slash_command(name='blend', description='Blend an image')
    async def blend(self, inter, img_url: str, img_url2: str) -> None:

        await inter.response.defer(with_message='Loading...', ephemeral=False)

        if not validators.url(img_url):
            return await inter.followup.send('Please provide a valid URL', ephemeral=True)

        if not validators.url(img_url2):
            return await inter.followup.send('Please provide a valid URL', ephemeral=True)

        async with aiohttp.ClientSession() as session:
            async with session.get(img_url) as resp:
                if resp.status != 200:
                    return await inter.followup.send('Something went wrong', ephemeral=True)
                data = await resp.content.read()
        
        async with aiohttp.ClientSession() as session:
            async with session.get(img_url2) as resp:
                if resp.status != 200:
                    return await inter.followup.send('Something went wrong', ephemeral=True)
                data2 = await resp.content.read()

        bytes_io = BytesIO()
        image = Image.open(BytesIO(data))
        image2 = Image.open(BytesIO(data2))

        # If both images are not the same size, then return an error
        if image.size != image2.size:
            return await inter.followup.send('Images must be the same size', ephemeral=True)

        # Convert both images to RGB
        image = image.convert('RGBA')
        image2 = image2.convert('RGBA')

        blend = Image.blend(image, image2, alpha=0.5).save(bytes_io, format='PNG')
        bytes_io.seek(0)
        dfile = disnake.File(bytes_io, filename='blend.png')
        return await inter.followup.send(file=dfile)


    @commands.slash_command(name='resize', description='Resize an image based on percentage')
    async def resize(self, inter, img_url: str, percent: int) -> None:
        if not validators.url(img_url):
            return await inter.response.send_message('Please provide a valid URL', ephemeral=True)

        async with aiohttp.ClientSession() as session:
            async with session.get(img_url) as resp:
                if resp.status != 200:
                    return await inter.response.send_message('Something went wrong', ephemeral=True)
                data = await resp.content.read()

        bytes_io = BytesIO()
        image = Image.open(BytesIO(data))
        image.resize((int(image.size[0] * percent / 100), int(image.size[1] * percent / 100))).save(bytes_io, format='PNG')
        bytes_io.seek(0)
        dfile = disnake.File(bytes_io, filename='resize.png')
        return await inter.response.send_message(file=dfile)

    
    @commands.slash_command(name='green', description='Greenify an image')
    async def greenify(self, inter, img_url: str) -> None:
        # TODO: Finish the implementation
        pass

    
    @commands.slash_command(name='reddify', description='Reddify an image')
    async def reddify(self, inter, img_url: str) -> None:
        # TODO: Finish the implementation
        pass

    @commands.slash_command(name='blueify', description='Blueify an image')
    async def blueify(self, inter, img_url: str) -> None:
        # TODO: Finish the implementation
        pass


def setup(bot):
    bot.add_cog(ImageProcessing(bot))