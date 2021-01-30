# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#
"""Userbot help command"""

import asyncio

from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern=r"^\.help(?: |$)(.*)")
async def help(event):
    """For .help command."""
    args = event.pattern_match.group(1).lower()
    if args:
        if args in CMD_HELP:
            msg = await event.edit(str(CMD_HELP[args]))
        else:
            msg = await event.edit("Please specify a valid module name.")
    else:
        head = "Tolong Sebutkan Module Nya Untuk Liat CMD nya !!"
        head2 = f"Module Aktip : {len(CMD_HELP)}"
        head3 = "Penggunaan: `.help` `<Nama Module>`"
        head4 = "Berikut List Module Yg Aktif: "
        string = ""
        sep1 = "`••••••••••••••••••••••••••••••••••••••••••••••`"
        sep2 = "`=========================================`"
        for i in sorted(CMD_HELP):
            string += "`" + str(i)
            string += "`  |  "
        await event.edit(
            f"{head}\
              \n{head2}\
              \n{head3}\
              \n{sep2}\
              \n{head4}\
              \n\n{string}\
              \n{sep1}"
        )
    await asyncio.sleep(40)
    await event.delete()
    ttry
        await msg.delete()
    except BaseException:
        return  # just# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#
""" Userbot help command """

import asyncio
from userbot import CMD_HELP
from userbot.events import register

modules = CMD_HELP


@register(outgoing=True, pattern="^.help(?: |$)(.*)")
async def help(event):
    """ For .help command,"""
    args = event.pattern_match.group(1).lower()
    if args:
        if args in CMD_HELP:
            await event.edit(str(CMD_HELP[args]))
        else:
            await event.edit("**Module Salah Goblokkkk!!**")
            await asyncio.sleep(18)
            await event.delete()
    else:
        await event.edit(f"**╭━━━━━━━━━━━━━━━━━━━━━╮**\
            \n│   Help for [🔥XBOT-REMIX🔥]\
            \n╰━━━━━━━━━━━━━━━━━━━━━╯ \
            \n╭━━━━━━━━━━━━━━━━━━━━━╮\
            \n│   Untuk melihat lengkap Command\
            \n│   Contoh: .help <nama module>\
            \n│   Modules Aktif: {len(modules)}\
           \n╰━━━━━━━━━━━━━━━━━━━━━╯")
        string = ""
        for i in CMD_HELP:
            string += "`" + str(i)
            string += "`\t• "
        await event.reply(f"•{string}•"
                          "\n╾─────────────────────╼")
        await asyncio.sleep(100)
        await event.delete() in case if msg deleted first
