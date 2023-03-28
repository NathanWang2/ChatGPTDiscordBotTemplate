import discord
import os
from dotenv import load_dotenv
from ChatGPT import ChatGPT

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

# Creates an instance to use chatgpt
chat_gpt = ChatGPT()

# https://discordpy.readthedocs.io/en/stable/quickstart.html
# You need to enable messge_content in order to read and write to server
intents = discord.Intents.default()
intents.message_content = True

# Create a new Discord client
client = discord.Client(intents=intents)

# Define an event handler for when the bot is ready
@client.event
async def on_ready():
    print("Logged in as {0.user}.".format(client))

# Define an event handler for when the bot receives a message
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    await message.channel.send(chat_gpt.askChat(message.content))

    if message.content.startswith("!hello"):
        print("recieved this msg")
        await message.channel.send("Hello, world!")

if __name__ == "__main__":
    # Run the bot using a bot token
    client.run(TOKEN)