import discord
import os
import sys
import asyncio
from time import sleep
from discord.ext import commands

TOKEN = open("TOKEN").readline()

bot = commands.Bot(command_prefix=['Gnome, ', 'gnome, '], description="A Soundboard Bot")

try: 
    clipList = os.listdir("clips/")
    for i in range(len(clipList)):
        clipList[i] = clipList[i][:-4]
except:
    print("clips directory not found.")
    clipList = []
    pass


@bot.event
async def on_ready():
    print("Gnome Boi is ready to meme.")


@bot.command()
async def play(ctx, arg):
    """Plays an audio clip in your voice channel."""
    
    voice = ctx.author.voice.channel

    if voice is None:
        await ctx.send("Hello there, old chum. I can't find you.")
    else:
        for i in clipList:
            if str(arg).endswith(str(i)):
                clip = discord.FFmpegPCMAudio('{}.mp3'.format(str(arg)))

                await playSound(ctx, clip)

                return
        await ctx.send("I can't seem to find that clip.")


@bot.command()
async def laugh(ctx):
    """Makes the bot laugh in your voice channel."""

    await ctx.send("**HOOOH**")

    laugh = discord.FFmpegPCMAudio('hooh.mp3')

    await playSound(ctx, laugh)


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


async def playSound(ctx, audioSource):
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
        await ctx.send("Hello there, old chum. Not caring to chat with an old friend?")
    else:
        playing = True

        clip = discord.PCMVolumeTransformer(
            audioSource, volume=0.5
        )
        connection = await voice.channel.connect()
        play = connection.play(clip, after=disconnect)


bot.run(TOKEN)