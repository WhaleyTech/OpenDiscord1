import discord
import discord.ext.commands as commands

def setup(bot):
    bot.add_cog(Mod(bot))

class Mod(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, user: discord.Member, *, reason="reason null"):
        if ctx.author.id == user.id:
            self_kick_embed = discord.Embed(
                description='Kicking yourself is not permitted',
                color=0xE91E63
            )
            await ctx.send(embed=self_kick_embed)
        if ctx.author.top_role.id == user.top_role.id and ctx.author.id != ctx.guild.owner.id:
            no_perms_embed = discord.Embed(
                description='You are not permitted to use this command.',
                color=0xE91E63
            )  
            await ctx.send(embed=no_perms_embed)
        await ctx.guild.kick(user, reason=reason)
        success_embed = discord.Embed(
            description=f'**{user}** has successfully been kicked.',
            color=0xE91E63
        )
        await ctx.send(embed=success_embed)

    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(manage_messages=True)
    async def purge(self, ctx, n: int):
        if n < 999:
            try:
                await ctx.channel.purge(limit=n+1)
            except Exception:
                err_embed = discord.Embed(
                    description='An error occured while deleting messages.',
                    color=0xE91E63
                )
                await ctx.send(embed=err_embed)
        else:
            lim_embed = discord.Embed(
                description='''The limit for deleting messages with this command is 999;
                            please try again!''',
                color=0xE91E63
            )
            await ctx.send(embed=lim_embed)
