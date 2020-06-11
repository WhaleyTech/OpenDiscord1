import discord
import discord.ext.commands as commands


class Info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(aliases=['addme'])
    async def invite(self, ctx):
        await ctx.send(f"Use this link to invite me to your own discord server! {discord.utils.oauth_url(self.bot.user.id)}") #need oauth2 url

def setup(bot):
    bot.add_cog(Info(bot))
   