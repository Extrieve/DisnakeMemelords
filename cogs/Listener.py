from disnake.ext import commands

class Listener(commands.Cog):
    # If someone says "hello" in a channel, the bot will reply with "hi"
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return
        
        if 'twitter.com' in message.content:
            author = message.author
            new_embbed = message.content.replace('twitter', 'twxtter')
            await message.reply(f'New Tweet from: {author.mention}\nEmbbeding to twxtter\n{new_embbed}', mention_author=True)
            await message.delete()

def setup(bot):
    bot.add_cog(Listener(bot))