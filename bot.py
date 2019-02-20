import discord
import os
import sys
from discord.ext import commands

TOKEN = open("TOKEN").readline()

bot = commands.Bot(command_prefix=['Gnome, ', 'gnome, '], description="A Soundboard Bot")

@bot.event
async def on_ready():
    print("Gnome Boi is ready to meme.")

@bot.command()
async def laugh(ctx):
    voice = ctx.author.voice
    await ctx.send("**HOOOH**")

    if voice is None:
        await ctx.send("Hello there, old chum. Not caring to chat with an old friend?")
    else:
        playing = True

        clip = discord.FFmpegPCMAudio('hooh.mp3')
        client = await voice.channel.connect()
        client.play(clip)

        while playing:
            if not client.is_playing():
                await client.disconnect()
                playing = False

@bot.command()
async def leave(ctx):
    person = ctx.author

    if person.id == 153935534207533056:
        await ctx.send("Goodbye then, old chum!")
        sys.exit()
    else:
        await ctx.send("No way!")


bot.run(TOKEN)