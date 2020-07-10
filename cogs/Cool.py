import random
import discord
import time
import utilities.CoolList as cl
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
    async def rolldice(self, ctx):
        await ctx.send(f':game_die: You roll a die! **{random.randint(1, 6)}**')     

    @commands.command()
    async def lowercase(self, ctx, *, message:str):
        await ctx.send(message.lower())

    @commands.command()
    async def uppercase(self, ctx, *, message:str):
        await ctx.send(message.upper())

    @commands.command()
    async def reverse(self, ctx, *, message:str):
        await ctx.send(message[::-1])

    @commands.command(aliases=["8ball", "eightball", "8", "ball"])
    async def eight_ball(self, ctx):
        await ctx.send("{} **{}**".format(random.choice(cl.eight_ball), ctx.author.name))


def setup(bot):
    bot.add_cog(Cool(bot))