import discord
from discord.ext import commands
import json

with open("setting.json", mode="r", encoding="utf8") as jfile:
    jdata = json.load(jfile) #import setting.json

import random #隨機取數模組
import datetime
import asyncio
import os 
import pytz

bot = commands.Bot(command_prefix=">") #定義主程式的"bot"為command.Bot,前綴為">"
bot.remove_command("help")

@bot.event
async def on_ready():
    print('>>Login as', bot.user) #Terminal會告知上線中
    ing=discord.Activity(type=discord.ActivityType.playing,name="Atom Editor") #presence
    await bot.change_presence(status=discord.Status.online, activity=ing)

@bot.command()
async def load(ctx, extension):
    bot.load_extension(f"cmds.{extension}")
    await ctx.send(f"Loaded {extension} done.")

@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f"cmds.{extension}")
    await ctx.send(f"Un-loaded {extension} done.")

@bot.command()
async def reload(ctx, extension):
    bot.reload_extension(f"cmds.{extension}")
    await ctx.send(f"Re-loaded {extension} done.")

@bot.group(invoke_without_command=True)
async def help(ctx):
    twtz = pytz.timezone("Asia/Taipei")
    timestamp= datetime.datetime.now().replace(tzinfo=twtz)
    embed=discord.Embed(title="Help", description="使用 >help <指令類別> 以取得該指令之更詳細使用方法", color=0xffbb00)
    embed.add_field(name="指令分類", value="Attano指令分類", inline=False)
    embed.add_field(name="Main", value="ping、say、repeat、botabout、dev", inline=False)
    embed.add_field(name="React", value="idk、thonk", inline=False)
    embed.add_field(name="P.S.", value="上述指令皆會隱藏使用者是誰", inline=False)
    embed.set_footer(text=timestamp)
    await ctx.send(embed=embed)

@help.command()
async def Main(ctx):
    twtz = pytz.timezone("Asia/Taipei")
    timestamp= datetime.datetime.now().replace(tzinfo=twtz)
    embed=discord.Embed(title="Main", description="主要指令", color=0x0084ff)
    embed.add_field(name="ping", value="查看機器人目前延遲", inline=False)
    embed.add_field(name="say", value="讓機器人替你說話", inline=False)
    embed.add_field(name="repeat", value="讓機器人重複你說的話", inline=False)
    embed.add_field(name="botabout", value="機器人的簡介", inline=False)
    embed.add_field(name="dev", value="機器人開發團隊", inline=False)
    embed.set_footer(text=timestamp)
    await ctx.send(embed=embed)

@help.command()
async def React(ctx):
        twtz = pytz.timezone("Asia/Taipei")
        timestamp= datetime.datetime.now().replace(tzinfo=twtz)
        embed=discord.Embed(title="React", description="反應指令", color=0x00d103)
        embed.add_field(name="idk", value="發送一個窩不知道gif", inline=False)
        embed.add_field(name="thonk", value="隨機發送一個thonk貼圖", inline=False)
        embed.set_footer(text=timestamp)
        await ctx.send(embed=embed)

for filename in os.listdir("./cmds"):
    if filename.endswith(".py"):
        bot.load_extension(f"cmds.{filename[:-3]}")

if __name__ == "__main__" :
    bot.run(jdata["token"])
