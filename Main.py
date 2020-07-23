import os, json, discord

import discord.ext.commands as commands

#if adding new commands, please refer to utilities/helplist.py
class Main(commands.Bot):
    
    def __init__(self):
        self.config = 'config.json'
        try:
            with open(self.config) as fp:
                self.config = json.load(fp)
            print("Found config.json!")
        except:
            print("Could not find config.json!")
            
        super().__init__(commands.when_mentioned_or(self.config['prefix']), description="Hello I'm OD1!")

        for file in os.listdir("cogs"):
            if file.endswith(".py"):
                name = file[:-3]
                self.load_extension(f"cogs.{name}")

bot = Main()
bot.run(bot.config['token'])