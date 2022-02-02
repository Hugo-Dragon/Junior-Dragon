from multiprocessing.spawn import import_main_path


import discord
from discord.ext import commands

class Cog_Extension(commands.Cog):
    def __init__(self, bot):
        self.bot = bot