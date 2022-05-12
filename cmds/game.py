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
        await ctx.send("Please guess a number from 1~100, you have 10 chances")

        for i in range(0,10):
            guess = await self.bot.wait_for("message", check=check)
    
            if int(guess.content) > number:
                await ctx.send("Too little")
            elif int(guess.content) < number:
                await ctx.send("Too Large")
            elif int(guess.content) == number:
                await ctx.send("You finally finish this stupid game!!")
            else:
                await ctx.send("Please guess the number FROM 1 TO 100")
        else:
            await ctx.send("Haha, you did NOT guess the correct number.")
            await ctx.send(f"The Correct Number is:{number} ")



def setup(bot):
    bot.add_cog(Game(bot))