from disnake.ext import commands
import disnake
import setup
import asyncio
import os

class Bot(commands.Bot):
    def __init__(self, **kwargs):
        super().__init__(
            command_prefix=commands.when_mentioned_or('!'),
            description='Third and final refactor',
            test_guilds=[193188992857014272],
            intents=disnake.Intents.all(),
            sync_commands_debug=True,
        )
        os.environ['DISPLAY'] = ':0' # fix for pywhatkit
        os.environ['XAUTHORITY']='/run/user/1000/gdm/Xauthority' # fix for pywhatkit
        for cog in setup.cogs:
            try:
                self.load_extension(cog)
            except Exception as e:
                print(f'Failed to load cog {cog}\n{e}')

    async def on_ready(self):
        print(f'Logged on as {self.user} (ID: {self.user.id})')


async def main():
    bot = Bot()
    await bot.start(os.environ['token'])

if __name__ == '__main__':
    asyncio.run(main())