mytitle = "{Flicks}"
from os import system
system("title "+mytitle)
import psutil
from pypresence import Presence
import time
import sys
import os
client_id = 'Your Account ID'
import discord
import asyncio
import colorama
from colorama import Fore, init, Style
import platform
from serverclone import Clone
flicks=("Flicks Cloner - /maxonfire")
Name = input(f'What Is Your Name :')
client = discord.Client()
os = platform.system()
if os == "Windows":
    system("cls")
else:
    system("clear")
    print(chr(27) + "[2J")
print(f"""{Fore.BLUE}


░█████╗░██╗░░░░░░█████╗░███╗░░██╗███████╗██████╗░
██╔══██╗██║░░░░░██╔══██╗████╗░██║██╔════╝██╔══██╗
██║░░╚═╝██║░░░░░██║░░██║██╔██╗██║█████╗░░██████╔╝
██║░░██╗██║░░░░░██║░░██║██║╚████║██╔══╝░░██╔══██╗
╚█████╔╝███████╗╚█████╔╝██║░╚███║███████╗██║░░██║
░╚════╝░╚══════╝░╚════╝░╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝
{Style.RESET_ALL}
                {Fore.MAGENTA}Developed by: Flicks /maxonfire.{Style.RESET_ALL}
        """)
print("Hy Fucking bich Skidder ")
token = input(f'{Name} Randike Token Dall:')

guild_s = input(f' {Name} Enter Guild Id Which You Want To Copy:')
guild = input(f'{Name} Enter Guild Where You Want To Copy : ')
print(f"{Name} max join kr mc /maxonfire ")
input_guild_id = guild_s  # <-- input guild id
output_guild_id = guild  # <-- output guild id
token = token  # <-- your Account token


print("  ")
print("  ")

@client.event
async def on_ready():
    extrem_map = {}
    print(f"Logged In as : {client.user}")
    print("Cloning Server")
    guild_from = client.get_guild(int(input_guild_id))
    guild_to = client.get_guild(int(output_guild_id))
    await Clone.guild_edit(guild_to, guild_from)
    await Clone.roles_delete(guild_to)
    await Clone.channels_delete(guild_to)
    await Clone.roles_create(guild_to, guild_from)
    await Clone.categories_create(guild_to, guild_from)
    await Clone.channels_create(guild_to, guild_from)
    print(f"""{Fore.GREEN}


░█████╗░██╗░░░░░░█████╗░███╗░░██╗███████╗██████╗░
██╔══██╗██║░░░░░██╔══██╗████╗░██║██╔════╝██╔══██╗
██║░░╚═╝██║░░░░░██║░░██║██╔██╗██║█████╗░░██║░░██║
██║░░██╗██║░░░░░██║░░██║██║╚████║██╔══╝░░██║░░██║
╚█████╔╝███████╗╚█████╔╝██║░╚███║███████╗██████╔╝
░╚════╝░╚══════╝░╚════╝░╚═╝░░╚══╝╚══════╝╚═════╝░



    {Style.RESET_ALL}""")
    await asyncio.sleep(5)
    client.close()


client.run(token, bot=False)