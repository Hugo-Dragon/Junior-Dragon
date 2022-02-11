import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json

with open("setting.json", mode="r", encoding="utf8") as jfile:
    jdata = json.load(jfile)

import random
import datetime
import asyncio

class Event(Cog_Extension):
    @commands.Cog.listener() #on_message關鍵字觸發
    async def on_message(self, msg):
        if msg.content.endswith(".3."): #結尾為.3.
            random_030 = random.choice(jdata[".3."]) #隨機取setting.json的.3.項目
            await msg.channel.send(random_030)

        ABAB_reply_select= ["ABAB", "<:ABAB:846568946722799646>"]
        ABAB_reply= random.choice(ABAB_reply_select)
        if msg.content == "<:ABAB:846568946722799646>" and msg.author != self.bot.user:
            await msg.channel.send(ABAB_reply)

        if msg.content == "早安" and msg.author != self.bot.user:
            await msg.reply("<:Morning:847652251107196939>")

        react_OAO_select= ["<:emmm:846569832823783436>", "<:cat_17:935731635440214027>", "<:emoji_14:833126188608127056>"]
        react_OAO= random.choice(react_OAO_select)
        if msg.content.endswith("OAO"):
            await msg.add_reaction(react_OAO)

        noubot_select= ["笑死", "爛bot", "<:emoji_13:833126152742502481>"]
        noubot_reply= random.choice(noubot_select)

        if msg.content == "爛bot" and msg.author != self.bot.user:
            await msg.channel.send(noubot_reply) 


def setup(bot):
     bot.add_cog(Event(bot))
