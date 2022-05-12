import discord
from discord.ext import commands
from core.classes import Cog_Extension

import json
with open("config.json", mode="r", encoding="utf8") as jfile:
    conf = json.load(jfile)

import random, datetime, asyncio

class Event(Cog_Extension):
    @commands.Cog.listener() 
    async def on_message(self, msg):
        if msg.content.endswith(".3."): 
            random_030 = random.choice(conf[".3."]) 
            await msg.channel.send(random_030)

        ABAB_reply_select= ["ABAB", "<:AB:949465980520792124>"]
        ABAB_reply= random.choice(ABAB_reply_select)
        if msg.content == "<:AB:949465980520792124>" and msg.author != self.bot.user:
            await msg.channel.send(ABAB_reply)

        if msg.content == "Morning" and msg.author != self.bot.user:
            await msg.reply("Good Morning~")

        react_OAO_select= ["<:emm_:949465980378173480>", "<:Thonk:916885587447934986>"]
        react_OAO= random.choice(react_OAO_select)
        if msg.content.endswith("OAO"):
            await msg.add_reaction(react_OAO)

        noubot_select= ["noob bot", "lan bot", "lag bot", "lan bot"]
        noubot_reply= random.choice(noubot_select)

        if msg.content == "lan bot" and msg.author != self.bot.user:
            await msg.channel.send(noubot_reply)


def setup(bot):
     bot.add_cog(Event(bot))