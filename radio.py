import discord
from discord import app_commands
from discord.ext import commands
import asyncio
import random
import requests
import io
import aiohttp
import pydub
import logging

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

logging.basicConfig(level=logging.INFO)

@bot.event
async def on_ready():
    print(f'{bot.user} has logged in')
    try:
        print("Starting command sync...")
        await bot.tree.sync()
        print("Commands synchronized globally")
        
        for guild in bot.guilds:
            await bot.tree.sync(guild=guild)
            print(f"Commands synchronized for server: {guild.name}")
        
        print("All commands synchronized successfully")
    except Exception as e:
        print(f"Command sync error: {e}")
    
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="Radio"))


@bot.tree.command(name="play")
async def play(interaction: discord.Interaction):
    """Plays Underground Bass Radio as test"""
    if not interaction.user.voice:
        await interaction.response.send_message("You have to be in a voice channel to use this command.")
        return
    
    channel = interaction.user.voice.channel
    voice_client = interaction.guild.voice_client
    
    if voice_client and voice_client.is_connected():
        await voice_client.move_to(channel)
    else:
        voice_client = await channel.connect()
        """Put of radio link here"""
    audio_source = discord.FFmpegPCMAudio("http://65.108.124.70:7200/stream")
    voice_client.play(audio_source)
    
    await interaction.response.send_message("Playing Radio !")

@bot.tree.command(name="stop")
async def stop(interaction: discord.Interaction):
    voice_client = interaction.guild.voice_client
    if voice_client and voice_client.is_connected():
        await voice_client.disconnect()
        await interaction.response.send_message("Bot disconnected.")
    else:
        await interaction.response.send_message("Bot is not in any voice channel.")

@bot.event
async def on_message(message):
    if bot.user.mentioned_in(message) and not message.mention_everyone:
        greet = [
            f"¡Hello {message.author.name}! are you ready to dance?",
        ]
        await message.channel.send(random.choice(greet))
    
    await bot.process_commands(message)

bot.run('YOUR DISCORD DEV API KEY HERE')