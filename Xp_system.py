import disnake
from disnake.ext import commands
from pymongo import MongoClient

cluster = MongoClient('mongodb+srv://Dovolentoboy:a600370@cluster0.6wxtw41.mongodb.net/test')
db = cluster['ecodb']
collection = db['users']

class Xp_system (commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        print('Module {} is loaded'.format(self.__class__.__name__))

    @commands.command(name='lvl')
    async def lvl(self,ctx,member:disnake.Member=None):
        if member is None:
            embed = disnake.Embed(
                title='Ваш опыт',
                description=f'```{collection.find_one({"_id":member.id})["xp"]}```\n'
                f'Ваш уровень\n'
                f'```{collection.find_one({"_id":member.id})["lvl"]}```'
            )
            await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Xp_system(bot))