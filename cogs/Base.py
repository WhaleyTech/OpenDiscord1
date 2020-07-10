import discord
import subprocess
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
            description="Thanks for inviting me to your server! Use !help for a list of commands.",
            color=discord.Color.blurple())
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