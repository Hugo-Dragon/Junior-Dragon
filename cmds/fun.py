import discord
from discord.ext import commands
from core.classes import Cog_Extension

import asyncio, time, datetime, pytz, random

import json
with open("config.json", mode="r", encoding="utf8") as jfile:
    conf = json.load(jfile)
    
class Game(Cog_Extension):
    @commands.command()
    async def nitro(self, ctx):
        embed=discord.Embed(title='Nitro', description='[Click Here lol 😆](https://youtube.com/watch?v=u6NOTogsw8M)', color=0x00ff00)
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Game(bot))