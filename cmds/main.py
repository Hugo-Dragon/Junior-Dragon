from click import command
import discord
from discord.ext import commands
from core.classes import Cog_Extension
from discord import Game

import json
with open("config.json", mode="r", encoding="utf8") as jfile:
    conf = json.load(jfile)

import random, datetime, time, asyncio, pytz

class Main(Cog_Extension):
    @commands.command() 
    async def ping(self, ctx):
        await ctx.send(f"🇵 🇴 🇳 🇬❗| 目前延遲:{round(self.bot.latency*1000)} (ms)")

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
    async def repeat(self, ctx, *,msg):
        await ctx.send(msg)

    @commands.command()
    async def clean(self, ctx, num: int):
        await ctx.channel.purge(limit=num+1)
        OK = await ctx.send("訊息已清理完畢^__^")
        await asyncio.sleep(3)
        await OK.delete()
    @commands.command()
    async def dev(self, ctx):
        twtz = pytz.timezone("Asia/Taipei")
        timestamp= time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        embed=discord.Embed(title="開發團隊", description="開發團隊列表", color=0xffbb00)
        embed.add_field(name="程式撰寫", value="恐龍#2549", inline=True)
        embed.add_field(name="機器人管理", value="恐龍#2549", inline=True)
        embed.add_field(name="總管理", value="恐龍#2549", inline=True)
        embed.add_field(name="P.S.", value="反正都是恐龍#2549管啦awa", inline=True)
        embed.set_footer(text=timestamp)
        await ctx.send(embed=embed)
    
    @commands.command() ### 尚未成功
    async def presence(self, ctx, type=None, *, game=None):
        '''Change the bot's presence'''
        if type is None:
            await ctx.send(f'Usage: `{ctx.prefix}presence [game/stream/watch/listen] [message]`')
        else:
            if type.lower() == 'game':
                await self.bot.change_presence(game=discord.Game(name=game))
                await ctx.send(f'Set presence to `Playing {game}`')
            elif type.lower() == 'watch':
                await self.bot.change_presence(game=discord.Game(name=game, type=3), afk=True)
                await ctx.send(f'Set presence to `Watching {game}`')
            elif type.lower() == 'listen':
                await self.bot.change_presence(game=discord.Game(name=game, type=2), afk=True)
                await ctx.send(f'Set presence to `Listening to {game}`')
            elif type.lower() == 'clear':
                await self.bot.change_presence(game=None)
                await ctx.send('Cleared Presence')
            else:
                await ctx.send('Usage: `.presence [game/stream/watch/listen] [message]`') 


def setup(bot):
    bot.add_cog(Main(bot))
