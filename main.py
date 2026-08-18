import discord
from discord.ext import commands
from logic_analistic import *
import requests

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print("Estamos aqui para cuidar el medio ambiente.")

@bot.command()
async def consejo(ctx):
    await ctx.send(ayuda())

def duck_image():
    url = "https://random-d.uk/api/random"
    res = requests.get(url)
    data = res.json()
    return data["url"]

@bot.command('pato')
async def pato(ctx):
    image_url = duck_image()
    await ctx.send("Mira! *señala un pato*")
    await ctx.send(image_url)

@bot.command()
async def recicla(ctx):
    await ctx.send("Para reciclar tendremos que usar material que aun se pueda usar y que no sea organico preferiblemente. Se reutiliza y puede usarse para hacer manualidades DIY")

@bot.command()
async def naturaleza(ctx):
    await ctx.send("El aire esta tan contaminado que tiene una composición de:")
    await ctx.send("1. Nitrógeno (78%)")
    await ctx.send("2. Oxígeno (21%)")
    await ctx.send("3. Argón y otros (1%)")

@bot.command()
async def agua(ctx):
    await ctx.send("Cuida el agua lo más que puedas...**si se acaba ya no hay reemplazo**")

bot.run("Token Example")
