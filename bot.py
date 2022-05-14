from disnake.ext import commands
from disnake import Intents
import config
import setup
import asyncio

class Bot(commands.Bot):
    def __init__(self, **kwargs):
        super().__init__(
            command_prefix=commands.when_mentioned_or('!'),
            description='Third and final refactor',
            test_guilds=[953357475254505592],
            sync_commands_debug=True,
            intents=Intents.all(),
        )
        
        for cog in setup.cogs:
            try:
                self.load_extension(cog)
            except Exception as e:
                print(f'Failed to load cog {cog}\n{e}')

    async def on_ready(self):
        print(f'Logged on as {self.user} (ID: {self.user.id})')


async def main() -> None:
    # intents = Intents.default()
    # intents.members = True
    # intents.presences = True
    # intents.messages = True
    bot = Bot()
    await bot.start(config.token)

if __name__ == '__main__':
    asyncio.run(main())