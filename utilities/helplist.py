#'list' = ['command alias', 'description about the command']  --- add command list to 'cogs'

info = ['info', 'Get some info about the bot']
addme = ['addme, invite', 'Shares a link that allows the bot to join your own discord server']
commits = ['commits, commit', 'Shows the latest commit history pushed to github']
id = ['id', "returns numeric ID of a user, or the author's ID if no user is specified"]
coinflip = ['coinflip', 'Flips a coin!']
rolldice = ['rolldice', 'Rolls a die :game_die:']
uppercase = ['uppercase', 'Makes the message uppercase']
lowercase = ['lowercase', 'Makes your message lowercase']
reverse = ['reverse', '!sdrow ruoy sesreveR']
eightball = ["eightball, 8ball, 8, ball", "The magic eight ball! :crystal_ball:"]
markdown = ["markdown", "Help on how to use markdown within Discord"]
codeblock = ["codeblock", "Makes user text into a 'fix' style codeblock"]
mock = ["mock", "YoU CaN't JuSt PuT tHiS mEmE oN eVeRyThInG"]
leetcode = ['leetcode', 'Sends URL of random LeetCode problems']
purge = ["purge", "Deletes messages within the channel"]
kick = ["kick", "Kicks a specified user"]
ban = ["ban", "Bans a specified user"]
unban = ["unban", "Unbans a specified user"]

info_cmds = [info, addme, commits, id]
rand_cmds = [info, addme, commits, leetcode, coinflip, 
            rolldice, uppercase, lowercase, reverse, eightball, 
            markdown, codeblock]
admin_cmds = [purge, kick, ban, unban]