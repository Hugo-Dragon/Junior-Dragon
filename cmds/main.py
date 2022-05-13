from click import command
import discord
from discord.ext import commands
from core.classes import Cog_Extension
import random

import json
with open("config.json", mode="r", encoding="utf8") as jfile:
    conf = json.load(jfile)

import random, datetime, time, asyncio, pytz

class Main(Cog_Extension):
    @commands.command() 
    async def ping(self, ctx):
        await ctx.send(f"🇵 🇴 🇳 🇬❗| Now's Ping:{round(self.bot.latency*1000)} (ms)")

    @commands.command()
    async def botabout(self, ctx):
        twtz = pytz.timezone("Asia/Taipei")
        timestamp= time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        embed=discord.Embed(title="About the bot", description="PY_Attano#9288"  ,color=0x00b1ff)
        embed.set_author(name="恐龍#2549", icon_url="https://imgur.com/yh0Gerr")
        embed.set_thumbnail(url="https://i.imgur.com/369RMge.png")
        embed.add_field(name="Made by", value="恐龍#2549", inline=True)
        embed.add_field(name="Made with", value="Python3.8", inline=True)
        embed.set_footer(text=timestamp)
        await ctx.send(embed=embed)
    @commands.command()
    async def say(self, ctx,  *,msg):
        await ctx.message.delete()
        await ctx.send(msg)
    @commands.command()
    async def echo(self, ctx,  *,msg):
        await ctx.message.delete()
        await ctx.send(msg)
    @commands.command()
    async def repeat(self, ctx, *,msg):
        await ctx.send(msg)

    @commands.command()
    async def clean(self, ctx, num: int):
        await ctx.channel.purge(limit=num+1)
        OK = await ctx.send("The message has been cleaned^__^")
        await asyncio.sleep(3)
        await OK.delete()
    @commands.command()
    async def dev(self, ctx):
        twtz = pytz.timezone("Asia/Taipei")
        timestamp= time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        embed=discord.Embed(title="The dev", description="The dev", color=0xffbb00)
        embed.add_field(name="Programming", value="恐龍#2549", inline=True)
        embed.add_field(name="Bot's Manage", value="恐龍#2549", inline=True)
        embed.add_field(name="P.S.", value="It's all by 恐龍#2549 xd", inline=True)
        embed.set_footer(text=timestamp)
        await ctx.send(embed=embed)
    @commands.command()
    async def botinfo(self, ctx):
        embed=discord.Embed(title="Bot Info", description="This bot is make by 恐龍#2549\nthis command is make by KL AE#2160\nLanguage: 🐍 Python\nVersion: 3.8 PY & 1.7.3 D.PY", color=random.randrange(0, 16777216)) # random color
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Main(bot))
