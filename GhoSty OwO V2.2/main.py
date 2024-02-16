import os as brutality_ghosty
brutality_ghosty.system("pip install discord.py==1.7.3")
brutality_ghosty.system("pip install colorama")
brutality_ghosty.system('sleep 2 && clear >/dev/null 2>&1 &' if brutality_ghosty.name == 'posix' else 'timeout /t 2 >nul 2>&1 && cls')
import json as ghostop
import random as ghostyjija
from colorama import Fore, Style, init
import discord
from discord.ext import commands, tasks
import asyncio as made_by_ghosty
# SKID IT 😂 || Made By GhoSty 
ghostyop = discord.Intents.all(); GhoStyyy = ("."); ghosty = commands.Bot(command_prefix=GhoStyyy, case_insensitive=True, self_bot=True, intents=ghostyop); ghosty.remove_command("help")
# SKID IT 😂 || Made By GhoSty 
running = True
pray_loop_running = True
# SKID IT 😂 || Made By GhoSty 
print(f"""{Fore.BLUE}

           ▒▒                    ▒▒            ▒▒       ▒▒▒
        ▒▒▒▒▒▒▒   ▒▒▒     ▒▒▒▒ ▒▒▒▒▒▒▒▒        ▒▒▒▒     ▒▒▒▒ ▒▒▒▒▒               ▒▒▒▒▒ 
      ▒▒▒▒████▒▒ ▒▒█▒▒  ▒▒▒█▒▒▒▒░█████▒        ▒█▒▒   ▒▒▒██▒ ████▒▒              ████▒▒
     ▒▒▒▒██░░██▒▒▒██▒▒ ▒▒░██▒░▒██░░░░█▒        ▒██▒▒ ▒▒██░▒▒ █▒▒▒█▒              █▒▒▒█▒
     ▒▒██░░░░██▒▒██▒▒▒ ▒░██▒▒██░░░░░░█▒        ▒▒█▒▒▒▒██▒▒▒   ▒▒▒█▒              ▒▒▒█▒
    ▒▒██░░█░░█▒▒▒█▒▒▒▒▒▒░█▒▒▒█░░░█░░██▒         ▒█▒▒▒██▒▒  ▒▒▒▒▒██▒           ▒▒▒▒▒██▒
    ▒▒█░░░░░░█▒▒█░░██░▒░█▒▒ ▒█░░░░░█▒▒▒         ▒░█▒██▒▒   ▒▒▒██▒▒▒▒▒         ▒▒▒██▒▒▒▒▒
    ▒▒█░░░░██▒▒▒████████▒▒  ▒██░░███▒▒          ▒▒██░▒    ▒▒███▒░▒██▒        ▒▒███▒░▒██▒
     ▒██████▒▒▒███▒▒▒██▒▒   ▒▒████▒▒▒            ▒█▒▒     ▒████████▒▒        ▒████████▒▒
    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒     ▒▒▒▒▒▒              ▒▒▒      ▒▒▒▒▒▒▒▒▒▒    █    ▒▒▒▒▒▒▒▒▒▒
     ▒▒▒▒▒    ▒▒▒▒▒▒▒▒▒      ▒▒▒▒▒               ▒▒▒
               ▒▒   ▒▒        ▒▒                 ▒▒{Style.RESET_ALL}""")
# SKID IT 😂 || Made By GhoSty 
init(autoreset=True)
print(f"{Fore.LIGHTRED_EX}\n\n > Made By GhoSty{Style.RESET_ALL}")
# SKID IT 😂 || Made By GhoSty 
@ghosty.event
async def on_ready():
    print(f"{Fore.LIGHTRED_EX} > OwO Farm v2 Connected To:{Style.RESET_ALL}", f"{Fore.LIGHTGREEN_EX}{ghosty.user}{Style.BRIGHT}{Style.RESET_ALL}")
# SKID IT 😂 || Made By GhoSty 
@ghosty.command(aliases = ["h"])
async def help(ctx):
    ghosty_help = """
    # 🤑 GhoSty OwO Farm V2.2 🤑 
Prefix: `.`

**__Main__**
 🌟 Start: *Starts The AutoBot*
 🛑 Stop: *Stops The AutoBot*

**__Features__**
 ⚠ Ban Bypass
 🚨 Auto Detects OwO Warnings
 ⏱ Auto Cut After 1 Warning
 💎 Auto Use Gems [Will Be Added In V3]
 🏹 Fast And Secure

**__Made with 💖 and 🧠 by GhoSty__**
"""
    await ctx.send(ghosty_help)
# SKID IT 😂 || Made By GhoSty 
# SKID IT 😂 || Made By GhoSty 
@ghosty.command()
async def start(ctx):
    global running
    while running:
        await ctx.send("owo hunt")
        await made_by_ghosty.sleep(2.5)
        
        await ctx.send("owo battle")# SKID IT 😂 || Made By GhoSty 
        await made_by_ghosty.sleep(2.5)

        await ctx.send("owo sell all")# SKID IT 😂 || Made By GhoSty 
        await made_by_ghosty.sleep(2.5)

        await ctx.send("owo pray")# SKID IT 😂 || Made By GhoSty 
        await made_by_ghosty.sleep(6)
# SKID IT 😂 || Made By GhoSty 
        phrases = [
            "ughhh am bored",
            "hell naaaaa",# SKID IT 😂 || Made By GhoSty 
            "lemme grind some moree",
            "To-do list: 1. Talk to myself, 2. Repeat",
            "ayo what",
            "dang it",
            "nuh uhhh",# SKID IT 😂 || Made By GhoSty 
            "i gotta do this",
            "If I were a superhero, my power would be the ability to find lost socks"
        ] # SKID IT 😂 || Made By GhoSty 

        await ctx.send(ghostyjija.choice(phrases))  

       
        latest_messages = await ctx.channel.history(limit=10).flatten()
        for message in latest_messages:
            if "please complete your captcha" in message.content.lower() or "please solve the captcha" in message.content.lower():
                await ctx.send("⚠ Warning Detected! 🛑 Stopping The Process | Run The Script Again To Continue")
                print("⚠ Warning Detected! 🛑 Stopping The Process | Run The Script Again To Continue")
                running = False
                break
# SKID IT 😂 || Made By GhoSty 

# SKID IT 😂 || Made By GhoSty 
            if not running:
                break 
# SKID IT 😂 || Made By GhoSty 
@ghosty.command()
async def stop(ctx):
    global running
    await ctx.send("🛑 Stopping | Run The Script Again To Continue")
    running = False

with open("config.json", "r") as config_file:
    config = ghostop.load(config_file)

ghostyopaf = (config["TOKEN"]) # SKID IT 😂 || Made By GhoSty 
ghosty.run(ghostyopaf, bot=False)
# SKID IT 😂 || Made By GhoSty 