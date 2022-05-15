from disnake.ext import commands
from enum import Enum
import disnake
import requests
import json
import asyncio
import os, sys
import csv
import urllib.parse
import validators
import random

class Anime(commands.Cog):

    working_dir = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(f'{working_dir}..')
    from setup import categories

    Categories = commands.option_enum(categories)
    themes_data = json.load(open(f'{working_dir}/../db/themes3.json', encoding='utf8'))

    with open(f'{working_dir}/../db/registered_ids2.csv', 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        registered_ids = [int(row[0]) for row in list(reader)[1:]]

    def __init__(self, bot):
        self.bot = bot

    ### Non-command functions ###
    def get_anime_data(self, anime_name: str) -> list:
        """
        Returns the data of the anime with the given name.
        """
        if len(anime_name) < 4:
            raise commands.BadArgument('The anime name must be at least 4 characters long.')

        url = 'https://api.jikan.moe/v4/anime'
        params = {'q' : anime_name}

        request = requests.get(url, params=params)
        if request.status_code != 200:
            raise commands.BadArgument('Anime not found.')
        
        data = request.json()
        names, anime_ids = [], []
        for anime in data['data']:
            names.append(anime['title'])
            anime_ids.append(anime['mal_id'])
        
        return list(zip(anime_ids, names))

    
    def get_anime_vid(self, anime_id: int) -> dict:
        """
        Returns the video of the anime with the given id.
        """
        openings, endings = [], []

        for item in self.themes_data:
            if item['anime_id'] == anime_id:
                current = item['mirrors'][0]['mirror']
                openings.append(current) if 'OP' in current else endings.append(current)
        
        return {'openings': openings, 'endings': endings}

    
    def anilist_query(self, anime_id: int) -> dict:
        
        query = '''
        query ($id: Int) { # Define which variables will be used in the query (id)
        Media (id: $id, type: ANIME) { # Insert our variables into the query arguments (id) (type: ANIME is hard-coded in the query)
            id
            title {
            romaji
            english
            native
            }
        }
        }
        '''

        # Define our query variables and values that will be used in the query request
        variables = {
            'id': int(anime_id)
        }

        url = 'https://graphql.anilist.co'

        # Make the HTTP Api request
        response = requests.post(url, json={'query': query, 'variables': variables})

        if response.status_code != 200:
            raise Exception('Query failed to run by returning code of {}. {}'.format(response.status_code, response.text))

        data = response.json()
        output = {}
        output['title_rom'] = data['data']['Media']['title']['romaji']
        output['title_eng'] = data['data']['Media']['title']['english']

        return output


    @commands.slash_command(name='anime-quote', description='Get a an anime quote.')
    async def anime_quote(self, inter, *, anime_name: str=None, character_name: str=None) -> None:
        """
        Get a quote from an anime.
        """
        if anime_name:
            await inter.response.defer(with_message='Loading...', ephemeral=False)

            url = 'https://animechan.vercel.app/api/quotes/anime?title='
            r = requests.get(url + anime_name)

            if r.status_code != 200:
                return await inter.followup.send('Anime not found.', ephemeral=True)

            data = json.loads(r.text)
            index = 0
            length = len(data)

            anime_name = data[index]['anime']
            character_name = data[index]['character']
            quote = data[index]['quote']

            embed = disnake.Embed(title=anime_name, description=quote, color=0x00FF00)
            embed.set_author(name=character_name)

            try:
            # get character img from image search
                char_url = 'https://imsea.herokuapp.com/api/1?q='
                params = {'q' : f'{character_name} {anime_name}'}
                char_r = requests.get(char_url, params=params)
                if char_r.status_code == 200:
                    char_data = json.loads(char_r.text)
                    char_img = char_data['results'][0]
            except:
                char_img = None

            if char_img:
                embed.set_thumbnail(url=char_img)

            await inter.followup.send(embed=embed)
            msg = await inter.original_message()

            # add reaction to msg
            await msg.add_reaction('◀️')
            await msg.add_reaction('▶️')

            def check(reaction, user):
                return user == inter.author and str(reaction.emoji) in ['◀️', '▶️']

            while True:
                try:
                    reaction, user = await self.bot.wait_for('reaction_add', timeout=60.0, check=check)
                except asyncio.TimeoutError:
                    return await inter.followup.send('Request timed out.', ephemeral=True)
                else:
                    if str(reaction.emoji) == '◀️':
                        index -= 1
                        if index < 0:
                            index = length - 1
                    elif str(reaction.emoji) == '▶️':
                        index += 1
                        if index >= length:
                            index = 0

                    anime_name = data[index]['anime']
                    character_name = data[index]['character']
                    quote = data[index]['quote']

                    embed = disnake.Embed(title=anime_name, description=quote, color=0x00FF00)
                    embed.set_author(name=character_name)
                    embed.set_thumbnail(url=char_img)
                    await msg.edit(embed=embed)

                    await msg.remove_reaction(reaction.emoji, user)
            
        elif character_name:
            return await inter.response.send_message('Coming soon!', ephemeral=True)

        url = 'https://animechan.vercel.app/api/random'
        r = requests.get(url)

        if r.status_code!= 200:
            return await inter.response.send_message('An error occurred while getting a quote.', ephemeral=True)

        data = json.loads(r.text)
        anime_name = data['anime']
        character_name = data['character']
        quote = data['quote']
        embed = disnake.Embed(title=f'Anime: {anime_name}\nCharacter: {character_name}', description=quote, color=0x00ff00)
        
        try:
            # get character img from image search
            char_url = 'https://imsea.herokuapp.com/api/1?q='
            params = {'q' : f'{character_name} {anime_name}'}
            char_r = requests.get(char_url, params=params)
            if char_r.status_code == 200:
                char_data = json.loads(char_r.text)
                char_img = char_data['results'][0]
        except:
            char_img = None

        if char_img:
            embed.set_thumbnail(url=char_img)

        return await inter.response.send_message(embed=embed)


    @commands.slash_command(name='anime-picture', description='Get an anime image/gif')
    async def ani_pic(self, inter, category: Categories = None) -> None:
        if category is None:
            # choose a random category
            category = random.choice(list(self.Categories))
        
        url = 'https://api.waifu.pics/sfw/'
        print(category)
        r = requests.get(f'{url}{category}').text
        picture = json.loads(r)['url']
        await inter.response.send_message(picture)
        

    @commands.slash_command(name='anime-search', description='Get information and details about an anime')
    async def ani_search(self, inter, query: str) -> None:
        
        if len(str(query)) < 4:
            return await inter.response.send_message('Search result should be at least 4 characters', ephemeral=True)

        url = 'https://api.jikan.moe/v4/anime'
        params = {'q' : query}

        request = requests.get(url, params=params, verify=False)

        if request.status_code != 200:
            return await inter.response.send_message('Anime not found.')

        data = request.json()
        results = []

        for i, entry in enumerate(data['data']):
            results.append(f'{i+1}. {entry["title"]}')

        embed = disnake.Embed(title='Anime Search', description='\n'.join(results), color=0x00ff00)
        embed.set_footer(text='Type the number of the anime you want to get info on.')
        await inter.response.send_message(embed=embed, ephemeral=True)

        def check(m):
            return m.author == inter.author

        try:
            msg = await self.bot.wait_for('message', check=check, timeout=60)
        except asyncio.TimeoutError:
            return await inter.followup.send('Timed out.')

        try:
            choice = int(msg.content) - 1
        except ValueError:
            return await inter.followup.send('Invalid number.')
        
        if choice < 0 or choice >= len(data['data']):
            return await inter.followup.send('Invalid number.')
        
        response = []
        try:
            response.append(f'**{data["data"][choice]["title"]}**')
            response.append(f'**Score:** {data["data"][choice]["score"]}')
            response.append(f'**Rating:** {data["data"][choice]["rating"]}')
            response.append(f'**Episodes:** {data["data"][choice]["episodes"]}')
            response.append(f'**Popularity:** {data["data"][choice]["popularity"]}')
            response.append(f'**Studios:** {data["data"][choice]["studios"][0]["name"]}')
            response.append(f'**Synopsis:** {data["data"][choice]["synopsis"]}')
            response.append(f'**Posters:** {data["data"][choice]["images"]["jpg"]["large_image_url"]}')
        except (KeyError, IndexError, ValueError) as e:
            print(e)
            response = []
            response.append(f'**{data["data"][choice]["title"]}**')
            response.append(f'**Score:** {data["data"][choice]["score"]}')
            response.append(f'**Rating:** {data["data"][choice]["rating"]}')
            response.append(f'**Popularity:** {data["data"][choice]["popularity"]}')
            response.append(
                f'**Synopsis:** {data["data"][choice]["synopsis"]}')
            response.append(
                f'**Posters:** {data["data"][choice]["images"]["jpg"]["large_image_url"]}')

        embed = disnake.Embed(title='Anime Search', description='\n'.join(response), color=0x00ff00)
        embed.set_thumbnail(url=data["data"][choice]["images"]["jpg"]["large_image_url"])

        return await inter.followup.send(embed=embed)


    @commands.slash_command(name='manga-search', description='Get information and details about an manga.')
    async def manga_search(self, inter, query: str) -> None:
        
        if len(query) < 4:
            return await inter.response.send_message('Search result should be at least 4 characters', ephemeral=True)

        url = 'https://api.jikan.moe/v4/manga/'
        params = {'q' : query, 'page' : 1}

        request = requests.get(url, params=params, verify=False)

        if request.status_code != (200 or 204):
            return await inter.response.send_message('Manga not found.')
        
        data = json.loads(request.text)
        results = []
        for i, entry in enumerate(data['data']):
            results.append(f'{i+1}. {entry["title"]}')

        embed = disnake.Embed(title='Manga Search', description='\n'.join(results), color=0x00ff00)
        embed.set_footer(text='Type the number of the manga you want to get info on.')
        await inter.response.send_message(embed=embed)

        # Get user selection
        def check(m):
            return m.author == inter.author
        
        try:
            choice = await self.bot.wait_for('message', check=check, timeout=20.0)
        except asyncio.TimeoutError:
            return await inter.followup.send('You took too long to respond.')
            
        try:
            choice = int(choice.content) - 1
        except ValueError:
            return await inter.followup.send('Please enter a valid number.')
        
        if choice < 0 or choice >= len(data['data']):
            return await inter.followup.send('Please enter a valid number.')
        
        response = []
        try:
            title = data['data'][choice]['title']
            image = data['data'][choice]['images']['jpg']['large_image_url']
            response.append(f'**Chapters**: {data["data"][choice]["chapters"]}')
            response.append(f'**Volumes**: {data["data"][choice]["volumes"]}')
            response.append(f'**Score**: {data["data"][choice]["score"]}')
            response.append(f'**Synopsis**: {data["data"][choice]["synopsis"]}')
        except (KeyError, IndexError, ValueError) as e:
            print(e)
            return await inter.followup.send('Manga not found.')

        embed = disnake.Embed(title=title, description='\n'.join(response), color=0x00ff00)
        embed.set_thumbnail(url=image)
        return await inter.followup.send(embed=embed)


    @commands.slash_command(name='anime-theme', description='Get anime opening/ending video')
    async def anime_theme(self, inter, query: str) -> None:
        
        if len(query) < 4:
            return await inter.response.send_message('Search result should be at least 4 characters', ephemeral=True)

        search = self.get_anime_data(query)
        if not search:
            return await inter.response.send_message(f'No results for {query}', ephemeral=True)

        available = []
        for entry in search:
            if entry[0] in self.registered_ids:
                available.append(entry)

        if not available:
            return await inter.response.send_message('Anime not found.')

        options = [f'{i+1}) {item[1]}' for i, item in enumerate(available)]
        embed = disnake.Embed(title='Anime Search', description='\n'.join(options), color=0x00ff00)
        embed.set_footer(text='Type the number of the anime you want to get info on.')
        await inter.response.send_message(embed=embed, ephemeral=True)

        # Get user selection
        def check(m):
            return m.author == inter.author and m.content.isdigit()
        
        try:
            choice = await self.bot.wait_for('message', check=check, timeout=30.0)
        except asyncio.TimeoutError:
            return await inter.followup.send('You took too long to respond.', ephemeral=True)

        try:
            choice = int(choice.content) - 1
        except ValueError:
            return await inter.followup.send('Please enter a valid number.', ephemeral=True)

        if choice < 0 or choice >= len(available):
            return await inter.followup.send('Please enter a valid number.', ephemeral=True)

        all = self.get_anime_vid(available[choice][0])
        ops = all['openings']
        eds = all['endings']

        if ops and not eds:
            await inter.followup.send(f'This title contains {len(ops)} opening(s). Enter the number of the video you want to watch.',
             ephemeral=True)

            try:
                choice = await self.bot.wait_for('message', timeout=60, check=lambda m: m.author == inter.author and m.content.isdigit())
            except asyncio.TimeoutError:
                return await inter.followup.send('You took too long to respond.', ephemeral=True)
            
            choice = int(choice.content) - 1
            if choice < 0 or choice >= len(ops):
                return await inter.followup.send('Invalid choice.', ephemeral=True)
            
            return await inter.followup.send(f'Opening #{choice + 1}):\n{ops[choice]}')

        elif eds and not ops:
            await inter.followup.send(f'This title contains {len(eds)} ending(s). Enter the number of the video you want to watch.', ephemeral=True)

            try:
                choice = await self.bot.wait_for('message', timeout=60, check=lambda m: m.author == inter.author and m.content.isdigit())
            except asyncio.TimeoutError:
                return await inter.followup.send('You took too long to respond.', ephemeral=True)
            
            choice = int(choice.content) - 1
            if choice < 0 or choice >= len(eds):
                return await inter.followup.send('Invalid choice.', ephemeral=True)
            
            return await inter.followup.send(f'Ending #{choice + 1}:\n{eds[choice]}')

        else:
            msg = await inter.followup.send(f'This title contains {len(ops)} opening(s) and {len(eds)} ending(s).\nDo you want to select an opening 😎 or an ending 🥰?')

            # add reactions to message
            await msg.add_reaction('😎')
            await msg.add_reaction('🥰')

            def check(reaction, user):
                return user == inter.author and str(reaction.emoji) in ['🥰', '😎']
            try:
            
                reaction, user = await self.bot.wait_for('reaction_add', timeout=60, check=check)
            except asyncio.TimeoutError:
                return await inter.followup.send('You took too long to respond.', ephemeral=True)
            
            if str(reaction.emoji) == '😎':
                await inter.followup.send(f'This title has {len(ops)} opening(s). Enter the number of the video you want to watch.'
                , ephemeral=True)
                try:
                    choice = await self.bot.wait_for('message', timeout=60, check=lambda m: m.author == inter.author and m.content.isdigit())
                except asyncio.TimeoutError:
                    return await inter.followup.send('You took too long to respond.', ephemeral=True)
                
                choice = int(choice.content) - 1
                if choice < 0 or choice >= len(ops):
                    return await inter.followup.send('Invalid choice.')
                
                return await inter.followup.send(f'Opening #{choice + 1}):\n{ops[choice]}')
            
            else:
                await inter.followup.send(f'This title has {len(eds)} ending(s). Enter the number of the video you want to watch.'
                , ephemeral=True)

                try:
                    choice = await self.bot.wait_for('message', timeout=60, check=lambda m: m.author == inter.author and m.content.isdigit())
                except asyncio.TimeoutError:
                    return await inter.followup.send('You took too long to respond.', ephemeral=True)
                
                choice = int(choice.content) - 1
                if choice < 0 or choice >= len(eds):
                    return await inter.followup.send('Invalid choice.', ephemeral=True)
                
                return await inter.followup.send(f'Ending #{choice+1}:\n{eds[choice]}')
    

    @commands.slash_command(name='anime-scene')
    async def anime_scene(self, inter, scene_url: str) -> None:
        """
        Automatically detect anime scene
        Parameters
        ----------
        scene_url: URL of an anime scene, the url has to be the endpoint to an image file
        """

        if not validators.url(scene_url):
            return await inter.response.send_message('Invalid URL.')

        parse_url = urllib.parse.quote_plus(scene_url)
        response = requests.get(f"https://api.trace.moe/search?url={parse_url}").json()
        
        if response['error']:
            return await inter.response.send_message('Could not find anime.')
        
        results = response['result']

        anime_id = results[0]['anilist']
        titles = self.anilist_query(anime_id)

        output = []
        title_rom = titles['title_rom']
        output.append(f"**English Title**: {titles['title_eng']}")
        output.append(f"**Filename**: {results[0]['filename']}")
        output.append(f"**Episode**: {results[0]['episode']}")
        output.append(f"Similarity: {round(results[0]['similarity'], 2)}")

        embed = disnake.Embed(title=title_rom, description='\n'.join(output), color=0x00ff00)
        embed.set_image(url=scene_url)
        return await inter.response.send_message(embed=embed)

        
def setup(bot):
    bot.add_cog(Anime(bot))