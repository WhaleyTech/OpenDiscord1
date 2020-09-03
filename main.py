import os
import json
import discord

import discord.ext.commands as commands

#if adding new commands, please refer to utilities/helplist.py
class Main(commands.Bot):
    def __init__(self):
        self.config = 'config.json'
        try:
            with open(self.config) as fp:
                self.config = json.load(fp)
            print("Found config.json!")
        except Exception as e:
            print("Could not find config.json!")
            print(e)
            print("=========================================")
            exit(0)

        super().__init__(commands.when_mentioned_or(self.config['prefix']), description="Hello I'm OD1!")

bot = Main()
    
for file in bot.config["cogs"]:
    bot.load_extension(file)

bot.run(bot.config['token'])
