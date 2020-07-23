import discord
import subprocess
import sys
import discord.ext.commands as commands
from discord.utils import find

def setup(bot):
    bot.add_cog(Base(bot))

class Base(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        general = find(lambda s: s.name == 'general', guild.text_channels)
        if general and general.permissions_for(guild.me).send_messages:
            embed = discord.Embed(title="OpenDiscord1 - The USI Collaborative Discord Bot",
            description="Thanks for inviting me to your server! Use {}help for a list of commands.".format(self.bot.config["prefix"]),
            color=0xE91E63)
        await general.send(embed=embed)

    @commands.command(aliases=['addme'])
    async def invite(self, ctx):
        await ctx.send(f"Use this link to invite me to your own discord server! {discord.utils.oauth_url(self.bot.user.id)}") #need oauth2 url

    @commands.command(aliases=['commit'])
    async def commits(self, ctx):
        """return latest commits"""
        commit = subprocess.check_output(['git', 'log', '--pretty=format:[`%h`](https://github.com/WhaleyTech/OpenDiscord1/commits) %s', '-n', '3']).decode('utf-8')
        embed = discord.Embed(description='Check us out on GitHub (https://github.com/WhaleyTech/OpenDiscord1)')
        embed.add_field(name='Commit History', value = commit, inline=False)
        await ctx.send(embed=embed)

    @commands.command()
    async def info(self, ctx):
        embed = discord.Embed(description="_A USI collaborative Discord Bot._", color=0xE91E63)
        embed.set_thumbnail(url="https://img.icons8.com/color/48/000000/python.png")
        embed.set_author(name='Contributors | EvanBlaine WhaleyTech')
        embed.add_field(name='Version Used:', value='*_Python {}.{}_*'.format(sys.version_info.major, sys.version_info.minor), inline=True)
        embed.set_footer(text='Created with discord.py')
        await ctx.send(embed=embed)
