import random, os, time, datetime, requests, pytz
from pyrogram import *
from pyrogram.types import *
from pyrogram.raw import *

api_id = 1 # api id
api_hash = "" # api hash
kattobot = "" # token del bot

# messaggi katto
kattostart = """
Miao, sono Katto 😼!
Mi reputo un tipo semplice, mangio cibo per gatti e fumo erba...
"""

kattoaggiunto = "" # messaggio di quando katto viene aggiunto al gruppo
comandimsg = """
<b>LISTA COMANDI</b>
Pagina: 1

Oki
Aiuto, Affondo
Amici Di Katto
Bambini
Don Gino
Pedofilo
Stonks
Scusate, mi è scappato

Comandi totali: 8

<b>Vuoi suggerire un comando?
Visita [Il mio sito web!](https://t.me/AnimeCommunityGruppo)</b>
"""
funzionimsg = """
<b>LISTA FUNZIONI</b>

/chatid: Visualizza ID Chat.

/userid (in reply): Visualizza ID Utente.

/myid: Visualizza Tuo ID

/random: genera un numero random

Dado: Lancia un Dado.

Lancia Una Moneta: Testa o Croce

Katti: Foto Di Gatti Casuali
"""

# inlinekatto
btnkattostart = InlineKeyboardMarkup([[InlineKeyboardButton("🔉 Canale", url="www.test.com"), InlineKeyboardButton("👥 Gruppo", url="www.test.com")], [InlineKeyboardButton("🎛 Comandi ", "cmd"), InlineKeyboardButton("📂 Funzioni", "funzioni")], [InlineKeyboardButton("➕ Aggiungi ad un gruppo", url="wwww.test.com")]])
btnindietrokatto = InlineKeyboardMarkup([[InlineKeyboardButton("🔙 Indietro", "home")]])
katto = Client('katto', api_id, api_hash, bot_token=kattobot)

@katto.on_message(filters.private & filters.command("start"))
async def start(client, message):
    await client.send_message(message.chat.id, kattostart, reply_markup=btnkattostart)

@katto.on_message(filters.private & filters.command("random"))
async def generanumero(client, message):
    generato = random.randint(1, 999999)
    await client.send_message(message.chat.id, f"il tuo numero: {generato}")


@katto.on_message(filters.command("myid"))
async def myid(client, message):
    await message.reply(f"TUO ID > {message.from_user.id}")

@katto.on_message(filters.command("userid"))
async def userid(client, message):
    if message.reply_to_message:
        await message.reply(f"ID > {message.reply_to_message.from_user.id}")
    else:
        await message.reply("comando in reply!")

@katto.on_message(filters.group & filters.channel & filters.command("chatid"))
async def chatid(client, message):
    await message.reply(f"CHATID > {message.chat.id}")

@katto.on_message(filters.new_chat_members)
async def welcome(client, message):
    for user in message.new.chat_members:
        if user.is_self:
            await client.send_message(kattoaggiunto)
        else:
            try:
                await client.get_chat_member(message.from_user.id)
            except:
                kattowelcome = random.choice([f"è entrato un bellissimo utente il suo nome è {message.from_user.mention}", f"🎉 {message.from_user.mention} partecipa alla festa!", f"😼 Dato il benvenuto a {message.from_user.mention} stronzi"])
                await client.send_message(message.chat.id, kattowelcome)

@katto.on_message(filters.text)
async def kattorispondi(kattoclient: Client, kattoso: types.Message):
    if kattoso.text.lower() == "oki":
        await kattoso.reply("Oh oh oh, oki di kattooo")
    elif kattoso.text.lower() == "Aiuto, Affondo":
        await kattoso.reply("Nooo, resta a galla, perfavore!")
    elif kattoso.text.lower() == "Amici Di Katto":
        await kattoso.reply("Solo @ChillatoDev.\nSono asociale, d'altronde, tale padre tale figlio!")
    elif kattoso.text.lower() == "Bambini":
        await kattoso.reply("Li vendo! 20 Euro/KG...")
    elif kattoso.text.lower() == "Don Gino":
        await kattoso.reply("Lo conosco, mi regala le caramelle in cambio di bimbe 2007+")
    elif kattoso.text.lower() == "Pedofilo":
        await kattoso.reply("Oh mio dio, ma stai parlando di me!")
    elif kattoso.text.lower() == "Stonks":
        await kattoso.reply("Chromostonks*")
    elif kattoso.text.lower() == "Scusate, mi è scappato":
        await kattoso.reply("attaccalo meglio, cojone")
    elif kattoso.text.lower() == "dado":
        await kattoclient.send_dice(kattoso.chat.id)
    elif kattoso.text.lower() == "lancia una moneta":
        await kattoso.reply(f"è uscito "+ random.choice(["👨🏻‍🦰", "❌"]))
    elif kattoso.text.lower() == "katti":
        kattsite = requests.get("https://cataas.com/cat?json=true")
        kattii = kattsite.json()
        await kattoso.reply_photo(f"https://cataas.com/{kattii.get('url')}")
    elif kattoso.text.lower() == "ciao":
        if kattoso.from_user.username:
            utente = "@" + f"{kattoso.from_user.username}"
        else:
            utente = "NESSUN USERNAME"
        await kattoso.reply(f"ciao {utente}")

@katto.on_callback_query()
async def bottone(client, query):
    if query.data == "cmd":
        await query.message.edit(comandimsg, reply_markup=btnindietrokatto)
    elif query.data == "funzioni":
        await query.message.edit(funzionimsg, reply_markup=btnindietrokatto)
    elif query.data == "home":
        await query.message.edit(kattostart, reply_markup=btnkattostart)




katto.run()
