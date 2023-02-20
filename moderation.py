import disnake
from disnake.ext import commands
from disnake.ext.commands import MissingAnyRole,MissingPermissions
import time
from time import strftime
from time import localtime
import asyncio
from asyncio import sleep







async def check_user(ctx):
    embed=disnake.Embed(color=disnake.Color.from_rgb(47,50,55),description="Нельзя выдать наказание/помилование самому себе. А ты что хотел? Такова участь модератора))) ",
    title='Ошибка применения команды')
    embed.set_thumbnail(url='https://cdn.discordapp.com/avatars/1046497929776603136/fa969a3a96de3c24a6ce1e56e7f0c379.png?size=1024')
    await ctx.send(embed=embed)


class Moderation(commands.Cog):
    def __init__(self, bot=commands.cog):
        self.bot = bot
        print('Module {} is loaded'.format(self.__class__.__name__))


        @commands.Cog.listener()
        async def on_command_error(ctx,error):
                print(error)
            
                if isinstance(error,MissingPermissions,MissingAnyRole):
                    embed=disnake.Embed(title='Ошибка примения команды',
                    description=f'{ctx.author.mention} у вас недостаточно прав для примения команды')
                    await ctx.send(embed=embed)

    @commands.slash_command(name="ban", description='Забанить на сервере')
    @commands.has_permissions(administrator=True)
    async def ban(self, ctx, member: disnake.Member, *, reason="Не указана"):
        if member and member.bot:
            await check_user(ctx)
        embed = disnake.Embed(title='Выдать Бан',color=disnake.Color.from_rgb(47, 50, 55))
        embed.add_field(name='Бан',value=f'Пользователь {ctx.author.mention} выдал Бан пользователю {member.mention}')
        embed.add_field(name='Причина:',value=reason,inline=False)
        await ctx.send(embed=embed)
        embed=disnake.Embed(color=disnake.Color.from_rgb (47,50,55),title='Вам был выдан Бан',
        description=f'Пользователь {member.mention} получил **Бан** по причине {reason} ')
        embed.add_field(
        value='Если вы считаете,что блокировка была ошибочной отписывать .',inline=False
        )
        embed.add_field(name='Создатель-', value='<@575681490810175500> (Rudi#1881)',inline=True)
        embed.add_field(name='Заместитель-', value='<@424262053071552513>(alexlovus#8863)',inline=True)
        embed.add_field(name='Заместитель-', value='<@873595256782856263>(wwlpx#6367)',inline=True)
        embed.add_field(name='Кем было выдано:',value=f'{ctx.author.mention}', inline=False)
        embed.set_thumbnail(url='https://cdn.discordapp.com/avatars/1046497929776603136/fa969a3a96de3c24a6ce1e56e7f0c379.png?size=1024')
        await member.send(embed=embed) #личка
        await member.ban(reason=reason)

        
            
        
        

    @commands.slash_command(name="unban", description='Разбанить на сервере')
    @commands.has_permissions(administrator=True)
    async def unban(self,ctx,member:disnake.Member):
        if member==ctx.author:
            return await check_user(ctx)
        ban_embed = disnake.Embed(title='Бан',description=f'{ctx.author.mention} разбанил пользователя {member.mention}')   
        await ctx.send (embed = ban_embed)
        await member.unban()


    @commands.slash_command(name='mute',description=' Замьютить ')
    @commands.has_permissions(administrator=True)
    async def mute (self,ctx,member:disnake.Member,*,reason ='Не указана',time=int(1*60)):
        if member and member.bot:
            await check_user(ctx)
        else:
            mute = disnake.utils.get(member.guild.roles, id=926527088985514084)
            embed = disnake.Embed(title='Выдать Мьют',color=disnake.Color.from_rgb(47, 50, 55))
            embed.add_field(name='Мьют',value=f'Пользователь {ctx.author.mention} выдал Мьют пользователю {member.mention} на {time} минут по причине {reason}')
            embed.add_field(name='Причина:',value=reason,inline=False)
            embed.set_image(url='https://media.tenor.com/3N3A5MQ6d_oAAAAC/blackand-white-anime.gif')
            await ctx.send(embed=embed)
            embed=disnake.Embed(color=disnake.Color.from_rgb (47,50,55),title='Вам был выдан Муют',
            description=f'Пользователь {member.mention} получил **Мьют** на {time} часов')
            embed.add_field(name='Причина:',value=reason)
            embed.set_image(url='https://media.tenor.com/P1hgLYnoJmsAAAAC/mei-misaki-another.gif')
            await member.send(embed=embed)
            await member.add_roles(mute)
            await asyncio.sleep(time)
            await member.remove_roles(mute)

        
        


    @commands.slash_command(name='unmute',description='Размьютить')
    @commands.has_permissions(administrator=True)
    async def unmute(self,ctx,member:disnake.Member):
            if member and member.bot:
                return await check_user(ctx)
            mute = disnake.utils.get(member.guild.roles, id=926527088985514084)
            mute_embed = disnake.Embed(title='Мут',description=f'{ctx.author.mention} размьюти пользователя {member.mention}')   
            await ctx.send (embed = mute_embed)
            await member.remove_roles(mute)


    @commands.slash_command(name='unlocalban',description = 'Разбан+роль')
    @commands.has_permissions(administrator=True)
    async def unbankai(self,ctx,member:disnake.Member):
        if member and member.bot:
            return await check_user(ctx)
        lb=disnake.utils.get(member.guild.roles,id=1068879473107271720)         
        lb_embed = disnake.Embed(title='Локал бан',description=f'{ctx.author.mention} разбанил пользователя {member.mention}')   
        await ctx.send(embed = lb_embed)
        await member.remove_roles(lb)
    

    @commands.slash_command(name='localban',description = 'Бан+роль')
    @commands.has_permissions(administrator=True)
    async def localban(self,ctx,member:disnake.Member,*,reason='Не указана'):
        if member and member.bot:
            return await check_user(ctx)
        else:
            lb=disnake.utils.get(member.guild.roles,id=1068879473107271720)
            embed = disnake.Embed(title='Выдать локальную блокировку',color=disnake.Color.from_rgb(47, 50, 55))
            embed.add_field(name='Бан',value=f'Пользователь {ctx.author.mention} выдал Бан пользователю {member.mention}')
            embed.add_field(name='Причина:',value=reason,inline=False)
            embed.set_image(url='https://anime-chan.me/uploads/posts/2016-01/1452967606_anime-sword-art-online-lisbeth-anime-gifki-2775271.gif')
            await ctx.reply(embed=embed)
            embed=disnake.Embed(color=disnake.Color.from_rgb (47,50,55),title='Вам был выдан Бан',
            description=f'Пользователь {member.mention} получил **Бан** по причине: ')
            embed.add_field(name=reason,
            value='Если вы считаете,что блокировка была ошибочной отписывать людям ниже',inline=False

            )
            embed.add_field(name='Создатель-', value='<@575681490810175500> (Rudi#1881)',inline=True)
            embed.add_field(name='Заместитель-', value='<@424262053071552513>(alexlovus#8863)',inline=True)
            embed.add_field(name='Заместитель-', value='<@873595256782856263>(wwlpx#6367)',inline=True)
            embed.add_field(name='Кем было выдано:',value=f'{ctx.author.mention}', inline=False)
            embed.set_thumbnail(url='https://cdn.discordapp.com/avatars/1046497929776603136/fa969a3a96de3c24a6ce1e56e7f0c379.png?size=1024')
            embed.set_image(url='http://68.media.tumblr.com/0e42f221a783ae10e79fd8c710b59898/tumblr_o1usx7DyI91s7fey2o1_500.gif')
            await member.send(embed=embed)
            await member.add_roles(lb)


    
        



    @commands.slash_command(name='clear',description='Очистка чата')
    @commands.has_permissions(administrator=True)
    async def clear(self,ctx,amount=int()):
        embed=disnake.Embed(title='Очистка чата',description=f'Вы очистили {amount} сообщений')
        await ctx.send(embed=embed)
        await ctx.channel.purge(limit = int(amount))




    
            
        
        


def setup(bot):
    bot.add_cog(Moderation(bot))
