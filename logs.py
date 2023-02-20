import disnake
from disnake.ext import commands
from pymongo import MongoClient
import datetime


cluster = MongoClient('mongodb+srv://Dovolentoboy:a600370@cluster0.6wxtw41.mongodb.net/test')
db = cluster['ecodb']
collection = db['users']

class logs(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        print('Module {} is loaded'.format(self.__class__.__name__))


    @commands.slash_command(name='ping')
    @commands.has_any_role('нигаа')
    async def ping(self, inter: disnake.ApplicationCommandInteraction):
        await inter.response.send_message(f"Понг! {round(self.bot.latency * 1000)}мс")

    @commands.Cog.listener()
    async def on_message_edit(self,before,after):
        embed=disnake.Embed(title=f'Пользователь изменил сообщение')
        embed.add_field(name='До:',value=f'`{before.content}`')
        embed.add_field(name='После:',value=f'`{after.content}`',inline=False)
        embed.add_field(name='Канал:',value=f'{before.channel.mention}',inline=False)
        embed.add_field(name='Время:',value=f'**{datetime.timedelta()}**',inline=True)
        embed.add_field(name='Пользователь:',value=f'{before.author.mention}',inline=True)
        await self.bot.get_channel(989659109299204136).send(embed=embed) #журнал аудита


    @commands.Cog.listener()
    async def on_message_delete(self,message):
        embed=disnake.Embed(title=f'Cообщение удалено')
        embed.add_field(name='Содержание:',value=f'`{message.content}`')
        embed.add_field(name=f'Кем удалено:',value=f'{message.author.mention}',inline=False)
        embed.add_field(name='Канал:',value=f'{message.channel.mention}')
        await self.bot.get_channel(989659109299204136).send(embed=embed) #журнал аудита
    

        



    

    @commands.Cog.listener()
    async def on_member_ban(self,guild, user):
        embed = disnake.Embed(
            title = 'Пользователя получает бан',
            description=f'{user} получает бан'
        )
        await self.bot.get_channel(989659109299204136).send(embed=embed) #журнал аудита
    

    @commands.Cog.listener()
    async def on_member_unban(self,guild, user):
        embed = disnake.Embed(
            title = 'Пользователя получает разбан',
            description=f'{user} получает помилование админа'
        )
        await self.bot.get_channel(989659109299204136).send(embed=embed) #журнал аудита

    


    

    
        
def setup(bot):
    bot.add_cog(logs(bot))
    