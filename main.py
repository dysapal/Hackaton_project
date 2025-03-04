import discord
import random
import os
from discord.ext import commands
import requests
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='/', intents=intents)
from model import detect_problem
@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy el bot {bot.user}')
@bot.command()
async def bye(ctx):
    await ctx.send(f'Hasta luego, te veré después')
@bot.command()
async def funcion(ctx):
    await ctx.send(f'Bien, Si usas el comando <Identificar> y luego envias una imagen de elementos como desperdicio de agua o demas y te dire su definicion y como evitarlo')
@bot.command()
async def ja(ctx):
    await ctx.send(f"ja"*5)
@bot.command('Identificar')
async def Identificar(ctx):
    if ctx.message.attachments:
        for image in ctx.message.attachments:
            file_name = image.filename
            file_url = image.url
            await ctx.send(f"imagen guardada en{file_name}")
            await image.save(file_name)
            model = "keras_model.h5"
            labels = "labels.txt"
            image = file_name
            clase = detect_problem(model,labels,image)
            if clase[0] == "Contaminacion":
                await ctx.send(f"La contaminación ambiental ocurre cuando se liberan sustancias dañinas en el entorno, lo que deteriora el aire, el agua y el suelo, y afecta la salud humana y los ecosistemas.")
                await ctx.send(f"Para evitar la contaminación ambiental se debe reducir, reutilizar y reciclar; usar recursos de manera responsable; optar por transporte sostenible y energías renovables; evitar productos químicos tóxicos; promover la reforestación y fomentar la educación ambiental.")
            if clase[0] == "Incendios":
                await ctx.send(f"Un incendio es un fuego descontrolado que se propaga rápidamente, causando daño a materiales, propiedades y seres vivos, y puede ser causado por factores naturales o humanos.")
                await ctx.send("Para evitar los incendios, es clave apagar bien las fogatas, evitar cigarrillos en áreas secas, mantener el entorno limpio y seguir medidas de prevención, como usar extintores y respetar las prohibiciones de quema.")
            if clase[0] == "Desperdicio_alimentos":
                await ctx.send(f"Ocurre cuando las personas no consumen en su totalida sus alimentos y desechan la comida que todavia puede ser consumida")
                await ctx.send("Para evitarlo debemos asegurarnos de consumir todos los alimentos en su totalidad y si no sera asi hay q compartirlos.")
            if clase[0] == "Desperdicio_agua":
                await ctx.send(f"El desperdicio de agua es el uso innecesario o excesivo de este recurso, como dejar grifos abiertos o regar en exceso, lo que contribuye a su escasez.")
                await ctx.send("Para evitar el desperdicio de agua, se debe cerrar los grifos cuando no se usan, reparar fugas, usar dispositivos eficientes, regar en horarios adecuados y reciclar agua. Estas acciones ayudan a conservar este recurso.")
    else:
        await(ctx.send("no subiste imagen :("))


bot.run("Tu token")
