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
        self.title = self.bot.config["name"]
    
    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        general = find(lambda s: s.name == 'general', guild.text_channels)
        if general and general.permissions_for(guild.me).send_messages:
            embed = discord.Embed(title="{} - The USI Collaborative Discord Bot".format(self.title),
            description="Thanks for inviting me to your server! Use {}help for a list of commands.".format(self.bot.config["prefix"]),
            color=0xE91E63)
        await general.send(embed=embed)

    @commands.command(aliases=['addme'])
    async def invite(self, ctx):
        """Shares a link that allows the bot to join your own discord server"""
        await ctx.send(f"Use this link to invite {self.title} to your own discord server! {discord.utils.oauth_url(self.bot.user.id)}") #need oauth2 url

    @commands.command(aliases=['commit'])
    async def commits(self, ctx):
        """Shows the latest commit history pushed to github"""
        commit = subprocess.check_output(['git', 'log', '--pretty=format:[`%h`](https://github.com/WhaleyTech/OpenDiscord1/commits) %s', '-n', '3']).decode('utf-8')
        embed = discord.Embed(description='Check us out on [GitHub](https://github.com/WhaleyTech/OpenDiscord1)')
        embed.add_field(name='Latest Commit History', value = commit, inline=False)
        await ctx.send(embed=embed)

    @commands.command()
    async def info(self, ctx):
        """Get some info about the bot"""
        embed = discord.Embed(description="_{} - A USI collaborative Discord Bot._".format(self.title), color=0xE91E63)
        embed.set_thumbnail(url="https://img.icons8.com/color/48/000000/python.png")
        embed.set_author(name='Contributors | EvanBlaine WhaleyTech')
        embed.add_field(name='Version Used:', value='*_Python {}.{}_*'.format(sys.version_info.major, sys.version_info.minor), inline=True)
        embed.set_footer(text='Created with discord.py')
        await ctx.send(embed=embed)

    @commands.command()
    async def id(self, ctx, user:discord.User=None):
        """returns command author's ID or a user's ID if specified"""
        if user is None:
            await ctx.send("Your ID is `{}`".format(ctx.author.id))
        else:
            await ctx.send("{}'s ID is `{}`".format(user.mention, user.id))
