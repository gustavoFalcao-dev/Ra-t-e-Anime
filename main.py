import os
import discord
from dotenv import load_dotenv
from discord.ext import commands
from init_db import connectDB, createDatabase, databaseExists
import src.endpoint as ep
import src.embed as embed


#FIXME the bot may freeze with multiple commands because they shouldn't be asynchronous


load_dotenv()
bot_token = os.getenv("token") #Token to access the discord bot API
mal_token = os.getenv("MALToken") #Token to access the MAL API
db_path = os.getenv("DB_PATH") #Path used to create the database
prefix = "$" #For future use/testing
intents = discord.Intents.default() #Needed to give minimal permissions to the bot
intents.message_content = True #Needed so the bot can read users messages
bot = commands.Bot(command_prefix = prefix, intents = intents) #Variable containing the bot startup settings

#===========================================================================================
def set_con(): #Function to create database or connect if it already exists
	return (
		createDatabase(db_path) if not databaseExists(db_path) else connectDB(db_path)
	)

@bot.event
async def on_ready(): #Function to print a message showing which account the bot is logged on when booted
	print("We have logged in as {0.user}".format(bot))
#===========================================================================================
	
@bot.command()
async def setupdb(ctx):
	with set_con() as conn: #Calls the database creation function
		await ctx.send("Database setup complete.") #Sends a message confirming that it was created

async def animelist(ctx, username: str):
	data = ep.get_json(mal_token).user_list(username) #Stores the parsed list from MAL API on the variable
	print(username) #Used for testing
	print(data) #Used for testing
	print(type(data)) #Used for testing

async def anime(ctx, anime_id: int):
	data = ep.get_json(_, mal_token).anime_request(anime_id) #Stores the anime information in a parsed list
	print(type(data)) #Used for testing


bot.run(bot_token) #Boots the bot