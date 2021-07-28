from discord.ext import commands
from PyUtils import *
import re
from discord import utils
from discord import Embed
from EzIntel import *

async def localParse(ctx, content):
    webhook = utils.get(await ctx.channel.webhooks(), name='webhook')
    if webhook is None:
        webhook = await ctx.channel.create_webhook(name='webhook')

    finalMsg = str(content)
    strEmojis = []
    parsedEmojis = []

    draftMatches = re.findall(":\w+:", finalMsg)
    matches = []

    for stringEmoji in re.findall('<:\w+:\d{18}>', content):
        if stringEmoji not in strEmojis:
            strEmojis.append(stringEmoji)
    for stringEmoji in strEmojis:
        x = stringEmoji.removeprefix('<')
        x = x[:len(x) - 19]
        parsedEmojis.append(x)
    for item in draftMatches:
        if item not in matches:
            matches.append(item)

    if matches:
        for match in matches:
            emoji = utils.get(ctx.guild.emojis, name=f'{match}'.removeprefix(':').removesuffix(':'))
            if emoji != None:
                finalMsg = finalMsg.replace(match, str(emoji))
    if strEmojis:
        for x in strEmojis:
            finalMsg.replace(x, parsedEmojis[strEmojis.index(x)])
    
    if type(ctx) == commands.context.Context:
        await webhook.send(content=finalMsg, username=ctx.message.author.display_name, avatar_url=ctx.message.author.avatar_url)
        await ctx.message.delete()
    else:
        await webhook.send(content=finalMsg, username=ctx.author.display_name, avatar_url=ctx.author.avatar_url)
        await ctx.delete()

class NitroParse(commands.Cog):
    """
    Parse your messages to send nitro emojis
    """

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='parse', aliases=['p', 'par', 'pa'], case_insensitive=True, help='send as bot, with extra functions')
    async def parse(self, ctx, *, content):
        await localParse(ctx, content)
        

    @commands.command(name='parseenable', help='parse, but toggled', aliases=['parsetoggle', 'toggleparse', 'enableparse', 'tparse'], case_insensitive=True)
    async def toggleparse(self, ctx):
        stopcmds=['stop', 'leave', 'stopparse', 'leaveparse']
        await emojiAdd(ctx, 'start')
        no1T = 'Toggling Auto Parse Mode'
        no1D = f'User: <@{ctx.author.id}> \nTo exit, use `{str(stopcmds)}` \n\n`Session:` Active'
        no1 = await ctx.send(embed = Embed(title=no1T, 
        description=no1D))

        try:
            while True:
                msg = await self.bot.wait_for('message', check=lambda message: message.author == ctx.author, timeout=60)
                stop = False

                for stopCmd in stopcmds: 
                    if stopCmd in msg.content[:len(stopCmd)]:
                        await emojiAdd(msg, 'stop')
                        stop = True
                if stop:
                    await no1.edit(embed=Embed(title=no1T, 
                    description=no1D.replace('`Session:` Active', 
                    f'`Session Ended:` ended by user with [{msg.content}]({msg.jump_url})')))
                    break
                
                await localParse(msg, msg.content)
        except Exception as e:
            await no1.edit(embed=Embed(title=no1T, 
            description=no1D.replace('`Session:` Active', 
            f'Session Ended: \n\nSession Ended: `{e}`')))

def setup(bot):
    bot.add_cog(NitroParse(bot))