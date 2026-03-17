import os
import discord
from dotenv import load_dotenv
from init_db import connectDB, createDatabase, databaseExists
import endpoint as ep

#TODO change nav to discord.ui instead of reactions listening

load_dotenv()
token = os.getenv("token")
username = os.getenv("testuser")
client_token = os.getenv("MALToken")
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
DB_PATH = "rat-e-anime.db"


def set_conn():
    return (
        createDatabase(DB_PATH) if not databaseExists(DB_PATH) else connectDB(DB_PATH)
    )


@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith("$hello"):
        await message.channel.send("Hello!")
    if message.content.startswith("$setupDB"):
        with set_conn() as conn:
            await message.channel.send("Database setup complete.")
    if message.content.startswith("$populateDB"):
        with connectDB(DB_PATH) as conn:
            with conn:
                cursor = conn.cursor()
                cursor.execute(
                    """
                    INSERT OR IGNORE INTO Anime (anime_id, anime_title, url_anime_main_picture, alternative_title_en, score)
                    VALUES (?, ?, ?, ?, ?)
                    """,
                    (
                        22199,
                        "Akame ga Kill!",
                        "https://myanimelist.net/images/anime/1429/95946.webp",
                        "Akame ga Kill!",
                        7.48,
                    ),
                )
        await message.channel.send("Banco de dados populado.")
    if message.content.startswith("$test"):
	    ep.user_list(username, client_token).teste()
	    await message.channel.send("Passed.")
    if message.content.startswith("$list"):
	    global msg_embed_id
	    users_reactions = ["🤡","😎"]
	    embed_users = discord.Embed(
	    	title = "Qual usuário?",
		description = "🤡 - GustaHawk\n😎 - Matheusinho",
		color = discord.Color.pink()
		)
	    msg_embed_users = await message.channel.send(embed=embed_users)
	    msg_embed_id = msg_embed_users.id
	    for emote in users_reactions:
		    await msg_embed_users.add_reaction(emote)
@client.event
async def on_reaction_add(reaction, user):
	global msg
	pages_reactions = ["◀️","▶️"]
	if user.bot:
		return
	if reaction.message.id != msg_embed_id:
		return
	if str(reaction.emoji) == "🤡":
	    pages_reactions = ["◀️","▶️"]
	    asw = ep.get_json(username, client_token).user_list()
	    node = asw["data"][0]["node"]
	    status = asw["data"][0]["list_status"]
	    embed = discord.Embed(
	    	title = node["title"],
		description = "Definetly a anime description",
		color = discord.Color.pink()
		)
	    embed.set_image(url=node["main_picture"]["large"])
	elif str(reaction.emoji) == "":
		embed = discord.Embed(
			title = "Calmai paizao",
			description = "É só um teste mano, nem tudo ta feito",
			color = discord.Color.pink()
			)
	await reaction.message.edit(embed=embed)
	await reaction.message.remove_reaction(reaction.emoji, user)
client.run(token)
