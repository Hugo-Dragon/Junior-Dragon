import discord
from discord.ext import commands

import json
with open("config.json", mode="r", encoding="utf8") as jfile:
    conf = json.load(jfile)

import random, datetime, time, asyncio, os, pytz
import keep_alive

bot = commands.Bot(command_prefix=">")
bot.remove_command("help")

timestamp= time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())


@bot.event
async def on_ready():
    print("Bot logined")
    print(bot.user)
    print("-----------") 
    await bot.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.listening, name="C.Debussy-Clair de lune"))

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
    embed=discord.Embed(title="Help", description="使用 >help <指令類別> 以取得該指令之更詳細使用方法", color=0xffbb00)
    embed.add_field(name="指令分類", value="Attano指令分類", inline=False)
    embed.add_field(name="Main", value="ping、say、repeat、botabout、dev、presence、clean", inline=False)
    embed.add_field(name="React", value="idk、thonk", inline=False)
    embed.add_field(name="Music", value="join、play、pause、resume、stop", inline=False)
    embed.add_field(name="Game", value="guessab", inline=False)
    embed.add_field(name="P.S.", value="除Music指令外，上述指令皆會隱藏使用者是誰", inline=False)
    embed.set_footer(text=timestamp)
    await ctx.send(embed=embed)

@help.command()
async def Main(ctx):
    twtz = pytz.timezone("Asia/Taipei")
    embed=discord.Embed(title="Main", description="主要指令區", color=0x0084ff)
    embed.add_field(name="ping", value="查看機器人目前延遲", inline=False)
    embed.add_field(name="say", value="讓機器人替你說話", inline=False)
    embed.add_field(name="repeat", value="讓機器人重複你說的話", inline=False)
    embed.add_field(name="botabout", value="機器人的簡介", inline=False)
    embed.add_field(name="dev", value="機器人開發團隊", inline=False)
    embed.add_field(name="clean", value="清除該頻道指定數量的訊息", inline=False)
    embed.add_field(name="presence", value="更改機器人目前的狀態", inline=False)
    embed.set_footer(text=timestamp)
    await ctx.send(embed=embed)

@help.command()
async def React(ctx):
    twtz = pytz.timezone("Asia/Taipei")
    embed=discord.Embed(title="React", description="反應指令區", color=0x00d103)
    embed.add_field(name="idk", value="發送一個窩不知道gif", inline=False)
    embed.add_field(name="thonk", value="隨機發送一個thonk貼圖", inline=False)
    embed.set_footer(text=timestamp)
    await ctx.send(embed=embed)

@help.command()
async def Music(ctx):
    twtz = pytz.timezone("Asia/Taipei")
    embed=discord.Embed(title="Music", description="音樂指令區（開發中）", color=0x00d103)
    embed.add_field(name="join", value="加入目前的語音頻道", inline=False)
    embed.add_field(name="play", value="播放音樂（對，目前只能夠一次播放一首）", inline=False)
    embed.add_field(name="pause", value="暫停目前播放的音樂", inline=False)
    embed.add_field(name="resume", value="重新播放已經暫停的音樂", inline=False)
    embed.add_field(name="stop", value="結束播放目前音樂", inline=False)
    embed.set_footer(text=timestamp)
    await ctx.send(embed=embed)

@help.command()
async def Game(ctx):
    embed=discord.Embed(title="Game", description="遊戲指令區（開發中）", color=0x00d103)
    embed.add_field(name="gn", value="猜數字遊戲", inline=False)
    embed.set_footer(text=timestamp)
    await ctx.send(embed=embed)


for filename in os.listdir("./cmds"):
    if filename.endswith(".py"):
        bot.load_extension(f"cmds.{filename[:-3]}")

if __name__ == "__main__" :
    bot.run(conf["token"])
