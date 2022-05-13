<<<<<<< HEAD
import discord # Unused Import
=======
import discord 
>>>>>>> 70bc067eb697736fa4c3ccb26be5966801ac26d4
from discord.ext import commands 
from core.classes import Cog_Extension


import json, random, datetime, asyncio
with open("config.json", mode="r", encoding="utf8") as config:
    conf = json.load(config)


class Event(Cog_Extension):
    @commands.Cog.listener() 
    async def on_message(self, msg):
        if msg.content.endswith(".3."): 
            random_030 = random.choice(conf[".3."]) 
            await msg.channel.send(random_030)

        ABAB_reply_select= ["ABAB", "ABABABAB"]
        ABAB_reply= random.choice(ABAB_reply_select)
        if msg.content == "ABAB" and msg.author != self.bot.user:
            await msg.channel.send(ABAB_reply)

        if msg.content == "Morning" and msg.author != self.bot.user:
            await msg.reply("Good Morning~")

        react_OAO_select= ["emmm", "???"]
        react_OAO= random.choice(react_OAO_select)
        if msg.content.endswith("OAO"):
            await msg.add_reaction(react_OAO)

        noubot_select= ["noob bot", "lan bot", "lag bot", "lan bot"]
        noubot_reply= random.choice(noubot_select)

        if msg.content == "lan bot" and msg.author != self.bot.user:
            await msg.channel.send(noubot_reply)


def setup(bot):
     bot.add_cog(Event(bot))