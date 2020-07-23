import discord
import discord.ext.commands as commands

import utilities.helplist as hl

def setup(bot):
    bot.remove_command('help')
    bot.add_cog(Help(bot))

class Help(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.title = '_All commands_'
        self.msg = ''

        for cog in hl.cogs:
            aliases = ''
            if len(cog) is 3:
                aliases += f' [{cog[2]}]'
            self.msg += f'- **_{cog[0]}_**{aliases} - {cog[1]}\n'
   
    @commands.command()
    async def help(self, ctx):
        embed = discord.Embed(
            title = self.title,
            description = self.msg,
            color=0xE91E63 #LUMINOUS_VIVID_PINK
        )
        embed.set_thumbnail(url="https://img.icons8.com/color/48/000000/python.png")
        embed.add_field(name="_Support_", value="If you have any issues with the bot, please go to our " + 
            "[Github Issues Page](https://github.com/WhaleyTech/OpenDiscord1/issues) and create a new issue")
        embed.add_field(name="_Add to Discord_", value="This bot can be added to your very own server! " +
        "[Click here to add it to yours]({})".format(discord.utils.oauth_url(self.bot.user.id)), inline=False)
        await ctx.send(embed=embed)
