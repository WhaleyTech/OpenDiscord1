import discord, json, logging
from discord.ext import commands

log = logging.getLogger()
log.setLevel(logging.INFO)
handler.setFormatter(logging.Formatter('{asctime}:{levelname}:{name}:{message}', style='{'))
log.addHandler(handler)

logging.getLogger('discord').setLevel(logging.WARNING)