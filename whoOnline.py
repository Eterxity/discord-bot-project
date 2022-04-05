import discord 
from discord.ext import commands,tasks
from discord import Member
import random
from random import randint
import os
from discord import Intents

#Prefix
bot = commands.Bot(command_prefix=".", intents = Intents.all())
message = ""

#Cogs
from help_cog import help_cog
from music_cog import music_cog

bot.remove_command('help')

#register the class with the bot
bot.add_cog(help_cog(bot))
bot.add_cog(music_cog(bot))

#Penis size command
@bot.command()
async def penis(ctx):
    penis_size = randint(0, 30)
    if str(ctx.message.author) == "Eterxity#6778":
        await ctx.reply("You have the biggest dick here!")
    elif str(ctx.message.author) == "奏 Cryptic#8596":
        await ctx.reply("You have small dick")
    elif str(ctx.message.author) == "veno#2024":
        await ctx.reply("You have no dick lmao")
    elif str(ctx.message.author) == "ShallowAjax#4091":
        await ctx.reply("Your dick size is determined by the first person to reply to this")
    else:
        await ctx.reply("Your penis is about this long "+str(penis_size)+" cm long")

#How gay command
@bot.command()
async def howgay(ctx):
    how_gay = randint(0, 100)
    if str(ctx.message.author) == "Eterxity#6778":
        await ctx.reply("You are not gay at all!")
    elif str(ctx.message.author) == "奏 Cryptic#8596":
        await ctx.reply("You're a femboy! Thus you are gay.")
    elif str(ctx.message.author) == "ShallowAjax#4091":
        await ctx.reply("You will always be 50 percent gay.")
    else:
        await ctx.reply("You are exactly "+str(how_gay)+" percent gay")

#Status of members
@bot.command(name="status")
async def status(ctx, user: discord.Member=None):
    if not user:
        user = ctx.message.author
    await ctx.reply(user.raw_status)

#Bot status
@bot.event
async def on_ready():
    await bot.change_presence(activity = discord.Game("with your mom's titties"))
    await bot.get_channel(960214328814997557).send("i'm ready to eat ass and kick bubblegum. and i'm all out of gum")
    print("bot's online")

#Auto role
@bot.event
async def on_member_join(member):
    role = discord.utils.get(member.server.roles, name = "egirls")
    await bot.add_role(member, role)

#Runs the bot
bot.run("OTU5OTQ4Nzk0OTk1MzEwNjYy.YkjT-w.aArbmhuQDxSclx23H7dckTO3_Gw")