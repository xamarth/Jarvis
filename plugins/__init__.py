# Jarvis - Userbot

import asyncio
import os
import time
from random import choice

import requests
from telethon import Button, events
from telethon.tl import functions, types  # pylint:ignore

from pyCore import *
from pyCore._misc._assistant import asst_cmd, callback, in_pattern
from pyCore._misc._decorators import jarvis_cmd
from pyCore._misc._wrappers import eod, eor
from pyCore.dB import DEVLIST, JARVIS_IMAGES
from pyCore.fns.helper import *
from pyCore.fns.misc import *
from pyCore.fns.tools import *
from pyCore.startup._database import _BaseDatabase as Database
from pyCore.version import __version__, jarvis_version
from strings import get_help, get_string
from pyCore.fns.FastTelethon import upload_file

udB: Database

Redis = udB.get_key
con = TgConverter
quotly = Quotly()
OWNER_NAME = jarvis_bot.full_name
OWNER_ID = jarvis_bot.uid

jarvis_bot: JarvisClient
asst: JarvisClient

LOG_CHANNEL = udB.get_key("LOG_CHANNEL")

def inline_pic():
    INLINE_PIC = udB.get_key("INLINE_PIC")
    if INLINE_PIC is None:
        INLINE_PIC = choice(JARVIS_IMAGES)
    elif INLINE_PIC == False:
        INLINE_PIC = None
    return INLINE_PIC


Telegraph = telegraph_client()

List = []
Dict = {}
InlinePlugin = {}
N = 0
cmd = jarvis_cmd
STUFF = {}

# Chats, which needs to be ignore for some cases
# Considerably, there can be many
# Feel Free to Add Any other...

NOSPAM_CHAT = [
    -1001109500936,  # TelethonChat
    -1001050982793,  # Python
    -1001256902287,  # DurovsChat
    -1001473548283,  # SharingUserbot
]

KANGING_STR = [
    "Using Witchery to kang this sticker...",
    "Plagiarising hehe...",
    "Inviting this sticker over to my pack...",
    "Kanging this sticker...",
    "Hey that's a nice sticker!\nMind if I kang?!..",
    "Hehe me stel ur stiker...",
    "Ay look over there (☉｡☉)!→\nWhile I kang this...",
    "Roses are red violets are blue, kanging this sticker so my pack looks cool",
    "Imprisoning this sticker...",
    "Mr.Steal-Your-Sticker is stealing this sticker... ",
]

ATRA_COL = [
    "DarkCyan",
    "DeepSkyBlue",
    "DarkTurquoise",
    "Cyan",
    "LightSkyBlue",
    "Turquoise",
    "MediumVioletRed",
    "Aquamarine",
    "Lightcyan",
    "Azure",
    "Moccasin",
    "PowderBlue",
]
