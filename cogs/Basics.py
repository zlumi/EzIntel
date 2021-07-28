from discord.ext import commands
import json
import sys
from discord import Embed
from PyUtils import *
import os
import re

config = json.load(open('config.json'))

class Basics(commands.Cog):
    """
    Botty stuff this bot can do
    """

    @commands.command(name='restart', aliases=['rs'], help='restart bot', case_insensitive=True)
    async def restart(self, ctx):
        if ctx.message.author.id in config['escalatedPermissions']:
            await emojiAdd(ctx, 'y')
            python = sys.executable
            os.execl(python, python, * sys.argv)
    """ @bot.command(name='help', help='ambulance incoming hold on')
    async def help(ctx):
        embedMsg = discord.Embed(title='Help', description=f'`ez.help` <module> for a more detailed view') """

    @commands.command(name='calculate', aliases=['calc', 'c'], case_insensitive=True, help='the calculator')
    async def calculate(self, ctx, *, input):
        allowed='0123456789+-*/().'
        try:
            if re.match("[0123456789+\-*\/().^]", input):
                if '^' in input:
                    input = input.replace('^', '**')
                if 'sqrt' in input:
                    input = input.replace('sqrt', '**')
                em = Embed(title=input, description=str(eval(input)))
                await ctx.send(embed=em)
            else:
                raise()
        except Exception as e:
            em = Embed(title='Error!', description=str(e))
            em.add_field(name='Add', value='+', inline=True)
            em.add_field(name='Subtract', value='-', inline=True)
            em.add_field(name='Divide', value='/', inline=True)
            em.add_field(name='Multiply', value='*', inline=True)
            em.add_field(name='To the Power of', value='** OR ^', inline=True)
            em.add_field(name='To the Root of', value='`n`Root(`x`) = `x`^(1/`n`)', inline=True)
            em.add_field(name='Your inputs', value='`x`, `n`')
            await ctx.send(embed=em)

def setup(bot):
    bot.add_cog(Basics(bot))