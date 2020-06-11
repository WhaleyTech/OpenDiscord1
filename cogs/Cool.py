import random
import discord

import discord.ext.commands as commands

""" random cool bot commands :) """
class Cool(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def coinflip(self, ctx):
        coin = ['Tails', 'Heads']
        await ctx.send(f"You flipped a coin! **{random.choice(coin)}**")
        

def setup(bot):
    bot.add_cog(Cool(bot))