from disnake.ext import commands
from disnake.ui import Button
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
    async def define(self, inter, *, word):
        if not word:
            return await inter.response.send_message('Please provide a word')

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
        


def setup(bot):
    bot.add_cog(Search(bot))