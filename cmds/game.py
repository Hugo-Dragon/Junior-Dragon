import discord
from discord.ext import commands
from core.classes import Cog_Extension

import asyncio, time, datetime, pytz, random
from random import randint

import json
with open("config.json", mode="r", encoding="utf8") as jfile:
    conf = json.load(jfile)
    
class Game(Cog_Extension):
    @commands.command()
    async def gn(self, ctx):
        def check(m):
            return m.author == ctx.author and m.channel == ctx.message.channel
        number = random.randint(1,100)
        await ctx.send("請從1~100之間猜一個數字，一共有10次機會")

        for i in range(0,10):
            guess = await self.bot.wait_for("message", check=check)
    
            if int(guess.content) > number:
                await ctx.send("太大了..")
            elif int(guess.content) < number:
                await ctx.send("太小了..")
            elif int(guess.content) == number:
                await ctx.send("你終於完成這個愚蠢的遊戲了")
            else:
                await ctx.send("請猜1~100之間的整數，不要給我亂來")
        else:
            await ctx.send("笑死，這都猜不中，有夠雖，可憐awa")
            await ctx.send(f"正確答案是:{number} ")



def setup(bot):
    bot.add_cog(Game(bot))