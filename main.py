from pathlib import Path
from typing import Sequence
import discord
from discord import Guild, Member, Message, utils, Embed, File
from discord import Intents, ActivityType, Activity
from discord.ext import commands
import datetime
import collections
import os

bot = commands.Bot(command_prefix='_', description='Bot de prueba', intents=Intents.all())
    
@bot.event
async def on_ready():
    await bot.change_presence(activity=Activity(type=ActivityType.watching))

EXTENSION_FILTER_SHEDULLE = {
    'excel':['xlsx', 'xlsm', 'xls', 'xlsb'],
    'img':['jpg', 'jpeg', 'png', 'bmp'],
}
CHANNELS_ID_SHEDULLE = {
    'horario': 1147750234290651196
}
@bot.event
async def on_message(message: Message):
    attachs = message.attachments
    channel = message.channel
    mess = channel.get_partial_message(1148052730712178738)
    file = File(Path("C:/Users/The Altro/Pictures/Screenshots/Captura de pantalla 2023-09-03 203436.png"))
    await mess.edit(attachments=[file])
    
    channels_id = list(CHANNELS_ID_SHEDULLE.values())
    exists = channel.id in channels_id
    if exists:
        if len(attachs)>0:
            for attach in attachs:
                _, extension = os.path(attach.filename)
                if extension not in EXTENSION_FILTER_SHEDULLE['excel']+EXTENSION_FILTER_SHEDULLE['img']:
                    message.remove_attachments(attach)
        if len(attachs)==0:
            await message.delete()
    
bot.run('MTE0Nzk3MDA5MTIyMTI1ODMxMA.GbHQC2.vLJK3aEbX_pBdOMTMwyakr7JQ9oP-g938sIwbI')
