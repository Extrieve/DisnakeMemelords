from disnake.ext import commands


class Listener(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):

        if message.author == self.bot.user:
            return
        
        if 'jueves' in message.content.lower():
            await message.reply('https://cdn.discordapp.com/attachments/862790378925850624/1170728291745927339/Hoy_no_es_jueves_mamaguevo_HOY_ES_VIERNES_-_HD.mp4?ex=655a18af&is=6547a3af&hm=7bd185a6ad76eb570e9fc38f6f051790b25d5dee72bb1eda07ca8cdaae4ff1b5&')
            return
        
        if 'twxtter.com' in message.content or 'fxtwitter.com' in message.content or 'vxtwitter.com' in message.content:
            return
        
        if 'twitter.com' in message.content:    
            author = message.author
            new_embbed = message.content.replace('twitter', 'fxtwitter')
            await message.reply(f'New Tweet from: {author.mention}\nEmbbeding to twxtter\n{new_embbed}', mention_author=True)
            await message.delete()

def setup(bot):
    bot.add_cog(Listener(bot))