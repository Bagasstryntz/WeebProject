from time import sleep
from platform import uname
from userbot import ALIVE_NAME, CMD_HELP
from userbot.events import register

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern='^A(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit(f"**Hallo Semua Saya {DEFAULTUSER}**")
    sleep(2)
    await typew.edit("`Assalamualaikum.....`")
# Owner @Si_Dian


@register(outgoing=True, pattern='^a(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit(f"**Hallo Semua Saya {DEFAULTUSER}**")
    sleep(2)
    await typew.edit("`Assalamualaikum.....`")
# Owner @Si_Dian


@register(outgoing=True, pattern='^W(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("`Astaghfirulloh Jawab Salam Dong...`")
    sleep(1)
    await typew.edit("`Waallaikumsalam......`")
# Owner @Si_Dian


@register(outgoing=True, pattern='^w(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("`Astaghfirulloh Jawab Salam Dong...`")
    sleep(1)
    await typew.edit("`Waallaikumsalam.....`")
# Owner @Si_Dian


CMD_HELP.update({
    "salam":
    "`A`\
\nUsage: Untuk Memberi salam.\
\n\n`W`\
\nUsage: Untuk Menjawab Salam."
})
