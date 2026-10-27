import os
import random
import discord
from discord.ext import commands
from discord import app_commands
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('TOKEN_DISCORD')

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

@client.event
async def on_ready():
    print(f'Conectado como {client.user}')
    

class Botillo(discord.Client):
    async def setup_hook(self):
        await tree.sync()     

# Zona de comandos

@tree.command(name="haiii", description="si está vivo contesta, si no me temo que no está en este plano")
async def ping(interaction: discord.Interaction):
    if random.random() < 0.5:
        url = os.getenv('GIF_CAT_HAIII')
    else:
        url = os.getenv('GIF_CAT_FREAKY')
    await interaction.response.send_message("haiii :3")
    await interaction.followup.send(url)

# Coso que hace que se carguen los comandos slash

@client.event
async def on_connect():
    print("Conectandome al servidor :3")

@client.event
async def setup_hook():
    await tree.sync()
    print ("Comandos slash sincronizados :3")
    
if not TOKEN:
    raise RuntimeError("No se encontró el token de Discord. Asegúrate de tener un archivo .env con la variable TOKEN_DISCORD.")

client.run(TOKEN)
    
    
    
    