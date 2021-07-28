from discord.ext import commands
from PyUtils import *
from discord import user
from discord import channel

class Moderation(commands.Cog):
    """
    Manual moderation
    """

    @commands.command(name='purge', help='purge the past ... messages', pass_context=True, case_insensitive=True, aliases=['delete'])
    @commands.has_permissions(administrator=True)
    async def clean(self, ctx, number:str, userName:str=None, channel:str=None):
        await ctx.message.delete()

        if userName == None:
            try:
                await ctx.channel.purge(limit=int(number))
            except:
                if number=='all':
                    await ctx.channel.purge(limit=len(await ctx.channel.history().flatten()))
                else:
                    emojiAdd('f')
"""else:   #USE CARFULLY! MAY OVERLOAD BOT
            if channel==None:
                for x in range(0, int(number)):
                    await ctx.channel.history().get(author__name=userName).message.delete()
            elif channel=='all':
                for chan in ctx.guild.channels:
                    for x in range(0, int(number)):
                        #await chan.history().get(author__name=userName).message.delete() """

def setup(bot):
    bot.add_cog(Moderation(bot))