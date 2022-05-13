"""
***************PY_Attano Bot***************
*************Author:hugocoding*************
**************Version: 0.0.2***************
**********Release Date:2022.5.12***********
"""
import discord
from discord.ext import commands
import keep_alive

import json, random, datetime, time, asyncio, os, pytz, keep_alive

with open("config.json", mode="r", encoding="utf8") as config:
    conf = json.load(config)

bot = commands.Bot(command_prefix=">")
bot.remove_command("help")

timestamp= time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())


@bot.event
async def on_ready():
    print("Bot logged in")
    print(bot.user)
    print("-----------") 
    await bot.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.listening, name="恐龍"))

@bot.command()
async def load(ctx, extension):
    bot.load_extension(f"cmds.{extension}")
    await ctx.send(f"Loaded {extension} done.")

@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f"cmds.{extension}")
    await ctx.send(f"Unloaded {extension} done.")

@bot.command()
async def reload(ctx, extension):
    bot.reload_extension(f"cmds.{extension}")
    await ctx.send(f"Reloaded {extension} done.")

@bot.group(invoke_without_command=True)
async def help(ctx):
    twtz = pytz.timezone("Asia/Taipei")
    embed=discord.Embed(title="Help", description="Use >help <command group> to get the way to use the command", color=0xffbb00)
    embed.add_field(name="Command Groups", value="PY_Attano's Command Groups", inline=False)
    embed.add_field(name="Main", value="ping, say, repeat, botabout, dev, presence, clean", inline=False)
    embed.add_field(name="React", value="idk, thonk", inline=False)
    embed.add_field(name="Music", value="join, play, pause, resume, stop", inline=False)
    embed.add_field(name="Game", value="gn", inline=False)
    embed.set_footer(text=timestamp)
    await ctx.send(embed=embed)

@help.command()
async def Main(ctx):
    twtz = pytz.timezone("Asia/Taipei")
    embed=discord.Embed(title="Main", description="The Main commands", color=0x0084ff)
    embed.add_field(name="ping", value="See the ping of the bot", inline=False)
    embed.add_field(name="say", value="Let the bot to say a message. \nAliases: `echo`", inline=False)
    embed.add_field(name="repeat", value="Let the bot to repeat a message", inline=False)
    embed.add_field(name="botabout", value="The introduce of the bot", inline=False)
    embed.add_field(name="dev", value="The dev of the bot", inline=False)
    embed.add_field(name="clean", value="Clean the specified number of messages for the channel", inline=False)
    embed.add_field(name="presence", value="Change the rich presence of the bot.*Still in development", inline=False)
    embed.add_field(name="botinfo", value="The info of the bot", inline=False)
    embed.set_footer(text=timestamp)
    await ctx.send(embed=embed)

@help.command()
async def React(ctx):
    twtz = pytz.timezone("Asia/Taipei")
    embed=discord.Embed(title="React", description="React commands", color=0x00d103)
    embed.add_field(name="idk", value="Sent a \"窩不知道\"gif", inline=False)
    embed.add_field(name="thonk", value="Sent a thonk texture", inline=False)
    embed.set_footer(text=timestamp)
    await ctx.send(embed=embed)

@help.command()
async def Music(ctx):
    twtz = pytz.timezone("Asia/Taipei")
    embed=discord.Embed(title="Music", description="Music Commands *Still in development", color=0x00d103)
    embed.add_field(name="join", value="Join the voice channel", inline=False)
    embed.add_field(name="play", value="Play the music *The Queue is still in development", inline=False)
    embed.add_field(name="pause", value="Pause the music", inline=False)
    embed.add_field(name="resume", value="Resume the music", inline=False)
    embed.add_field(name="stop", value="Stop the music", inline=False)
    embed.set_footer(text=timestamp)
    await ctx.send(embed=embed)

@help.command()
async def Game(ctx):
    embed=discord.Embed(title="Game", description="Game Commands *Still in development", color=0x00d103)
    embed.add_field(name="gtn", value="Guess the Number", inline=False)
    embed.set_footer(text=timestamp)
    await ctx.send(embed=embed)

@help.command()
async def Fun(ctx):
    embed=discord.Embed(title='Fun', description='Fun Commands *Still In Development*', color=0x00d103)
    embed.add_field(name='nitro', value='send a nitro to you [rickroll lol]', inline=False)
    embed.set_footer(text=timestamp)
    await ctx.send(embed=embed)

for filename in os.listdir("./cmds"):
    if filename.endswith(".py"):
        bot.load_extension(f"cmds.{filename[:-3]}")

if __name__ == "__main__" :
    keep_alive.keep_alive()
    bot.run(conf["token"])
