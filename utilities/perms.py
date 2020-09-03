import discord.ext.commands as commands

def admin_perms():
    return commands.has_permissions(administrator=True)

def mod_perms():
    return commands.has_permissions(manage_messages=True)

def kick_perms():
    return commands.has_permissions(kick_members=True)

def ban_perms():
    return commands.has_permissions(ban_members=True)