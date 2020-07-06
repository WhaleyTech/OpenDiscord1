import random
import discord
import time

import discord.ext.commands as commands

""" random cool bot commands :) """
class Cool(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def coinflip(self, ctx):
        coin = ['Tails', 'Heads']
        await ctx.send(f"You flipped a coin! **{random.choice(coin)}**")

    @commands.command()
    async def roll(self, ctx):
        dice_min=1
        dice_max=6
        await ctx.send(f':game_die: You roll a die! **{random.randint(dice_min, dice_max)}**')     


def setup(bot):
    bot.add_cog(Cool(bot))