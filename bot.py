import discord
import os
import sys
import asyncio
from time import sleep
from discord.ext import commands

TOKEN = open("TOKEN").readline()

bot = commands.Bot(command_prefix=['Gnome, ', 'gnome, '], description="A Soundboard Bot")

clipList = os.listdir("clips/")
for i in range(len(clipList)):
    clipList[i] = clipList[i][:-4]


@bot.event
async def on_ready():
    print("Gnome Boi is ready to meme.")


@bot.command()
async def play(ctx):
    """Plays an audio clip in your voice channel."""
    
    def disconnect(error):
        coroutine = connection.disconnect()
        future = asyncio.run_coroutine_threadsafe(coroutine, bot.loop)
        try:
            future.result()
        except:
            print("Error disconnecting")
            pass

    voice = ctx.author.voice

    if voice is None:
        await ctx.send("Hello there, old chum. I can't find you.")
    else:
        for i in clipList:
            if ctx.message.content.endswith(str(i)):
                playing = True

                clip = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio("clips/" + str(i) + ".mp3"), volume=0.1)
                connection = await voice.channel.connect()
                connection.play(clip, after=disconnect)

                return
        await ctx.send("I can't seem to find that clip.")


@bot.command()
async def laugh(ctx):
    """Makes the bot laugh in your voice channel."""

    def disconnect(error):
        coroutine = connection.disconnect()
        future = asyncio.run_coroutine_threadsafe(coroutine, bot.loop)
        try:
            future.result()
        except:
            print("Error disconnecting")
            pass

    voice = ctx.author.voice
    await ctx.send("**HOOOH**")

    if voice is None:
        await ctx.send("Hello there, old chum. Not caring to chat with an old friend?")
    else:
        playing = True

        clip = discord.FFmpegPCMAudio('hooh.mp3')
        connection = await voice.channel.connect()
        play = connection.play(clip, after=disconnect)


@bot.command()
async def clips(ctx):
    """Lists all clips available for playback."""

    c = ''
    for i in clipList:
        c += str(i) + '\n'
    await ctx.send("```The clips I can play are:\n" + c + "```")


@bot.command()
async def leave(ctx):
    """Gracefully shuts the bot down."""

    person = ctx.author

    if person.id == 153935534207533056:
        await ctx.send("Goodbye then, old chum!")
        sys.exit()
    else:
        await ctx.send("No way!")


bot.run(TOKEN)