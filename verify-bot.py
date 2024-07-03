#Hello! This code is made by @Endruvz on Github
#If this code helps you get the active developer badge please star the reposirory on Github C:

#imports
import inspect
import os
import discord
import time

from colorama import Fore, Style, just_fix_windows_console

try:
    from discord import app_commands
except ImportError:
    exit("Error! Discord.py in not insalled or is outdated.")


just_fix_windows_console()

#cool logo :O
name = f'''
{Fore.LIGHTBLUE_EX}██████╗ ███████╗██╗   ██╗██████╗  ██████╗ ████████╗
██╔══██╗██╔════╝██║   ██║██╔══██╗██╔═══██╗╚══██╔══╝
██║  ██║█████╗  ██║   ██║██████╔╝██║   ██║   ██║   
██║  ██║██╔══╝  ╚██╗ ██╔╝██╔══██╗██║   ██║   ██║   
██████╔╝███████╗ ╚████╔╝ ██████╔╝╚██████╔╝   ██║   
╚═════╝ ╚══════╝  ╚═══╝  ╚═════╝  ╚═════╝    ╚═╝  \n'''

#starting text
print(name+ inspect.cleandoc(f"""
                             
                             Hello! Welcome to DevBot.
                             To get your active developer badge you need to create your bot and enter in your bot token under this message.
                             
                             {Style.DIM}{Fore.WHITE}Make sure to enable community on your discord server or you wont get the badge!!!{Style.RESET_ALL} 
                             {Fore.RED}Only close this program after the bot joined the discord server and you ran the command!!!{Fore.RESET} """))

time.sleep(1) #stops for a bit, just cause :)

#gets the location of your folder
filepath = os.getcwd()

#tries to open file
try:
    tokenf = open(filepath+"/config.txt", "r")
except FileNotFoundError:
    exit("config.txt does not exist or has been deleted! Create a txt file in the the folder called 'config.txt' and try again.")

#this is where you input your token
while True:
    if os.path.getsize(filepath+"/config.txt"):
        print(f"\n{Fore.GREEN}Found token from previous run.{Fore.RESET}")
        token = tokenf.read()
        break
    else:
        tokeni = input('> ')
        token = tokeni
        tokenf = open(filepath+"/config.txt", "w")
        tokenf.write(tokeni)
        print(f"\n{Fore.LIGHTBLUE_EX}Saving your token locally...{Fore.RESET}")
        break
tokenf.close()



#--------------------------------------------------------Discord client part of code--------------------------------------------------------#

#variables
intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)


#event that runs on the bot starting up
@client.event
async def on_ready():
    await tree.sync()
    print(f'{Fore.LIGHTBLUE_EX}Logged in as {client.user}')
    link = f"https://discord.com/oauth2/authorize?client_id={client.user.id}&permissions=8&scope=bot"
    print(f"\nHere's a link to invite your bot to your server. \n{Fore.CYAN}{link}")

#command to get your badge
@tree.command(name="start", description="Run this command to get your badge!")
async def start(interaction:discord.Interaction):
    await interaction.response.send_message(inspect.cleandoc(f""" 
                                                            Hello! {interaction.user} the command has been run.
                                                            Eligibility for the badge is checked every 24 hours so you need to wait until then to optain your badge.
                                                            
                                                            If it has already been 24h go to https://discord.com/developers/active-developer and fill out the requirements on the site.
                                                            
                                                            Again thank you for using my bot and have fun with your badge.
                                                            Please star my repository on Github and if you had any issues open a issue ticket."""))
    

#uses the token execute the command
client.run(token)
