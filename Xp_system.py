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
                description=f'```{collection.find_one({"_id":ctx.author.id})["xp"]}```\n'
                f'Ваш уровень\n'
                f'```{collection.find_one({"_id":ctx.author.id})["lvl"]}```'
            )
            await ctx.send(embed=embed)
        else:
            embed = disnake.Embed(
                title='Ваш опыт',
                description=f'```{collection.find_one({"_id":member.id})["xp"]}```\n'
                f'Ваш уровень\n'
                f'```{collection.find_one({"_id":member.id})["lvl"]}```'
            )
            await ctx.send(embed=embed)
    
    @commands.Cog.listener()
    async def on_message(self,message):
        if message.author == self.bot.user:
            return
        user = message.author
        data = collection.find_one({'_id':user.id})
        if data['xp'] == 1000 + 1000 * data['lvl']:
            collection.update_one(
                {
                '_id':user.id
                },
                {
                '$inc':{
                    'lvl':1
                }
                }
            )

            collection.update_one(
                {
                '_id':user.id
                },
                {
                '$set':{
                    'xp':0
                }
                }
            )
            
        else:
            collection.update_one(
                {
                '_id':user.id
                },
                {
                    '$inc':{
                        'xp':5
                    }
                }
            )


    


def setup(bot):
    bot.add_cog(Xp_system(bot))
