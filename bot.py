import discord
import os
from discord.ext import commands

TOKEN = open("TOKEN").readline()

client = commands.Bot(command_prefix='gnome, ')

@client.async_event
def on_ready():
    print("Gnome Boi is ready to meme.")

@client.async_event
def on_message(message):
    author = message.author
    content = message.content
    channel = message.channel
    vc = author.voice_channel

    if client.command_prefix + "laugh" in content.lower():
        yield from client.send_message(channel, "**HOOOH**")

        if vc is None:
            yield from client.send_message(channel, "Hello there, old chum. Not caring to chat with an old friend?")
        else:
            voice = yield from client.join_voice_channel(vc)
            player = voice.create_ffmpeg_player('hooh.mp3')
            player.start()

            playing = True
            
            while(playing):
                if player.is_done():
                    playing = False
            player.stop()

            yield from voice.disconnect()

client.run(TOKEN)