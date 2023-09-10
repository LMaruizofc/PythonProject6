import discord
from discord.ext import commands

class events(commands.Cog):

    def __init__(self, bot: commands.Bot):

        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):

        print('Eu entrei como {0}'.format(self.bot.user))

def setup(bot: commands.Bot) -> None:

    bot.add_cog(events(bot))