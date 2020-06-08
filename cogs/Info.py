import discord
import discord.ext.commands as commands


class Info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(aliases=['joinme', 'join', 'botinvite'])
    async def invite(self, ctx):
        await ctx.send("Use this URL to invite me to your own discord server! {}") #need oauth2 url

def setup(bot):
    bot.add_cog(Info(bot))