import random

from disnake.ext import commands


class Listener(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    response_map = {
        'days': {
            3: ['https://video.twimg.com/ext_tw_video/1715039056256716800/pu/vid/avc1/1070x602/IwQ51Avy_Bdt0krY.mp4?tag=12'],
            4: ['https://cdn.discordapp.com/attachments/862790378925850624/1170728291745927339/Hoy_no_es_jueves_mamaguevo_HOY_ES_VIERNES_-_HD.mp4?ex=655a18af&is=6547a3af&hm=7bd185a6ad76eb570e9fc38f6f051790b25d5dee72bb1eda07ca8cdaae4ff1b5&']
        }
    }

    @commands.Cog.listener()
    async def on_message(self, message):

        if message.author == self.bot.user:
            return
        
        if 'jueves' in message.content.lower():
            created_at = message.created_at
            day_content = self.response_map['days'][created_at.weekday()]
            # if day_content choice is a list, choose a random element
            if isinstance(day_content, list):
                day_content = random.choice(day_content)
            
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