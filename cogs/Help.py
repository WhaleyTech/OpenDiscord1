import discord
import discord.ext.commands as commands

#Need to put in another python file or switch up to json
addme = ['addme', 'Shares a link that allows to join your own discord server']
coinflip = ['coinflip', 'Flips a coin!']

cogs = [addme, coinflip]
#----------

def setup(bot):
    bot.remove_command('help')
    bot.add_cog(Help(bot))

class Help(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.info_title = 'All commands'
        self.info_msg = '▫ **command** [alias1, alias2, ...] - description\n\n'

        for cog in cogs:
            aliases = ''
            if len(cog) is 3:
                aliases += f' [{cog[2]}]'
            self.info_msg += f'▫ **{cog[0]}**{aliases} - {cog[1]}\n'
   
    @commands.command()
    async def help(self, ctx):
        info_embed = discord.Embed(
            title = self.info_title,
            description = self.info_msg,
            color=0xE91E63 #LUMINOUS_VIVID_PINK
        )
        await ctx.send(embed=info_embed)