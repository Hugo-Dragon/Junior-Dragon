import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json

with open("setting.json", mode="r", encoding="utf8") as jfile:
    jdata = json.load(jfile)

import random
import datetime
import asyncio

class React(Cog_Extension):
    @commands.command() #idk command
    async def idk(self, ctx):
        idk = discord.File(jdata["idkqwq"])
        await ctx.message.delete()
        await ctx.send(file= idk)

    @commands.command()
    async def thonk(self, ctx):
        random_thonk = random.choice(jdata["thonk"])
        await ctx.message.delete()
        await ctx.send(random_thonk)


def setup(bot):
    bot.add_cog(React(bot)) 
