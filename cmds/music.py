from aiohttp import ClientProxyConnectionError
import discord
import os
# load our local env so we dont have the token in public
from dotenv import load_dotenv
from discord.ext import commands
from core.classes import Cog_Extension
from discord.utils import get
from discord import FFmpegPCMAudio
from discord import TextChannel
from youtube_dl import YoutubeDL

import json
with open("config.json", mode="r", encoding="utf8") as jfile:
    config = json.load(jfile)

import random, datetime, asyncio

class Music(Cog_Extension):
    @commands.command()
    # command for bot to join the channel of the user, if the bot has already joined and is in a different channel, it will move to the channel the user is in
    async def join(self, ctx):
        channel = ctx.message.author.voice.channel
        voice = get(self.bot.voice_clients, guild=ctx.guild)
        if voice and voice.is_connected():
            await voice.move_to(channel)
        else:
            voice = await channel.connect()

    # command to play sound from a youtube URL
    @commands.command()
    async def play(self, ctx, url):
        YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist': 'True'}
        FFMPEG_OPTIONS = {
            'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
        voice = get(self.bot.voice_clients, guild=ctx.guild)

        if not voice.is_playing():
            with YoutubeDL(YDL_OPTIONS) as ydl:
                info = ydl.extract_info(url, download=False)
            URL = info['url']
            voice.play(FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))
            voice.is_playing()
            await ctx.message.add_reaction("✔")

        # check if the bot is already playing
        else:
            await ctx.send(":x: It's already playing now!")
            return
    
    # command to resume voice if it is paused
    @commands.command()
    async def resume(self, ctx):
        voice = get(self.bot.voice_clients, guild=ctx.guild)

        if not voice.is_playing():
            voice.resume()
            await ctx.message.add_reaction("✅")

    # command to pause voice if it is playing
    @commands.command()
    async def pause(self, ctx):
        voice = get(self.bot.voice_clients, guild=ctx.guild)

        if voice.is_playing():
            voice.pause()
            await ctx.message.add_reaction("✅")


    # command to stop voice
    @commands.command()
    async def stop(self, ctx):
        voice = get(self.bot.voice_clients, guild=ctx.guild)

        if voice.is_playing():
            voice.stop()
            await ctx.message.add_reaction("✅")

def setup(bot):
    bot.add_cog(Music(bot))