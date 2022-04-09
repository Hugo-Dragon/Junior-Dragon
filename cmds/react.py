import discord
from discord.ext import commands
from core.classes import Cog_Extension

import json
with open("config.json", mode="r", encoding="utf8") as jfile:
    conf = json.load(jfile)

import random, datetime, time, asyncio

class React(Cog_Extension):
    @commands.command()
    async def idk(self, ctx):
        idk = discord.File(conf["idkqwq"])
        await ctx.message.delete()
        await ctx.send(file= idk)

    @commands.command()
    async def thonk(self, ctx):
        random_thonk = random.choice(conf["thonk"])
        await ctx.message.delete()
        await ctx.send(random_thonk)


def setup(bot):
    bot.add_cog(React(bot))
