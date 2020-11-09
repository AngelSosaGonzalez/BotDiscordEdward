#Importaremos el modulo de discord
import discord

#Como su nombre lo dice exportaremos los comandos
from discord.ext import commands

#Importamos TimeStamp (NO ES OBLIGATORIO)
import datetime


"""NOTA PARA EL DESARROLLADOR, toda funcion de evento o comando se debe
de ejecutar en forma de Corutina, para esto se debe realizar de la siguiente
manera: async def on_ready():, usar siempre async"""

#Ya importado los modulos necesarios, vamos con la carnita
Edward = commands.Bot(command_prefix='-', description='Hola soy Edward tu Bot de Cabecera')
"""El comando_prefix es la inicial de como llamaremos a nuestros comandos
lo normal es que sea un caracter que se use muy a seguido, este proyecto se usara "-" """

#Crearemos nuestro primer comando
@Edward.command()

#El nombre del comando lo definiremos con el nombre de esta funcion
#usaremos primeramente el comando help, porque pues este dara todos los demas comandos que hagamos

async def ed(ctx):
    #Aqui se enviara el mensaje
    #await son para las corutinas de las acciones que hara nuestro bot 
    await ctx.send('Hola soy Edward tu Bot de Cabecera')

#Comando de informacion
#Mostrara el nombre del servidor, un mensajito y la fecha
#pero no solo eso le pondremos color
@Edward.command()
async def info(ctx):
    embed = discord.Embed(title=f"{ctx.guild.name}", description="Hola, bienvenido al servidor", timestamp=datetime.datetime.utcnow(), color=discord.Color.dark_magenta())
    #informacion de la creacion del servidor
    embed.add_field(name='Este servidor de creo en: ', value=f'{ctx.guild.created_at}')
    
    #Informacion del creador (en este caso soy yo)
    embed.add_field(name='El creador del servidor es: ', value=f'{ctx.guild.owner}')
   
    #ID del servidor
    embed.add_field(name='ID del servidor: ', value=f'{ctx.guild.id}')

    #Informacion de la region
    embed.add_field(name='El servidor se creo en: ', value=f'{ctx.guild.region}')
    
    #Mostrar el logo del servidor
    #la url es de una imagen sacada de internet, pero siquiere agregar la del servidor usa:
    #"{ctx.guild.icon}" 
    embed.set_thumbnail(url='https://instagram.fmex5-1.fna.fbcdn.net/v/t51.2885-19/s150x150/91072421_517258895657525_1025869130676305920_n.jpg?_nc_ht=instagram.fmex5-1.fna.fbcdn.net&_nc_ohc=q5A_YZMFBk0AX-nfqlf&oh=4e411537cbca8c5b90afa3b53acd932d&oe=5FD3312B')

    #SI QUIERES MOSTRAR MAS DATOS DEL SERVIDOR, VEA LA DOCUMENTACION (EL LINK ESTE EN EL README)

    await ctx.send(embed=embed)


#Ahora vamos a crear Eventos
#Vamos a crear un evento de arranque
@Edward.event
async def on_ready():
    
    #Si tienes canal de Strings (Streaming, pues...) configuraremos el estado
    #mostrando basicamente que el bot muestre que se esta stremeando 
    #para este ejemplo usaremos twitch (bueno... solo se pude twitch)
    select = input('¿Haras streaming hoy? S/N: \n')
    if select.upper() == 'S':
        Game = input('\nDime, ¿Que juego jugaremos hoy?: \n')
        #Preguntamos el juego
    
        Twitch = input('\nWow, jugaras {}, ahora dame la URL de tu canal (URL, porfa, no me lo hagas dificil): \n'.format(Game))
        #Preguntamos el canal

        await Edward.change_presence(activity=discord.Streaming(name=Game, url=Twitch))
        #Este es le proceso para el estado del Bot

        #Daremos un mensaje de aviso, para verificar si el Bot esta en linea
        print('\nYa inicio este pinche PEDOOO!!!') 

    else:
        #Daremos un mensaje de aviso, para verificar si el Bot esta en linea
        print('\nYa inicio este pinche PEDOOO!!!') 

    
#Vamos a correr a Edward
Edward.run('*Key de Discord*')