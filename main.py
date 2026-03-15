import discord
from dotenv import load_dotenv
import os
#TODO Decidir banco de dados

load_dotenv()
token = os.getenv("token")
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
    if message.content.startswith('$test'):
        a = discord.Embed(title="Test anime", description="Test anime description", color=0xFFC0CB)
        a.set_image(url="https://a.storyblok.com/f/178900/1413x2000/7269083660/03610357ef4a76af4e984ed4bfc8680c1653890021_main.png/m/filters:quality(95)format(webp)")
        await message.channel.send(embed=a)

client.run(token)
