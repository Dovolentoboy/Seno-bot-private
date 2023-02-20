import disnake
from disnake.ext import commands
from typing import Optional



class Role_list(disnake.ui.View):
    def __init__ (self):
        super().__init__(timeout=None)
        self.value: Optional[bool] = None


    @disnake.ui.button(style=disnake.ButtonStyle.grey,label='Черный',row=1)
    async def Black (self,button:disnake.Button,interaction:disnake.Interaction):
        Black = interaction.guild.get_role(1072561365438451743)
        await interaction.user.add_roles(Black)
        await interaction.response.send_message(f'{Black.mention} Успешно присвоено',ephemeral=True)


    @disnake.ui.button(style=disnake.ButtonStyle.grey,label='Желтый',row=1)
    async def Yellow (self,button:disnake.Button,interaction:disnake.Interaction):
        Yellowe = interaction.guild.get_role(1053659255586173069)
        await interaction.user.add_roles(Yellowe)
        await interaction.response.send_message(f'{Yellowe.mention} Успешно присвоено',ephemeral=True)


    @disnake.ui.button(style=disnake.ButtonStyle.grey,label='Синий',row=1)
    async def Blue (self,button:disnake.Button,interaction:disnake.Interaction):
        Blue = interaction.guild.get_role(1072584390229643405)
        await interaction.user.add_roles(Blue)
        await interaction.response.send_message(f'{Blue.mention} Успешно присвоено',ephemeral=True)


    @disnake.ui.button(style=disnake.ButtonStyle.grey,label='Белый',row=2)
    async def White (self,button:disnake.Button,interaction:disnake.Interaction):
        White = interaction.guild.get_role(1072589560405561355)
        await interaction.user.add_roles(White)
        await interaction.response.send_message(f'{White.mention} Успешно присвоено',ephemeral=True)
    
    @disnake.ui.button(style=disnake.ButtonStyle.grey,label='Фиолетовый',row=2)
    async def Purple (self,button:disnake.Button,interaction:disnake.Interaction):
        Purple = interaction.guild.get_role(1053659559698382940)
        await interaction.user.add_roles(Purple)
        await interaction.response.send_message(f'{Purple.mention} Успешно присвоено',ephemeral=True)

    @disnake.ui.button(style=disnake.ButtonStyle.grey,label='Зеленый',row=2)
    async def Green (self,button:disnake.Button,interaction:disnake.Interaction):
        Green = interaction.guild.get_role(1073320952517103677)
        await interaction.user.add_roles(Green)
        await interaction.response.send_message(f'{Green.mention} Успешно присвоено',ephemeral=True)

    @disnake.ui.button(style=disnake.ButtonStyle.grey,label='Розовый',row=3)
    async def Pink(self,button:disnake.Button,interaction:disnake.Interaction):
        Pink = interaction.guild.get_role(1073321877164007515)
        await interaction.user.add_roles(Pink)
        await interaction.response.send_message(f'{Pink.mention} Успешно присвоено',ephemeral=True)
    

    @disnake.ui.button(style=disnake.ButtonStyle.grey,label='Коричневый',row=3)
    async def Brown(self,button:disnake.Button,interaction:disnake.Interaction):
        Brown = interaction.guild.get_role(1073325026113237032)
        await interaction.user.add_roles(Brown)
        await interaction.response.send_message(f'{Brown.mention} Успешно присвоено',ephemeral=True)

    @disnake.ui.button(style=disnake.ButtonStyle.grey,label='Ядовитый',row=4)
    async def Toxic(self,button:disnake.Button,interaction:disnake.Interaction):
        Toxic = interaction.guild.get_role(1046155535134769192)
        await interaction.user.add_roles(Toxic)
        await interaction.response.send_message(f'{Toxic.mention} Успешно присвоено',ephemeral=True)

    @disnake.ui.button(style=disnake.ButtonStyle.grey,label='Красный',row=4)
    async def Red(self,button:disnake.Button,interaction:disnake.Interaction):
        Red = interaction.guild.get_role(1076188724624371793)
        await interaction.user.add_roles(Red)
        await interaction.response.send_message(f'{Red.mention} Успешно присвоено',ephemeral=True)

    @disnake.ui.button(style=disnake.ButtonStyle.grey,label='Оранжевый',row=4)
    async def Orange(self,button:disnake.Button,interaction:disnake.Interaction):
        Orange = interaction.guild.get_role(1076189305455771768)
        await interaction.user.add_roles(Orange)
        await interaction.response.send_message(f'{Orange.mention} Успешно присвоено',ephemeral=True)

    @disnake.ui.button(style=disnake.ButtonStyle.grey,label='Аква',row=3)
    async def Aqua(self,button:disnake.Button,interaction:disnake.Interaction):
        Aqua = interaction.guild.get_role(1076190223978999831)
        await interaction.user.add_roles(Aqua)
        await interaction.response.send_message(f'{Aqua.mention} Успешно присвоено',ephemeral=True)


    @disnake.ui.button(style=disnake.ButtonStyle.grey,emoji='🧹',row=0)
    async def all_remove (self,button:disnake.Button,interaction:disnake.Interaction):
        White = interaction.guild.get_role(1072589560405561355)
        Blue = interaction.guild.get_role(1072584390229643405)
        Yellowe = interaction.guild.get_role(1053659255586173069)
        Black = interaction.guild.get_role(1072561365438451743)
        Purple = interaction.guild.get_role(1053659559698382940)
        Green = interaction.guild.get_role(1073320952517103677)
        Brown = interaction.guild.get_role(1073325026113237032)
        Red = interaction.guild.get_role(1076188724624371793)
        Orange = interaction.guild.get_role(1076189305455771768)
        Aqua = interaction.guild.get_role(1076190223978999831)
        Pink = interaction.guild.get_role(1073321877164007515)
        Toxic = interaction.guild.get_role(1046155535134769192)
        await interaction.response.send_message('С вас успешно забраны все роли цветов!',ephemeral=True)
        await interaction.user.remove_roles(White,Black,Blue,Yellowe,Purple,Green,Brown,Orange,Aqua,Red,Pink,Toxic)
        
    


    
        
        

    
class Rolelists(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        print('Module {} is loaded'.format(self.__class__.__name__))


    @commands.command(name='Rolelist')
    @commands.has_permissions(administrator=True)
    async def Rolelist(self,ctx):
        view = Role_list()
        embed = disnake.Embed(
        title='Выберите Цвет при помощи кнопок ниже',
        description=
        '<@&1072561365438451743> - Черный цвет: \n'
        '<@&1053659255586173069> - Желтый цвет\n'
        '<@&1072584390229643405> - Синий цвет\n'
        '<@&1072589560405561355> - Белый цвет\n'
        '<@&1053659559698382940> - Фиолетовый цвет\n'
        '<@&1073320952517103677> - Зеленый цвет\n'
        '<@&1073321877164007515> - Розовый цвет \n'
        '<@&1073322347051884655> - Темно-фиолетовый цвет\n'
        '<@&1073325026113237032> - Коричневый цвет\n'
        '<@&1046155535134769192> - Ядовитый цвет\n'
        '<@&1076189305455771768> - Оранжевый\n'
        '<@&1076190223978999831> - Аква\n'
        '<@&1076188724624371793> - Красный\n'
        'По всем вопросам бота обращаться к <@839490293447524384>',
        color=disnake.Color.from_rgb(47,50,55)
        )
        embed.set_image(url='https://i.pinimg.com/originals/0b/5f/93/0b5f93b109857efa338b93449fdf72aa.gif')
        
        
        await ctx.send (embed=embed,view=view)

   






def setup(bot):
    bot.add_cog(Rolelists(bot))
                

        