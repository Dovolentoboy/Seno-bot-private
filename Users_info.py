import disnake
from disnake.ext import commands
from pymongo import MongoClient


cluster = MongoClient(LINK)
Warndb = cluster.Warndb
Warncoll =  Warndb.users


Economydb = cluster.ecodb
Economycoll = Economydb.users


Mutedb = cluster.Mutedb
Mutecoll = Mutedb.users


Localbandb = cluster.Localban
Localbancoll = Localbandb.users


async def check_user(ctx):
    await ctx.send('Это заранее заготовленное сообщение. Вы не можете просмотреть информацию о боте ')

class User_info(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        print('Module {} is loaded'.format(self.__class__.__name__))


    @commands.slash_command(name='userinfo')
    @commands.has_permissions(administrator=True)
    async def userinfo(self,ctx,member:disnake.Member=None):  
        if member is None or member == ctx.author:
            embed = disnake.Embed(
            title=f'Статистика пользователя {ctx.author.mention}',
            description=f'Ниже будет преставлена статистика о вас \n'
                        f'\n'
                        f'Ваши провинности💀\n'
                        f'\n'
                        f'Ваши предупреждения :\n'
                        f'\n'
                        f' ```{Warncoll.find_one({"_id":ctx.author.id})["warns"]}``` \n'
                        f'Ваши муты:\n'
                        f'\n'
                        f'```{Mutecoll.find_one({"_id":ctx.author.id})["mutes"]}```\n'
                        f'\n'
                        f'Ваши локальные блокировки:'
                        f'```{Localbancoll.find_one({"_id":ctx.author.id})["localban"]}```'
                        f'\n'
                        'Экономика\n'
                        f'\n'
                        f'Деньги 💵:'
                        f'```{Economycoll.find_one({"_id":ctx.author.id})["balance"]}```'
                        f'\n'
                        f'Ваш уровень:'
                        f'\n'
                        f'```{Economycoll.find_one({"_id":ctx.author.id})["lvl"]}```\n'
                        '\n'
                        f'Ваш опыт:'
                        f'\n'
                        f'```{Economycoll.find_one({"_id":ctx.author.id})["xp"]}```'
        )
        else:
            embed = disnake.Embed(
            title=f'Статистика пользователя {member.mention}',
            description=f'Ниже будет преставлена статистика о вас \n'
                        f'\n'
                        f'Ваши провинности💀\n'
                        f'\n'
                        f'Ваши предупреждения :\n'
                        f'\n'
                        f' ```{Warncoll.find_one({"_id":member.id})["warns"]}``` \n'
                        f'Ваши муты:\n'
                        f'\n'
                        f'```{Mutecoll.find_one({"_id":member.id})["mutes"]}```\n'
                        f'\n'
                        f'Ваши локальные блокировки:'
                        f'```{Localbancoll.find_one({"_id":member.id})["localban"]}```'
                        f'\n'
                        'Экономика\n'
                        f'\n'
                        f'Деньги 💵:'
                        f'```{Economycoll.find_one({"_id":member.id})["balance"]}```'
                        f'\n'
                        f'Ваш уровень:'
                        '\n'
                        f'```{Economycoll.find_one({"_id":member.id})["lvl"]}```\n'
                        f'\n'
                        f'Ваш опыт:'
                        f'\n'
                        f'```{Economycoll.find_one({"_id":member.id})["xp"]}```'
        )
        
        await ctx.send(embed=embed)
           



def setup(bot):
    bot.add_cog(User_info(bot))