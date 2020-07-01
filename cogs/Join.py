import discord
import discord.ext.commands as commands
from discord.utils import find


class Join(commands.Cog):
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

def setup(bot):
    bot.add_cog(Join(bot))
    