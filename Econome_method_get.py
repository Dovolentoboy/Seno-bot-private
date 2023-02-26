import disnake
import random
import datetime
from disnake.ext import commands
from pymongo import MongoClient

cluster = MongoClient('mongodb+srv://Dovolentoboy:a600370@cluster0.6wxtw41.mongodb.net/test')
db = cluster['ecodb']
collection = db['users']


class Economy_methot_get(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        print('Module {} is loaded'.format(self.__class__.__name__))



    @commands.Cog.listener()
    async def on_message(self,message):
        if message.author == self.bot.user:
            return
        else:
            collection.update_one(
                {
                '_id':message.author.id
                },
                {
                '$inc':{
                    'balance':5
                }
                }
            )


def setup(bot):
    bot.add_cog(Economy_methot_get(bot))

    
