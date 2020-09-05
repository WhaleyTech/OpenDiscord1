import discord
import discord.ext.commands as commands

import utilities.helplist as hl

def setup(bot):
    bot.remove_command('help')
    bot.add_cog(Help(bot))

def c_(n: list, msg: str):
        aliases = ''
        for i in n:
            if len(i) is 3:
                aliases += f' [{i[2]}]'
            msg += f'- **_{i[0]}_**{aliases} - {i[1]}\n'
        return msg

class Help(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.title = f'_{self.bot.config["name"]} Commands_'
        self.msg = ''

    @commands.command()
    async def help(self, ctx):
        embed = discord.Embed(
            title = self.title,
            description = "Use **{0}help1 | {0}help2 | {0}help3** for a list of commands!".format(self.bot.config["prefix"]),
            color = 0xE91E63, #LUMINOUS_VIVID_PINK
        )
        embed.set_thumbnail(url="https://img.icons8.com/color/48/000000/python.png")
        embed.add_field(name="_Support_", value="If you have any issues with the bot, please go to our " + 
            "[Github Issues Page](https://github.com/WhaleyTech/OpenDiscord1/issues) and create a new issue")
        await ctx.send(embed=embed)

    @commands.command()
    async def help1(self, ctx):
        """info commands"""
        info_embed = discord.Embed(
            title = "_Help1 - Info Commands_",
            description = c_(n=hl.info_cmds, msg=self.msg),
            color = 0xE91E63,
        )
        info_embed.set_footer(text="{0}help2 - Admin Commands | {0}help3 - Random Commands".format(self.bot.config["prefix"]))
        await ctx.send(embed=info_embed)

    @commands.command()
    async def help2(self, ctx):
        """admin commands"""
        admin_embed = discord.Embed(
            title = "_Help2 - Admin Commands_",
            description = c_(n=hl.admin_cmds, msg=self.msg),
            color = 0xE91E63,
        )
        admin_embed.set_footer(text="{0}help3 - Random Commands".format(self.bot.config["prefix"]))
        await ctx.send(embed=admin_embed)
    
    @commands.command()
    async def help3(self, ctx):
        """random commands"""
        rand_embed = discord.Embed(
            title = "_Help3 - Random Commands_",
            description = c_(n=hl.rand_cmds, msg=self.msg),
            color = 0xE91E63,
        )
        rand_embed.set_footer(text="End of Help!")
        await ctx.send(embed=rand_embed)
