#Starter bot made by dathidewolf
#if you get invalid syntax errors or any kind of error [before you edit the code, assuming thats not the first thing you do] let me know
#if you liked this Starter and it helped you, feel free to head on over to my youtube or twitter and support me Twitter; https://twitter.com/Dathidewolf  Youtube; https://www.youtube.com/channel/UC2_8JEMcpbdH0Bc5oBDknFQ?view_as=subscriber

#reminders to do
#make better support command, tidy the code up a bit

import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import random
import chalk
import time
import os

bot = commands.Bot(command_prefix='put your prefix here')

#Please dont remove this i would like to be credited, if you then shame on you :thumbs down:
description = "A Starter bot made by Dathidewolf, if you want your own starter bot contact me @dathidewolf#4041"

#To make your own commands just copy paste this below and fill in the blanks
#@bot.command(pass_context=True)
#async def putcommandtrigggerhere(ctx):
#    await bot.say("put what you want bot to say here")


#Do not touch these
@bot.event
async def on_ready():
    print ("IM ALL FIRED UP")
    print ("I am running on " + bot.user.name)
    print ("With the ID: " + bot.user.id)
    print ("Get help here")
    print ("https://discord.gg/tHuD92K")

#To see if bot is up and reading commands 
@bot.command(pass_context=True)
async def ping(ctx):
    await bot.say(":ping_pong: Pong!")
    print ("user has pinged")

#Get info on a user
@bot.command(pass_context=True)
async def info(ctx, user: discord.Member):
    await bot.say("The users name is: {}".format(user.name))
    await bot.say("The users ID is: {}".format(user.id))
    await bot.say("The users status is: {}".format(user.status))
    await bot.say("The users highest role is: {}".format(user.top_role))
    await bot.say("The user joined at: {}".format(user.joined_at))

#kick somebody
@bot.command(pass_context=True)
@commands.has_role("put admin role here")
async def kick(ctx, user: discord.Member):
    await bot.say(":boot: Cya, {}. Ya loser!".format(user.name))
    await bot.kick(user)
    print ("user has kicked someone")

#ban somebody
@bot.command(pass_context=True)
@commands.has_role("put owner role here")
async def ban(ctx, user: discord.Member):
    await bot.say("okay! ill ban {}, for you!".format(user.name))
    await bot.ban(user)
    print ("user has banned someone")

#what a well mannered bot
@bot.command(pass_context=True)
async def hi(ctx):
    await bot.say("Hello! nice to meet you!")

#again please do not touch this part.
@bot.command(pass_context=True)
async def botsupport(self, ctx):
    #dont remove this line please
    await bot.say("If you have any problems or bugs :bug: , get help with the source code here here https://discord.gg/tHuD92K :smiley: ")
    #if you edit the code feel free to remove "starter" cause if you edit it its not a starter bot is it?
    await bot.say("And if you do not own this starter bot, and want to start on coding/making bots ask @dathidewolf#4041, my master!")

#havent really tested this either, if it causes problems let me know
@bot.command(pass_context=True)
async def cool(self, context):
    """are you cool?"""
    author = context.message.author.mention

    choices = ['yes', 'no', 'i wouldint count on it', ' definatly not']

    image = random.choice(choices)

    embed = discord.Embed(description=choices.format(author), colour=discord.Colour.blue())
    await self.bot.say(embed=embed)


#Use at your own risk, it might break the bot, i have not tested it yet and do not plan on doing so, if you want to use it remove the "#"
#IF this does break the bot contact me at @dathidewolf#4041, i will get around to testing it, if you cant fix it just ask me to help i can probably fix it
#@bot.command(pass_context=True)
#async def pingt(ctx):
#    channel = ctx.message.channel
#    t1 = time.perf_counter()
#    await self.bot.send_typing(channel)
#    t2 = time.perf_counter()
#    await bot.say("pseudo-ping: {}ms".format(round((t2-t1)*1000)))

#Again i dont know if this works on this one file bot, works on my multiple file bot, yet again contact me if [somehow]it breaks your bot
#@bot.command(pass_context=True)
#async def unban(self, ctx, userid):
#    """Unban Users"""
#    userobj = await self.bot.get_user_info(userid)
#    await self.bot.unban(ctx.message.server, userobj)
#    await self.modcog.new_case(ctx.message.server, user=userobj, action="UNBAN")
#    await self.bot.say("Done.")


bot.run("PUT YOUR BOTS TOKEN HERE")
