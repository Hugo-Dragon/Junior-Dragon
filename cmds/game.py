from distutils.command.config import config
import discord
from discord.ext import commands
from core.classes import Cog_Extension

import json, asyncio, time, datetime, pytz, random

with open("config.json", mode="r", encoding="utf8") as config:
    conf = json.load(config)
    
class Game(Cog_Extension):
    @commands.command()
    async def gn(self, ctx):
        def check(m):
            return m.author == ctx.author and m.channel == ctx.message.channel 
        number = random.randint(1,101) # Fixed Error (must add 1 to largest int)
        sus = str(number)
        await ctx.send("Please guess a number from 1~100, you have 10 chances")

        nowchance = 0
        newline = '\n'
        for i in range(0, 10):
            guess = await self.bot.wait_for("message", check=check)
            nowchance = nowchance+1
            if int(guess.content) > number:
                await ctx.send(f"Uhh... The number is too little, try a bit more bigger{newline}Chances left: `{str(nowchance)}`")
            elif int(guess.content) < number:
                await ctx.send(f"Uhh... The number is too large, try a bit fewer {newline}Chances left: `{str(nowchance)}`")
            elif int(guess.content) == number:
                await ctx.send(f":tada: You finished this game!!! The number is {sus}! Congrats!")
            else:
                await ctx.send(f"Please guess the number between 1 and 100{newline}Chances left: `{str(nowchance)}`")
        else:
            await ctx.send("Uhhh... You failed this game :sweat:")
            await ctx.send(f"The Correct Number is: {sus}")



def setup(bot):
    bot.add_cog(Game(bot))