import disnake 
import asyncio
from disnake.ext import commands
from pymongo import MongoClient
from asyncio import sleep



cluster = MongoClient(Link)
db = cluster.Warndb
collusers = db.users
collservers = db.Collservers




async def check_user(ctx):
    embed=disnake.Embed(

        color=disnake.Color.from_rgb(47,50,55),
            description="Нельзя выдать наказание/помилование самому себе. А ты что хотел? Такова участь модератора))) ",
                title='Ошибка применения команды'
    )    
    await ctx.send(embed=embed)

class Warn_system(commands.Cog):    
    def __init__(self,bot):
        self.bot = bot 
        print('Module {} is loaded'.format(self.__class__.__name__))
        
        


    @commands.slash_command(name='warn',description='Выдать предупреждение')
    @commands.has_permissions(administrator=True)
    async def warn(self,ctx,member:disnake.Member,*,reason='Не указана'):
        if member == ctx.autho or member == member.bot or member is None:
            return await check_user(ctx)
        time = int(1*42000)
        if collusers.find_one({'_id':member.id})['warns'] >= 3:
            collusers.update_one(
                {
                '_id':member.id
                },
                {
                '$set': {
                    'warns':0,
                        'reason':[]
                }
                }
               
                
            )
            embed = disnake.Embed(
                title='Выдать предупреждение',
                description=f'Пользователь {ctx.author.mention} выдал финальное предупреждение для пользователя {member.mention}\n'
                            f'Причина : **{reason}**.\n'
                            f'Наказание : 12 часов мута',
                color=disnake.Color.from_rgb(47,50,55)
            )
            ls_embed=disnake.Embed(
                title='Предупреждение',
                description=f'Вам было выдано финальное предупреждение по причине: **{reason}**',
                color=disnake.Color.from_rgb(47,50,55))
            ls_embed.add_field(name='**Наказание:**',value='12 часов мута')
            mute = disnake.utils.get(member.guild.roles,id=926527088985514084)
            await member.add_roles(mute)
            await ctx.send(embed=embed)
            await member.send(embed = ls_embed)
        else:
            collusers.update_one(
                {
                '_id':member.id
                },
                {
                '$inc': {
                    'warns':1
                    
                }
                }
            )

            collusers.update_one(
                {
                '_id':member.id
                },
                {
                "$push":
                    {
                        "reason":{
                            "author_id":ctx.author.id,
                            'reason':reason

                        }

                    }
                }
            )   
            embed = disnake.Embed(
                    title='Выдать предупреждение',
                    description=f'Пользователь {ctx.author.mention} выдал предупреждение пользователю {member.mention}\n'
                    f'Причина : **{reason}**'
                )
            await ctx.send (embed=embed)
            embed=disnake.Embed(
                title='Предупреждение',
                description=f'Вам было выдано предупреждение по причине: **{reason}**',
                color=disnake.Color.from_rgb(47,50,55)
            )
            await member.send(embed=embed)



    @commands.slash_command(name='unwarn',description='Снять предупреждение с пользователя')
    @commands.has_permissions(administrator=True)
    async def unwarn(self,ctx,member:disnake.Member):
        if collusers.find_one({'_id':member.id})['warns'] ==0:
            embed= disnake.Embed(
                title='Снять предупреждение',
                description=f'Пользователь {member.mention} не имеет предупреждений',
                color=disnake.Color.from_rgb(47,50,55)
            )
            await ctx.send (embed=embed)
        else:
                collusers.update_one(
                    {
                    '_id':member.id
                    },
                    {
                    '$inc': {
                        'warns': -1
                    }
                    }
                )
                collusers.update_one(
                    {
                    '_id':member.id
                    },
                    {
                    '$pull':{
                        'reason'
                        'author_id':ctx.author.id
                    }
                    }
                )
                embed = disnake.Embed(
                    title='Снять предупреждение',
                    description=f'Пользователь {ctx.author.mention} снимает предупреждение с пользователя {member.mention}',
                    color=disnake.Color.from_rgb(47,50,55)
                )
                ls_embed = disnake.Embed(
                    title='Предупреждения',
                    description='С вас снято предупреждение',
                    color=disnake.Color.from_rgb(47,50,55)
                )
                
                await ctx.send(embed=embed)
                await member.send(ls_embed)

    @commands.slash_command(name='viewwarns',description='Просмотреть свои предупреждения')
    async def view_warns(self,ctx,member:disnake.Member = None):
        if member is None:
            embed = disnake.Embed(
                    title='Ваши предупреждения',
                    description=f'Ваши предупреждения: **{collusers.find_one({"_id":ctx.author.id})["warns"]}**\n',
                    color=disnake.Color.from_rgb(47,50,55)
                )
            await ctx.send(embed=embed)
        else:
            embed = disnake.Embed(
                    title=f'Предупреждения пользователя {member.mention}',
                    description=f'Предупреждения: **{collusers.find_one({"_id":member.id})["warns"]}**\n',
                    color=disnake.Color.from_rgb(47,50,55)
                    )
            await ctx.send (embed=embed)
        
                
                
                

            


def setup (bot):
    bot.add_cog(Warn_system(bot))
