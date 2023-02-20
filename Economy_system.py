import disnake
from disnake.ext import commands
from pymongo import MongoClient

cluster = MongoClient('mongodb+srv://Dovolentoboy:a600370@cluster0.6wxtw41.mongodb.net/test')
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
                description=f"Ваш баланс 💵 : **{collection.find_one({'_id':ctx.author.id})['balance']}"
            )
            await ctx.send (embed=embed)
        else:
            embed = disnake.Embed(
            title='Баланс',
            description=f"Баланс 💵 пользователя {member.mention}\n ```{collection.find_one({'_id':member.id})['balance']}```")
            await ctx.send (embed=embed)


def setup(bot):
    bot.add_cog(Economy_system(bot))



   