import discord, os
from discord.ext import commands
from config import configData

client = commands.Bot(
    command_prefix = configData['prefix'],
    help_command = None,
    case_insensitive = True,
    intents = discord.Intents.all()
)

for filename in os.listdir('./commands'):

    if filename.endswith('.py'):

        client.load_extension('commands.{0}'.format(filename[:-3]))

for filename in os.listdir('./events'):

    if filename.endswith('.py'):

        client.load_extension('events.{0}'.format(filename[:-3]))

client.run(configData['token'])