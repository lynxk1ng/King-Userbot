# ©Copyright King-Userbot (Apis) USERBOT TELEGRAM
# Ported by Apis
# Thanks for ultroid
# Thanks for ᴀxᴇʟ.ᴀʟ/ᴄᴏɴᴛʀɪʙᴜᴛᴏʀ

from userbot.events import register
from userbot import CMD_HELP, bot


@register(outgoing=True, pattern="^.gcast (.*)")
async def gcast(event):
    kinguser = event.pattern_match.group(1)
    if not kinguser:
        return await event.edit("`Kasi Pesan yg mau lu kirim secara global tod`")
    tt = event.text
    msg = tt[6:]
    kingget = await event.edit("`Lagi ngirim pesan ke semua gc yg lu gabung...`")
    er = 0
    done = 0
    async for x in bot.iter_dialogs():
        if x.is_group:
            chat = x.id
            try:
                done += 1
                await bot.send_message(chat, msg)
            except BaseException:
                er += 1
    await kingget.edit(f"**Berhasil ngirim Pesan lu Tod Ke** `{done}` **Grup, Maaf Tod lu gagal ngirim Pesan Ke** `{er}` **Grup**")


@register(outgoing=True, pattern="^.gucast (.*)")
async def gucast(event):
    kinguser = event.pattern_match.group(1)
    if not kinguser:
        return await event.edit("`Kasi pesan Yang mau lu kirim tod`")
    tt = event.text
    msg = tt[7:]
    kingget = await event.edit("`Lagi ngirim pesan PC global..... Sabar Tod...`")
    er = 0
    done = 0
    async for x in bot.iter_dialogs():
        if x.is_user and not x.entity.bot:
            chat = x.id
            try:
                done += 1
                await bot.send_message(chat, msg)
            except BaseException:
                er += 1
    await kingget.edit(f"**Berhasil ngirim Pesan Tod Ke** `{done}` **Orang, Gagal ngirim Pesan lu tod Ke** `{er}` **Orang.**")


CMD_HELP.update(
    {
        "gcast": "**✘ Plugin : **`Global Broadcast`\
        \n\n  •  **Perintah :** `.ggcast` <Text>`\
        \n  •  **Function : **Global Group Broadcast. Mengirim Pesan Global Broadcast pesan ke Seluruh Grup Yang lu Masuki\
        \n\n  •  **Perintah :** `.gucast` <Text>`\
        \n  •  **Function : **Global Users Broadcast. Kirim Pesan itu Secara Global ke Semua memb Group Anda\
     "
    }
)
