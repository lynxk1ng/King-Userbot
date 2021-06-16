from platform import uname
from time import sleep
from userbot import ALIVE_NAME, CMD_HELP
from userbot.events import register

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern="^.P(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`Assalamu'alaikum...`")


@register(outgoing=True, pattern=r"^\.p(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`Assalamu'alaikum...`")


@register(outgoing=True, pattern="^.Ass(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit(f"**Halo bro saya {DEFAULTUSER} salam kenal 😁**")
    sleep(2)
    await typew.edit("`Assalamualaikum Waruhmatulahi Wabarukatuh...`")


@register(outgoing=True, pattern="^.Waa(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**iyaa bro**")
    sleep(2)
    await typew.edit("`Walaikumsalam Waruhmatulahi Wabarukatuh...`")


@register(outgoing=True, pattern="^.L(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`Wa'alaikumsalam...`")


@register(outgoing=True, pattern=r"^\.l(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`Wa'alaikumsalam...`")


@register(outgoing=True, pattern=r"^\.Wibu(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`Tidak, Ada Wibu😱`")
    
    await typew.edit("`Sekuat Apapun aku jika Bertemu Wibu Aku harus Lari`")
    
    await typew.edit("`Kita Harus Berlari Dari Wibu Karena Wibu Adalah Ras Terkuat diBumi`")
    
    await typew.edit("`Lari... Ada Wibu Nolep🏃🏃`")


CMD_HELP.update(
    {
        "salam": "**✘ Plugin : **`salam`\
        \n\n  •  **Perintah :** `.P` | `.p`\
        \n  •  **Function :** Untuk salam ke semua orang\
        \n\n  •  **Perintah :** `.Ass`\
        \n  •  **Function :** Salam kenal dan salam\
        \n\n  •  **Perintah :** `.Waa`\
        \n  •  **Function :** Menjawab salam panjang\
        \n\n  •  **Perintah :** `.L` | `.l`\
        \n  •  **Function :** Untuk menjawab salam\  
    "   \n\n  •  **Perintah :** `.Wibu` | `.wibu`\
    }   \n  •  **Function :** Berisi pesan untuk wibu\
)
