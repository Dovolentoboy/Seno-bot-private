import disnake
from disnake.ext import commands
import os
from pymongo import MongoClient
from config import Token

cluster = MongoClient(')
db = cluster['ecodb']
collection = db['users']
db2 = cluster['Warndb']
collection2 = db2['users']

bot = commands.Bot(command_prefix='.',intents=disnake.Intents.all())








@bot.event 
async def on_ready():
    print(f"Bot {bot.user.name} Работает!", bot.user)
    await bot.change_presence(status=disnake.Status.online,activity=disnake.Game(name='Dovolen toboy самый пиздатый создатель'))
    for guild in bot.guilds:
            for member in guild.members:
                post = {
                    '_id':member.id,
                    'balance':0,
                    'lvl':0,
                    'xp':0

            }
            if collection.count_documents({'_id':member.id}) == 0:
                collection.insert_one(post)
            

            for guild in bot.guilds:
                for member in guild.members:
                    value = {
                        '_id':member.id,
                        'warns':0,
                        'reason':[]
                    }
                    if collection2.count_documents({'_id':member.id}) == 0:
                        collection2.insert_one(value)
        
        
                
    
    

    
            

@bot.event
async def on_member_join(self,ctx,member):
        for guild in bot.guilds:
            for member in guild.members:
                post = {
                    '_id':member.id,
                    'balance':0,
                    'lvl':0,
                    'xp':0

            }
            if collection.count_documents({'_id':member.id}) == 0:
                collection.insert_one(post)
            

            for guild in bot.guilds:
                for member in guild.members:
                    value = {
                        '_id':member.id,
                        'warns':0,
                        'reason':[]
                    }
                    if collection2.count_documents({'_id':member.id}) == 0:
                        collection2.insert_one(value)
                        
        embed=disnake.Embed(
            title='Новый участник',
            description=f'{member.mention} Добро пожаловать на сервер! Прежде чем общаться прочтите правила и пройдите верификацию',
            color=disnake.Color.from_rgb(47,50,55)
            )
        url = 'https://tenor.com/ru/view/welcome-gif-20647847'
        embed.set_image(url=url)
        role = disnake.utils.get(member.guild.roles,id=1068443146586947634) #личка
        await member.send (embed=embed)
        await member.add_roles(role)
        
        
        
                
        

            
@bot.slash_command()
async def load(ctx, *, extension):
    if str(ctx.author.id) != "839490293447524384":
        return await ctx.send('У вас недостаточно прав!')
    try:
        bot.load_extension(f'cogs.{extension}')
        await ctx.send(f'{extension} перезагружен')
    except Exception as e:
        await ctx.send(e)


@bot.slash_command()
async def unload(ctx, *, extension):
    if str(ctx.author.id) != "839490293447524384":
        return await ctx.send('У вас недостаточно прав!')
    try:
        bot.unload_extension(f'cogs.{extension}')
        await ctx.send(f'{extension} неактивен')
    except Exception as e:
        await ctx.send(e)
    



for filename in os.listdir("./cogs"):
    if filename.endswith(".py") and not filename.startswith("_"):
        bot.load_extension(f"cogs.{filename[:-3]}")


        

bot.run(Token) 
    









