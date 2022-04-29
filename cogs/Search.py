from disnake.ext import commands
import disnake
import sys, os
import requests
import json
import asyncio
from serpapi import GoogleSearch

class Search(commands.Cog):
    # Get current working directory and add it to the path
    cwd = os.getcwd()
    sys.path.append(f'{cwd}..')
    from config import serp_key

    def __init__(self, bot):
        self.bot = bot


    def getDefinition(self, word):
        response = requests.get(
            f'https://api.dictionaryapi.dev/api/v2/entries/en/{word}')
        processedResponse = json.loads(response.text)
        return processedResponse[0]['meanings'][0]['definitions']


    @commands.slash_command(name='define', description='Get the definition of a word')
    async def define(self, inter, word):

        try:
            definition = self.getDefinition(word)
        except KeyError:
            return await inter.response.send_message(f'No definition found for {word}')

        # Embed the definition
        index = 0
        embed = disnake.Embed(title=f'{word.capitalize()}', color=0x00ff00)
        embed.add_field(name='Definition', value=definition[index]['definition'])
        embed.set_footer(text=f'Definition {index + 1} of {len(definition)}')
        await inter.response.send_message(embed=embed)
        msg = await inter.original_message()
        
        # add left and right emoji to the message
        await msg.add_reaction('◀️')
        await msg.add_reaction('▶️')

        # Wait for a reaction
        def check(reaction, user):
            return user == inter.author and str(reaction.emoji) in ['◀️', '▶️'] and reaction.message.id == msg.id
        
        while True:
            try:
                reaction, user = await self.bot.wait_for('reaction_add', timeout=30.0, check=check)
            except asyncio.TimeoutError:
                return await inter.followup.send('Timed out.')

            if str(reaction.emoji) == '◀️':
                index -= 1
                if index < 0:
                    index = len(definition) - 1
            elif str(reaction.emoji) == '▶️':
                index += 1
                if index >= len(definition):
                    index = 0

            embed.clear_fields()
            embed.add_field(name='Definition', value=definition[index]['definition'])
            embed.set_footer(text=f'Definition {index + 1} of {len(definition)}')
            await msg.edit(embed=embed)

            await msg.remove_reaction(reaction.emoji, user)


    @commands.slash_command(name='image-search', description='Search for an image')
    async def image_search(self, inter, query):

        await inter.response.defer(with_message='Searching...', ephemeral=False)

        params = {
            'q': query,
            'tbm': 'isch',
            'ijn': '0',
            'api_key': self.serp_key
        }
        search = GoogleSearch(params)
        results = search.get_dict()
        length = len(results['images_results'])

        if not results:
            return await inter.followup.send(f'No results found for {search}.', ephemeral=True)
    
        # Display the first image but allow the user to traverse the rest
        embed = disnake.Embed(title=f'{results["images_results"][0]["title"]}', url=results['images_results'][0]['original'], color=0x00ff00)
        embed.set_image(url=results['images_results'][0]['original'])
        await inter.followup.send(embed=embed)
        msg = await inter.original_message()
        # Allow the user to traverse the rest of the images
        await msg.add_reaction('◀️')
        await msg.add_reaction('▶️')

        def check(reaction, user):
            return user == inter.author and str(reaction.emoji) in ['◀️', '▶️']
        
        index = 0
        while True:
            try:
                reaction, user = await self.bot.wait_for('reaction_add', timeout=60.0, check=check)
            except asyncio.TimeoutError:
                return await inter.followup.send('Request timed out.')
            else:
                if str(reaction.emoji) == '◀️':
                    index -= 1
                    if index < 0:
                        index = length - 1
                elif str(reaction.emoji) == '▶️':
                    index += 1
                    if index >= length:
                        index = 0
                embed = disnake.Embed(title=f'{results["images_results"][index]["title"]}', url=results['images_results'][index]['original'], color=0x00ff00)
                embed.set_image(url=results['images_results'][index]['original'])
                await msg.edit(embed=embed)
                await msg.remove_reaction(reaction.emoji, user)

    
    @commands.slash_command(name='yugioh', description='Search for a card')
    async def yugi(self, inter, search):
        """
        Search for a card on Yugioh Wiki.
        """

        url = 'https://db.ygoprodeck.com/api/v7/cardinfo.php'
        params = {
            'name': search
        }
        response = requests.get(url, params=params)

        if response.status_code != 200:
            return await inter.response.send_message('No results found.', ephemeral=True)

        data = json.loads(response.text)
        
        images = []
        for i in range(len(data['data'][0]['card_images'])):
            images.append(data['data'][0]['card_images'][i]['image_url'])

        embed = disnake.Embed(title=f'{data["data"][0]["name"]}', color=0x00ff00)
        embed.set_image(url=images[0])
        embed.add_field(name='Card Type', value=data['data'][0]['type'])
        embed.add_field(name='Card Description', value=data['data'][0]['desc'])
        embed.add_field(name='Card ATK', value=data['data'][0]['atk'])
        embed.add_field(name='Card DEF', value=data['data'][0]['def'])
        embed.add_field(name='Card Level', value=data['data'][0]['level'])
        
        await inter.response.send_message(embed=embed)
        message = await inter.original_message()

        # Add reactions to the message
        await message.add_reaction('◀️')
        await message.add_reaction('▶️')

        # Wait for a reaction
        def check(reaction, user):
            return user == inter.author and str(reaction.emoji) in ['◀️', '▶️'] and reaction.message.id == message.id
        
        index = 0
        while True:
            try:
                reaction, user = await self.bot.wait_for('reaction_add', timeout=30.0, check=check)
            except asyncio.TimeoutError:
                return await inter.followup.send('Timed out.')

            if str(reaction.emoji) == '◀️':
                index -= 1
                if index < 0:
                    index = len(images) - 1
            elif str(reaction.emoji) == '▶️':
                index += 1
                if index >= len(images):
                    index = 0

            embed.clear_fields()
            embed.set_image(url=images[index])
            embed.add_field(name='Card Type', value=data['data'][0]['type'])
            embed.add_field(name='Card Description', value=data['data'][0]['desc'])
            embed.add_field(name='Card ATK', value=data['data'][0]['atk'])
            embed.add_field(name='Card DEF', value=data['data'][0]['def'])
            embed.add_field(name='Card Level', value=data['data'][0]['level'])
            await message.edit(embed=embed)

            await message.remove_reaction(reaction.emoji, user)
        

def setup(bot):
    bot.add_cog(Search(bot))