from discord.ext import commands
from discord import Embed
from PyUtils import *
import requests
from urllib import parse as par

botId = 847902326626844702

class AiChats(commands.Cog):
    """
    Chat with me
    """

    def __init__(self, bot):
            self.bot = bot

    @commands.command(name='chat', aliases=['startchat', 'schat', 'sc', 'talk'], case_insensitive=True, help='you lonely?')
    async def chat(self, ctx):

        await ctx.reply('Session Started')

        """async with cleverbotfree.async_playwright() as p_w:
            c_b = await cleverbotfree.CleverbotAsync(p_w)
            while True:
                uMsg = await self.bot.wait_for('message', check=lambda message: message.author == ctx.author, timeout=60)
                userMsg = uMsg.content
                async with ctx.typing():
                    if userMsg == 'bye' or userMsg == 'quit':
                        await no1.edit(embed=discord.Embed(title=no1T, 
                        description = no1D.replace('`Session:` Active', 
                        f'`Session Ended:` ended by user with [{userMsg.content}]({userMsg.jump_url})')))
                        break
                    resp = await c_b.single_exchange(userMsg)
                await ctx.send(resp)
            await c_b.close() """

        while True:
            uMsg = None

            try:
                uMsg = await self.bot.wait_for('message', check=lambda message: message.author == ctx.author, timeout=60)
            except Exception as e:
                await ctx.reply("Session finished: " + str(e))

            userMsg = uMsg.content
            returnedAns = None
            
            if uMsg != None:
                async with ctx.typing():
                    encodeContent = par.urlencode({"message": userMsg, "botname": await self.bot.fetch_user(botId), "ownername": await self.bot.fetch_user(738359334349570150), "user": uMsg.author})
                    returnedAns = str(requests.get(f'https://api.affiliateplus.xyz/api/chatbot?' + encodeContent).text)
                if userMsg == 'bye' or userMsg == 'quit':
                    await ctx.reply("Session ended by user")
                    break
                await uMsg.reply(returnedAns.removeprefix('{"message":"').removesuffix('"}'), mention_author=False)

def setup(bot):
    bot.add_cog(AiChats(bot))