import os

import discord
from dotenv import load_dotenv

from init_db import connectDB, createDatabase, databaseExists

# TODO Decidir banco de dados

load_dotenv()
token = os.getenv("token")
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
    if message.content.startswith("$test"):
        a = discord.Embed(
            title="Test anime", description="Test anime description", color=0xFFC0CB
        )
        a.set_image(
            url="https://a.storyblok.com/f/178900/1413x2000/7269083660/03610357ef4a76af4e984ed4bfc8680c1653890021_main.png/m/filters:quality(95)format(webp)"
        )
        await message.channel.send(embed=a)
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


client.run(token)
