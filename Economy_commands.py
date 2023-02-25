import disnake
from disnake.ext import commands
from pymongo import MongoClient

cluster = MongoClient('LINK')
db = cluster['ecodb']
collection = db['users']


class Economy_system (commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        print('Module {} is loaded'.format(self.__class__.__name__))


    @commands.command(name='Balance',aliases = ['bal','balance','баланс','cash'])
    @commands.has_any_role('🛡️участники')
    async def balance(self,ctx,member:disnake.Member=None):
        if member is None:
            embed = disnake.Embed(
                title='Баланс',
                description=f"Ваш баланс 💵 : ```{collection.find_one({'_id':ctx.author.id})['balance']}```"
            )
            await ctx.send (embed=embed)
        else:
            embed = disnake.Embed(
            title='Баланс',
            description=f"Баланс 💵 пользователя {member.mention}\n ```{collection.find_one({'_id':member.id})['balance']}```")
            await ctx.send (embed=embed)

    @commands.command(name='pay',aliases = ['Перевод', 'transfer','транзакция','пэй'])
    async def pay(self,ctx,member:disnake.Member,count = int()):
        if collection.find_one({'_id':member.id})['balance'] < count:
            await ctx.send ('Вы слишком бедны для этого')
        else :
            collection.update_one(
                {
                '_id':ctx.author.id
                },
                {
                '$set':{
                    'balance': +count
                }
                }
            )
            collection.update_one(
                {
                '_id':member.id
                },
                {
                '$set':{
                    'balance': -count
                }
                }
            )
            await ctx.send (f'{ctx.author.mention} перевел {count} 💵 денег пользователю {member.mention} ')
            await member.send (f'Пользователь {ctx.author.mention} перевел вам {count} 💵 денег')

    @commands.command(name='set',aliases = ['установить'])
    @commands.has_permissions(administrator=True)
    async def set_balance (self,ctx,member:disnake.Member=None,count = int()):
        if member is None:
            collection.update_one(
                {
                '_id':ctx.author.id
                },
                {
                '$set':{
                    'balance': +count
                }
                }
            )
            await ctx.send (f"Пользователю {ctx.author.mention} установлено значение баланса : **{collection.find_one({'_id':member.id})['balance']}** ")
        else:
            collection.update_one(
                {
                '_id':member.id
                },
                {
                '$set':{
                    'balance': +count
                }
                }
            )
            await ctx.send (f"Пользователю {member.mention} установлено значение баланса : **{collection.find_one({'_id':member.id})['balance']}** ")

    @commands.command(name='pay',aliases = ['перевод','transfer'])
    async def pay (self,ctx,member:disnake.Member,count = int()):
        if member == ctx.author or member is None or member.bot:
            await ctx.send ('Лучше эти деньги сохрани себе)\n'
                            'Твой любимый создатель')
        elif collection.find_one({'_id':ctx.author.id})['balance'] < count:
            await ctx.send (f'{ctx.author.mention}, простите ,но вы слишком бедны для того чтобы вложиться в другого пользователя')
        else:
            collection.update_one(
                {
                    '_id':ctx.author.id
                },
                {
                '$inc': {
                    'balance': -count
                }
                }
            )
            collection.update_one(
                {
                    '_id':member.id
                },
                {
                '$inc': {
                    'balance': count
                }
                }
            )
            await ctx.send (f'Успешно! Пользователю {member.mention} переведено {count} денег 💵')
            await member.send (f'Пользователь {ctx.author.mention} перевел вам свои пожитки в виде {count} денег 💵')


    @commands.command(name='give')
    @commands.has_any_role('нигаа')
    async def give (self,ctx,member:disnake.Member,count = int()):
        if member and member.bot:
            return await ctx.send('Нельзя выдавать деньги 💵 себе / боту')
        else:
            collection.update_one(
                {
                '_id':member.id
                },
                {
                '$inc':{
                    'balance':count
                }
                }
            )
            await ctx.send(f'Пользователю {member.mention} выдано {count} денег 💵')
        
            
        
        


def setup(bot):
    bot.add_cog(Economy_system(bot))



   
