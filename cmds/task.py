import discord
from discord.ext import commands
from core.classes import Cog_Extension

import time, datetime, json, asyncio

class Task(Cog_Extension):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

def setup(bot):
    bot.add_Cog(Task(bot))
