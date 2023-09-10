import discord
from discord.ext import commands
from discord import slash_command
from config import configData
from classes.buttons import *

class whitelist(commands.Cog):

    def __init__(self, bot:commands.Bot):

        self.bot = bot

    @slash_command(name = 'whitelist',description = 'Começa a whitelist do servidor')
    async def wl(self, ctx: discord.Interaction):

        if discord.utils.get(ctx.guild.roles, id = configData['cargos']['cidadao']) in ctx.user.roles:

            await ctx.response.send_message('Você já fez a WL {0}'.format(ctx.user.name), ephemeral = True)

            return

        member = ctx.user

        overwrites = {

            ctx.guild.default_role: discord.PermissionOverwrite(read_messages=False),

            member: discord.PermissionOverwrite(read_messages=True),

        }

        channel = await ctx.guild.create_text_channel(name= f'wl-{ctx.user.name}', 
        overwrites = overwrites, 
        category = discord.utils.get(ctx.guild.categories, id = configData['categorias']['wl']))

        await channel.send(view = wl0(ctx.user,self.bot))

        await ctx.response.send_message('Whitelist iniciada, clique a baixo para ir pro canal',
        view = discord.ui.View(jumpto(f'https://discordapp.com/channels/{ctx.guild.id}/{channel.id}'),
        timeout = 180),
        ephemeral = True)

    @slash_command(name = 'mensagem_wl', description = 'Envia a mensagem de WL')
    @commands.has_guild_permissions(administrator = True)
    async def msgwl(self, ctx: discord.Interaction):

        msg = discord.Embed(
            title = '🔔 WHITELIST',
            description='''
Você pode fazer nossa Whitelist a qualquer momento e quantas
vezes quiser, o resultado será enviado no seu DM assim que sua WHITELIST for revisada.

```❗ ATENÇÃO```
para realizar sua Whitelist use o comando /whitelist
''')

        msg.set_image(url = 'https://media.giphy.com/media/sKezAGnlMZmLnwXwP8/giphy.gif')

        await ctx.response.send_message(embed = msg)

def setup(bot:commands.Bot):

    bot.add_cog(whitelist(bot))