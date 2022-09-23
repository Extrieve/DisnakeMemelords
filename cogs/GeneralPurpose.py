from disnake.ext import commands, tasks
import disnake
import random
import json
import sys, os
import validators
import aiohttp
import art
from PIL import Image
from io import BytesIO
from pytube import YouTube

class GeneralPurpose(commands.Cog):

    time_interval = random.randint(5, 15)

    cwd = os.getcwd()
    sys.path.append(f'{cwd}..')
    from config import ame_token, bg_key
    from setup import ame_endpoints, speech_bubble, horoscope
    Templates = commands.option_enum(ame_endpoints)
    Horoscope = commands.option_enum(horoscope)
    movie_clips = json.load(open(f'db/movies_db.json', encoding='utf8'))
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\ AppleWebKit/537.36 (KHTML, like Gecko) \ Chrome/58.0.3029.110 Safari/537.36'}

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

    @commands.slash_command(name="phone-info", description="Get all information related to the phone nummber")
    async def phone_info(self, inter, phone_num: str, country_code: str = '1') -> None:
        # Getting rid of special chars
        phone_num = phone_num.replace('-', '').replace('(', '').replace(')', '').replace(' ', '').replace('+', '')
        phone_num = f'{country_code}{phone_num}'
        if not phone_num.isdigit():
            return await inter.response.send_message('Please provide a valid phone number', ephemeral=True)

        await inter.response.defer(with_message='Loading...', ephemeral=False)

        url = "https://phonevalidation.abstractapi.com/v1/?api_key=42253fea4b5645c9a45713308d620752&phone={phone}"

        async with aiohttp.ClientSession() as session:
            async with session.get(url.format(phone=phone_num)) as resp:
                if resp.status != 200:
                    return await inter.response.send_message('Something went wrong', ephemeral=True)
                data = await resp.json()

        title = f'Phone: {data["phone"]}'
        valid = f'Validity: {data["valid"]}'
        international_format = f'International Format: {data["format"]["international"]}'
        local_format = f'Local Format: {data["format"]["local"]}'
        country = f'Country: {data["location"]}'
        carrier = f'Carrier: {data["carrier"]}'
        num_type = f'Number Type: {data["type"]}'

        description = [valid, international_format, local_format, country, carrier, num_type]
        embed = disnake.Embed(title=title, description='\n'.join(description), color=0x00ff00)

        return await inter.followup.send(embed=embed)

    
    @commands.slash_command(name='text-ascii', description='Get ascii art!')
    async def text_ascii(self, inter, text: str, font: str = 'block') -> None: 
        if len(text) > 20:
            return await inter.response.send_message('Please provide a text with less than 20 characters', ephemeral=True)

        if not text:
            return await inter.response.send_message('Please provide a text', ephemeral=True)

        try:
            ascii_text = art.text2art(text, font=font)
            
            if len(ascii_text) > 2000:
                # convert to text file as BytesIO
                bytes_io = BytesIO()
                bytes_io.write(ascii_text.encode())
                bytes_io.seek(0)
                file = disnake.File(bytes_io, filename='ascii_txt.txt')
                return await inter.response.send_message('Your message surpassed Discord 2000 character limit so we converted it to txt :)\n' ,file=file)

            return await inter.response.send_message(f'```{ascii_text}```')

        except art.artError:
            font = 'default'
            ascii_text = art.text2art(text, font=font)
            
            if len(ascii_text) > 2000:
                # convert to text file as BytesIO
                bytes_io = BytesIO()
                bytes_io.write(ascii_text.encode())
                bytes_io.seek(0)
                file = disnake.File(bytes_io, filename='ascii_txt.txt')
                return await inter.response.send_message('Your message surpassed Discord 2000 character limit so we converted it to txt :)\n' ,file=file)

            return await inter.response.send_message('The font you provided is not valid, using default font\n{ascii_art}', ephemeral=True)


    @commands.slash_command(name='horoscope', description='Get your horoscope fortune for the day.')
    async def horoscope(self, inter, sign: Horoscope) -> None: 
        url = 'https://aztro.sameerkumar.website/'
        params = (
        ('sign', sign),
        ('day', 'today'),
        )

        async with aiohttp.ClientSession() as session:
            async with session.post(url, params=params) as resp:
                if resp.status != 200:
                    return await inter.response.send_message('Something went wrong', ephemeral=True)
                data = await resp.json()

        title = f'Horoscope for {sign.capitalize()} -> {data["current_date"]}'
        description = [f"Today's fortune: {data['description']}"]
        embed = disnake.Embed(title=title, description='\n'.join(description), color=0x00ff00)

        return await inter.response.send_message(embed=embed)


    @commands.slash_command(name='random-person', description='Randomly generate the face of a person')
    async def random_person(self, inter) -> None:
        url = 'https://thispersondoesnotexist.com/image'
        await inter.response.defer(with_message='Loading...', ephemeral=False)

        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                if resp.status != 200:
                    return await inter.followup.send('Something went wrong', ephemeral=True)
                data = await resp.read()

        image = BytesIO(data)
        image.seek(0)
        file = disnake.File(image, filename='random_person.png')

        return await inter.followup.send(file=file, ephemeral=False)

    
    @commands.slash_command(name='youtube-embed', description='Embed a youtube video')
    async def youtube_embed(self, inter, url: str) -> None: 
        yt = YouTube(url)
        await inter.response.defer(with_message='Loading...', ephemeral=False)

        stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').asc().first()

        if not stream:
            return await inter.followup.send('No mime type found for your video.', ephemeral=True)

        stream.download(filename='youtube.mp4', output_path='db/')

        try:
            video = disnake.File('db/youtube.mp4', filename='youtube.mp4')

            # embed = disnake.Embed(title=yt.title, description=yt.description, color=0x00ff00)
            # embed.set_image(url=yt.thumbnail_url)

            return await inter.followup.send(file=video, ephemeral=False)

        except Exception as e:
            return await inter.followup.send('The video is too large for Discord. We apologize for the inconvenience.', ephemeral=True)



    # @commands.slash_command(name='weather', description='Get the live weather of a city')
    # async def weather(self, inter, city: str) -> None:
    #     await inter.response.defer(with_message='Loading...', ephemeral=False)
    #     title = f'Weather in {city}'
    #     city = city.replace(' ', '+')
    #     url = f'https://www.google.com/search?q={city}\&oq={city}\&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=\chrome&ie=UTF-8'

    #     async with aiohttp.ClientSession() as session:
    #         async with session.get(url, headers=self.headers) as resp:
    #             if resp.status != 200:
    #                 return await inter.followup.send('Something went wrong', ephemeral=True)
    #             data = await resp.text()

    #     soup = BeautifulSoup(data, 'html.parser')
    #     location = soup.select('#wob_loc').getText().strip()
    #     time = soup.select('#wob_dts').getText().strip()
    #     temp = soup.select('#wob_tm').getText().strip()
    #     desc = soup.select('#wob_dc').getText().strip()
    #     humidity = soup.select('#wob_hm').getText().strip()
    #     description = [location, time, temp, desc, humidity]
    #     embed = disnake.Embed(title=title, description='\n'.join(description), color=0x00ff00)

    #     return await inter.followup.send(embed=embed)


    # @commands.slash_command(name='ascii-art', description='Produce ascii art from an image')
    # async def ascii_art(self, inter, image: disnake.Attachment) -> None:
    #     await inter.response.defer(with_message='Loading...', ephemeral=False)

    #     if not image:
    #         return await inter.followup.send('Please provide an image', ephemeral=True)

    #     # Store image in BytesIO
    #     image = BytesIO(await image.read())
    #     kit.image_to_ascii_art(image, 'ascii')
    #     return await inter.followup.send(file=disnake.File('ascii.txt'))


def setup(bot):
    bot.add_cog(GeneralPurpose(bot))