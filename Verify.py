import disnake
from typing import Optional
from disnake.ext import commands




class Verify_button (disnake.ui.View):
    def __init__ (self):
        super().__init__(timeout=None)
        self.value: Optional[bool] = None

    @disnake.ui.button(label='Верифицироваться',style=disnake.ButtonStyle.green,emoji='✅')
    async def verify(self,button:disnake.Button,interaction:disnake.Interaction):
        role = interaction.guild.get_role(926372966487453726)
        verify_role = interaction.guild.get_role(1068443146586947634)
        await interaction.user.remove_roles(verify_role)
        await interaction.user.add_roles(role)
        await interaction.response.send_message('Вы успешно прошли верификацию!',ephemeral=True)


class Verify(commands.Cog):
    def __init__(self,bot) :
        self.bot = bot
        print('Module {} is loaded'.format(self.__class__.__name__))

    
    @commands.command(name='verify')
    @commands.has_permissions(administrator=True)
    async def verify(self,ctx):
        view=Verify_button()
        verify_embed = disnake.Embed(
            title='Верификация',
            description='Пройдите верификацию чтобы продолжить общение!'
        )
        await ctx.send(embed=verify_embed,view=view)

    
        

def setup(bot):
    bot.add_cog(Verify(bot))
