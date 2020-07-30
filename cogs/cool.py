import random
import discord
import time
import requests
import utilities.lists as cl
import discord.ext.commands as commands

""" random cool bot commands :) """
class Cool(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def markdown(self, ctx):
        desc = (
            "**Markdown Text** is a nice feature within discord! "
            "Discord supports simple text formatting that helps "
            "make a sentence be easily noticed."
        )
        markdown_link = (
            'https://support.discordapp.com/hc/en-us/'
            'articles/210298617-Markdown-Text-101-Chat-Formatting-Bold-Italic-Underline-'
        )
        embed = discord.Embed(title='Markdown',
                                description=desc,
                                url=markdown_link,
                                color=0xE91E63)
        embed.set_thumbnail(url="https://img.icons8.com/color/48/000000/markdown.png")
        await ctx.send(embed=embed)

    @commands.command()
    async def leetcode(self, ctx):
        await ctx.send(requests.get('https://leetcode.com/problems/random-one-question/all').url)

    @commands.command()
    async def coinflip(self, ctx):
        coin = ['Tails', 'Heads']
        await ctx.send(f"You flipped a coin! **{random.choice(coin)}**")

    @commands.command()
    async def codeblock(self, ctx, *, msg:str):
        """makes user text into a 'fix' style codeblock"""
        await ctx.send("```fix\n" + msg + "\n```")

    @commands.command()
    async def mock(self, ctx, *, msg:str):
        """YoU CaN't JuSt PuT tHiS mEmE oN eVeRyThInG"""
        message=""
        for i in msg:
            message += random.choice([i.upper(), i.lower()])
        await ctx.send(message)

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