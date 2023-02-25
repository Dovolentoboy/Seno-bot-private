import disnake
import asyncio
from disnake.ext import commands
from pymongo import MongoClient
from asyncio import sleep
import datetime

cluster = MongoClient('mongodb+srv://Dovolentoboy:a600370@cluster0.6wxtw41.mongodb.net/test')
Warndb = cluster.Warndb
Warncoll =  Warndb.users


Economydb = cluster.ecodb
Economycoll = Economydb.users


Mutedb = cluster.Mutedb
Mutecoll = Mutedb.users


async def check_user_mute (ctx):
    await ctx.send ('Сочувствую вам , ведь вы хотите заткнуть рот самому себе/боту')
async def check_user_unmute (ctx):
    await ctx.send ('Нельзя открывать рот самому себе раньше времени')


class Mute_system(commands.Cog):    
    def __init__(self,bot):
        self.bot = bot 
        print('Module {} is loaded'.format(self.__class__.__name__))
    
    @commands.slash_command(name='mute')
    @commands.has_permissions(administrator=True)
    async def mute_system(self,ctx,member:disnake.Member,time = int(),reason = 'Не указана'):
        mute_role = disnake.utils.get(member.guild.roles,id=926527088985514084)
        if member and member.bot:
            return await check_user_mute(ctx)
        
        else :
            Mutecoll.update_one(
                {
                '_id':member.id
                },
                {
                '$inc':{
                    'mutes':1
                }
                }
            )
            Mutecoll.update_one(
                {
                '_id':member.id
                },
                {
                '$push':{
                    'reason':{
                        'reason':reason
                    }
                }
                }
            )
            embed =disnake.Embed(
                    title='Выдача мута',
                    description=f'Пользователь {ctx.author.mention} получает мут на {time} минут по причине {reason}'
                )
            await ctx.send (embed=embed)
            await member.add_roles(mute_role)
            await asyncio.sleep(time*60)
            await member.remove_roles(mute_role)    
            await member.send(embed=embed)
    

    @commands.slash_command(name='unmute',description='Снятие мута')
    @commands.has_permissions(administrator=True)
    async def unmute(self,ctx,member:disnake.Member):
        if member and member.bot:
            return await check_user_unmute(ctx)
        else:
            embed = disnake.Embed(
                title='Система мута',
                description='С вас был снят мут. Продолжайте общение!'
            )
            mute_role = disnake.utils.get(member.guild.roles,id=926527088985514084)
            await member.remove_roles(mute_role)
            await member.send(embed=embed)
    


    



def setup(bot):
    bot.add_cog(Mute_system(bot))
                
            
        
        

        

        