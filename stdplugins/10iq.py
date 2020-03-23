from os import remove
from os import execl
import sys

from git import Repo
from git.exc import GitCommandError, InvalidGitRepositoryError, NoSuchPathError

# from uniborg import CMD_HELP, bot
# from uniborg.events import register


import asyncio
import random
import re
import time

from collections import deque

import requests

from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import MessageEntityMentionName
from telethon import events

from uniborg.util import admin_cmd

@borg.on(admin_cmd(pattern="10iq ?(.*)", outgoing=True))
async def iqless(e):
    await e.edit("DÜÜÜT DÜÜÜTT AÇ YOLU AÇÇ HADİ ASLAN PARÇASI YOLU AÇ HADİ BAK ENGELLİ BEKLİYO BURDA HADİ DÜÜÜTTT ♿️ BAK SİNİRLENDİ ARKADAŞ HADİ YOLU AÇ HADİİ DÜÜÜT DÜÜTT BİİİPP HADİ BE HIZLI OLL DÜÜÜTT BİİİPPP ♿️♿️ BAK HIZLANDI ENGELLİ KARDEŞİMİZ SERİ KÖZ GETİR SERİ DÜÜÜTT DÜÜÜT DÜÜÜÜTTTTT BİİİİPPP BİİİİİPPP DÜÜÜTTT ♿️♿️♿️♿️ BAK ARTIYO SAYILARI AÇTIN MI YOLU AÇMADIN PÜÜÜÜ REZİİİLL DÜÜÜÜTTT ♿️♿️♿️♿️♿️♿️ BAK KALABALIKLASTI BAK DELI GELIYOR DELIRDI DELI AC YOLU DUTDUTDURURURUDUTTT♿️♿️♿️♿️♿️♿️♿️♿️♿️♿️♿️♿️♿️♿️KAFAYI YEDI BUNLAR AC LAAAAN YOLU")