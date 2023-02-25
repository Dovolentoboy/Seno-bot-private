import disnake
from disnake.ext import commands
from pymongo import MongoClient

cluster = MongoClient(LINK)
Localbandb = cluster.Localban
Localbancoll = Localbandb.users


class Localban_system(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        print('Module {} is loaded'.format(self.__class__.__name__))



    @commands.slash_command(name='localban',description='Выдача локальной блокировки')
    @commands.has_permissions(administrator=True)
    async def localban(self,ctx,member:disnake.Member,reason = 'Не указана'):
        if member and member.bot:
            return await ctx.send('Вы не можете прописать наказание себе/боту')
        else :
            embed = disnake.Embed(
                title='Выдача локальной блокировки',
                description=f'{ctx.author.mention} получает локальную блокировку по причине {reason}'
            )
            role = disnake.utils.get(member.guild.roles,id=1068879473107271720)
            Localbancoll.update_one(
                {
                '_id':member.id,
                
                },
                {
                '$inc':{
                    'localban':1
                }
                },
                
            )
            Localbancoll.update_one(
                {
                '_id':member.id
                },
                {
                '$push':{
                    'reason':reason

                }
                }
            )
            ls_embed = disnake.Embed(
                title='Локальная блокировка',
                description=f'Вам была выдана локальная блокировка по причине : {reason}\n'
                            'Если вы считаете ,что блокировка ошибочная обращаться к <@839490293447524384>|Dovolen toboy#9956',
                            color=disnake.Color.from_rgb(47,50,55)
            )
            await member.send(embed=ls_embed)
            await member.add_roles(role)
            await ctx.send(embed=embed)

    @commands.slash_command(name='unlocalban',description='Выдача локальной блокировки')
    @commands.has_permissions(administrator=True)
    async def unlocalban(self,ctx,member:disnake.Member):
        if member and member.bot:
            return await ctx.send('Вы не можете прописать помилование себе/боту')
        role = disnake.utils.get(member.guild.roles,id=1068879473107271720)
        embed = disnake.Embed(
            title='Снятие локальной блокировки',
            description=f'С пользователя {member.mention} была снята локальная блокировка',
            color=disnake.Color.from_rgb(47,50,55)
        )
        ls_embed = disnake.Embed(
                title='Локальная блокировка',
                description=f'С вас была снята локальная блокировка\n'
                            'Хорошего вам общения на сервере!',
                            color=disnake.Color.from_rgb(47,50,55))
        await member.send(embed=ls_embed)
        await member.remove_roles(role)
        await ctx.send(embed=embed)



def setup(bot):
    bot.add_cog(Localban_system(bot))
