from disnake.ext import commands

class Listener(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):

        if message.author == self.bot.user:
            return
        
        if 'twxtter.com' in message.content or 'fxtwitter.com' in message.content or 'vxtwitter.com' in message.content:
            return
        
        if 'twitter.com' in message.content:    
            author = message.author
            new_embbed = message.content.replace('twitter', 'twxtter')
            await message.reply(f'New Tweet from: {author.mention}\nEmbbeding to twxtter\n{new_embbed}', mention_author=True)
            await message.delete()

def setup(bot):
    bot.add_cog(Listener(bot))