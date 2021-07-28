from discord.ext import commands

async def emojiAdd(ctx, emoji: str):
    if type(ctx) == commands.context.Context:
        x = ctx.message
    else:
        x = ctx

    if emoji=='y':
        await x.add_reaction('✅')
    elif emoji=='n':
        await x.add_reaction('❎')
    elif emoji=='stop':
        await x.add_reaction('🛑')
    elif emoji=='start':
        await x.add_reaction('⏩')
    else:
        await x.add_reaction(emoji)