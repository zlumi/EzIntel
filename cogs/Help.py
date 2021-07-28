import discord
from discord.ext import commands
from discord.errors import Forbidden

class Help(commands.Cog):
    """
    Sends this help message
    """

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx, *input):
        """Shows all modules of that bot"""
        prefix = 'ez.'
        version =  1.0
        owner = 738359334349570150
        owner_name = "zClapr#0001"

        if not input:
            try:
                owner = ctx.guild.get_member(owner).mention
            except AttributeError as e:
                owner = owner
                
            emb = discord.Embed(title='Commands and modules', color=discord.Color.blue(),
                                description=f'Use `{prefix}help <module>` to gain more information about that module\n')

            for cog in self.bot.cogs:
                emb.add_field(name=(f"`{cog}`"), value=self.bot.cogs[cog].__doc__, inline=False)
            commands_desc = ''
            for command in self.bot.walk_commands():
                if not command.cog_name and not command.hidden:
                    commands_desc += f'{command.name} - {command.help}\n'
            if commands_desc:
                emb.add_field(name='Not belonging to a module', value=commands_desc, inline=False)

            emb.set_footer(text=f"""Developed by zClapr#0001\nRunning {version}""")

        elif len(input) == 1:
            for cog in self.bot.cogs:
                if cog.lower() == input[0].lower():
                    emb = discord.Embed(title=f'{cog} - Commands', description=self.bot.cogs[cog].__doc__,
                                        color=discord.Color.green())
                    for command in self.bot.get_cog(cog).get_commands():
                        if not command.hidden:
                            emb.add_field(name=f"`{prefix}{command.name}`", value=command.help, inline=False)
                    break
            else:
                emb = discord.Embed(title="Error",
                                    description=f"Module `{input[0]}` not found!",
                                    color=discord.Color.orange())
        elif len(input) > 1:
            emb = discord.Embed(title="Error",
                                description="Please request only one module at once.",
                                color=discord.Color.orange())
        else:
            pass
        
        await ctx.send(embed=emb)


def setup(bot):
    bot.add_cog(Help(bot))