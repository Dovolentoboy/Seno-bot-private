from disnake.ext import tasks, commands
import disnake
import random
from typing import Optional





bite = ['https://media.discordapp.net/attachments/889573796070162432/889573892207804466/image0.gif',
        'https://media.discordapp.net/attachments/889573796070162432/889573892530782208/image1.gif',
        'https://media.discordapp.net/attachments/889573796070162432/889573893772283944/image3.gif',
        'https://media.discordapp.net/attachments/889573796070162432/889573894258843668/image4.gif',
        'https://media.discordapp.net/attachments/889573796070162432/889573894598574121/image5.gif',
        'https://media.discordapp.net/attachments/889573796070162432/889573895470972958/image7.gif',
        'https://media.discordapp.net/attachments/889573796070162432/889573896037224518/image8.gif'
        ]
hug = ['1059124944358879232/hug_0.gif', '1059133714044559380/hug_1.gif', '1059133714430447626/hug_2.gif',
       '1059133714837282862/hug_3.gif', '1059133715252527144/hug_4.gif', '1059133715592269884/hug_5.gif',
       '1059133715990716416/hug_6.gif', '1059134737140174908/hug_7.gif', '1059134737727365190/hug_8.gif',
       '1059134738150981693/hug_9.gif', '1059134738872422420/hug_10.gif', '1059134739291840532/hug_11.gif',
       '1059134739749011456/hug_12.gif', '1059134740336234567/hug_13.gif', '1059134740835336212/hug_14.gif',
       '1059134741254787122/hug_15.gif', '1059135687498149908/hug_16.gif', '1059135687921782804/hug_17.gif',
       '1059135688278290543/hug_18.gif', '1059135688676737034/hug_19.gif', '1059135689112965170/hug_20.gif',
       '1059135691570819222/hug_21.gif', '1059135691935731752/hug_22.gif', '1059136114633490442/hug_22.gif',
       '1059136115057102858/hug_23.gif', '1059136115442995310/hug_24.gif', '1059136115807883434/hug_25.gif',
       '1059156786021666896/gif_26.gif', '1059156786332057610/gif_27.gif', '1059156786625663026/gif_28.gif'
                                                                           '1059156786936025248/gif_29.gif'
       ]
smoke = ['1059158748242907196/smoke_0.gif', '1059158782896263179/smoke_1.gif', '1059158791406506056/smoke_2.gif'
                                                                               '1059158809542664304/smoke_3.gif',
         '1059158834830123038/smoke_4.gif', '1059158854132318308/smoke_5.gif',
         '1059170403404230727/smoke_6.gif', '1059170403945283704/smoke_7.gif', '1059170404645736468/smoke_8.gif',
         '1059170405153255424/smoke_9.gif', '1059170405715284009/smoke_10.gif'
         ]
smile = ['1059169885621583882/smile_10.gif', '1059169886129115276/smile_9.gif', '1059169886590468126/smile_8.gif',
         '1059169887035084862/smile_7.gif', '1059169887546769428/smile_6.gif', '1059169887970414652/smile_5.gif',
         '1059169888712785991/smile_3.gif', '1059169889300008970/smile_2.gif', '1059169889681686569/smile_1.gif',
         '1059170016597135461/smile_12.gif', '1059170017192718346/smile_11.gif'
         ]
wave = ['1059171992953171988/wave_1.gif', '1059171992479207444/wave_2.gif', '1059171991824900130/wave_3.gif',
        '1059171991392882699/wave_4.gif', '1059171990965071953/wave_5.gif', '1059171990562410617/wave_6.gif',
        '1059171990184927292/wave_7.gif'
        ]
pat = ['1059172765950808134/pat_1.gif', '1059172765636239561/pat_2.gif', '1059172765267148840/pat_3.gif',
       '1059172764998701096/pat_4.gif', '1059172764679938148/pat_5.gif', '1059172764356984912/pat_6.gif',
       '1059172764050788462/pat_7.gif', '1059172763732025408/pat_8.gif', '1059172763417460766/pat_9.gif',
       '1059172763035766874/pat_10.gif'
       ]
wink = ['1059175697416982638/wink_1.gif', '1059175697073053787/wink_2.gif', '1059175696762667100/wink_3.gif',
        '1059175696410349578/wink_4.gif', '1059175695965757470/wink_5.gif', '1059175695621816340/wink_6.gif',
        '1059175695303053383/wink_7.gif', '1059175694963318864/wink_8.gif', '1059175694657126462/wink_9.gif',
        '1059175694329974925/wink_10.gif'
        ]
lick = ['1059177648108097676/lick_1.gif', '1059177647386660965/lick_2.gif', '1059177646862389418/lick_3.gif',
        '1059177646392623224/lick_4.gif', '1059177645981585518/lick_5.gif', '1059177645583110234/lick_6.gif',
        '1059177645163692093/lick_7.gif', '1059177644710711336/lick_8.gif'
        ]
bonk = ['1059178911944163399/Bonk_1.gif', '1059178911612801084/Bonk_2.gif', '1059178911277252608/Bonk_3.gif',
        '1059178910874615848/Bonk_4.gif', '1059178910576808017/Bonk_5.gif', '1059190633723605140/bonk_6.gif',
        '1059190634122055680/bonk_7.gif', '1059190634482774058/bonk_8.gif', '1059190634822508605/bonk_9.gif',
        '1059190635464232981/bonk_10.gif'
        ]
happy = ['zCYkbZ_.gif', 'ugYkZmY.gif', 'E96qRwy.gif', "Vk_UEkj.gif", "FTwUuPj.gif", 'SWMEyvi.gif', 'U3KnDqC.gif',
         'ZBGzoJM.gif', 'GTqw3qe.gif', 'yiso92r.gif', '60P7W0B.gif', '6i0Ultd.gif', 'QIgMz3F.gif'
         ]
dance = ['1059167795138527262/dance_1.gif', '1059167794706518077/dance_2.gif', '1059167794190635048/dance_3.gif',
         '1059167793326608424/dance_5.gif', '1059167793750216784/dance_4.gif', '1059167792479342592/dance_7.gif',
         '1059167792026374174/dance_8.gif', '1059167791623700541/dance_9.gif', '1059167791179108422/dance_10.gif',
         '1059167799689363486/dance_11.gif'
         ]
smug = ['Wf2wxtM.gif', 'hEHBgzb.gif', '5W-whq8.gif', 'r_Gx1KQ.gif', 'djTUASr.gif', '8Py2vAi.gif',
        'TavGjAi.gif', 'SQMCRFn.gif', 'p_KTcUp.gif'
        ]
kiss = ['https://cdn.discordapp.com/attachments/1059124257445118012/1059154163361120256/'
        '4037e6ae03275bd33b3e5df50acda41a.gif',
        'https://cdn.discordapp.com/attachments/1059124257445118012/1059154162924916746/'
        'b45bb5bfddb6115a76c3bf4057bc176a.gif', 'https://cdn.discordapp.com/attachments/1059124257445118012/10591541'
                                                '62434179072/2b023f55e9a938c4f9adf6baad25a98d.gif',
        'https://cdn.discordapp.com/attachments/1059124257445118012/1059154161997975692/'
        '9e8f058883fe6d3e7e62d34dacbf9574.gif', 'https://cdn.discordapp.com/attachments/1059124257445118012/'
                                                '1059154161477877770/8e07e7c01e476e419c09949d15b2530c.gif',
        'https://cdn.discordapp.com/attachments/1059124257445118012/1059154161071038485/'
        '21dc95dc046c6505af35603227d6a923.gif', 'https://cdn.discordapp.com/attachments/1059124257445118012/'
                                                '1059154160513187860/e00f3104927ae27d7d6a32393d163176.gif'
        ]
slap = ['vX9nrsn.gif', 'E7cfJjs.gif', 'r4jONxp.gif', 'mXj8i8S.gif', 's~CLnmA.gif', '6-_UTFD.gif', 'puI2pTf.gif',
        'cvKQqp-.gif', 'JOKXwLd.gif', 'zFe9vib.gif', 'aI5vJ9n.gif', '~P5~hin.gif', 'gsskphB.gif', 'VPwmf~k.gif',
        '28V06Sq.gif', 'Oyfmk6s.gif', 'QFGN4vE.gif'
        ]
squeeze = ['1059553165772587028/squeeze_1.gif', '1059553164669485227/squeeze_3.gif',
           '1059553164283625592/squeeze_4.gif', '1059553163780292719/squeeze_5.gif',
           '1059553163394433035/squeeze_6.gif', '1059553162673012766/squeeze_8.gif', '1059553162287132722/squeeze_9.gif'
           ]
kill = ['6Izshr4.gif', 'jNWDXiC.gif', 'ETWB-ef.gif', '9b1NpBN.gif', 'Q~m51SY.gif', '7Z1tV23.gif', 'hsAy9-u.gif',
        'lgsRSai.gif', '8uhQSdY.gif', 'hGFuwrQ.gif', 'Oz4aaul.gif', 'judBJyS.gif', 'ylnGeuF.gif', 'Qug33iz.gif',
        'aHcQUmi.gif'
        ]
suicide = ['1059803775335931965', '1059803775017173022', '1059803774358659142', '1059803774006345789',
           '1059807635827851284', '1059807636234702858'
           ]
blush = ['1059816095244103690', '1059816095613198386', '1059816095931977748', '1059816096292679710',
         '1059816096825364560', '1059816097186066442', '1059816097555161148', '1059816098205282344',
         '1059816098943475712', '1059816099358715945', '1059816380926533733', '1059816381320802325',
         '1059816381861863494', '1059816382419718315', '1059816382826557480', '1059816383275356220',
         '1059816383820607548', '1059816384231645224', '1059816384764334140', '1059816606290681906',
         '1059816606609453116', '1059816607288926258', '1059816607603503124', '1059816607985176586',
         '1059816608329113640', '1059816608719188038', '1059816606982737970'
         ]
poke = ['1059834814569652294', '1059834814871634000', '1059834815203004486', '1059834815517564948',
        '1059834815895044157', '1059834816348049531', '1059834816821985380', '1059834817178521681',
        '1059834817589551174', '1059835114915373056', '1059835115292872745', '1059835115687133204',
        '1059835116089778328', '1059835116500828262', '1059835116848947210', '1059835117234835567',
        '1059835117692010596', '1059835118144999494', '1059835184607936602', '1059835185119645776'
        ]
love = ['1059855879043809330', '1059855878494359643', '1059855878116876288', '1059855877714214962',
        '1059855877252849735', '1059855693546520616', '1059855693248737340', '1059855692879646730',
        '1059855692527304715', '1059855692179189790', '1059855691847847987', '1059855691445174292',
        '1059855691067699334', '1059855690585341992', '1059855690119786566', '1059856975204208740'
        ]
depression = ['1059876886248947762', '1059876885846310932', '1059876793856831569', '1059876793538060329',
              '1059876793114447882', '1059876792791478472', '1059876792460124160', '1059876792078454864',
              '1059876791759679628', '1059876791390576721', '1059876791071821955', '1059876278766936174',
              '1059876277919699065', '1059876277537996960', '1059876277139546232', '1059876276661387264',
              '1059876276229382285', '1059876275818352740', '1059876275336003634', '1059886129375096852'
              ]
sleep = ['1059939431064289360/sleep_1.gif', '1059939431064289360/sleep_2.gif', '1059939431064289360/sleep_3.gi'
                                                                               '1059939431064289360/sleep_4.gif',
         '1059939431064289360/sleep_5.gif', '1059939431064289360/sleep_6.gif'
                                            '1059939431064289360/sleep_7.gif,', '1059939431064289360/sleep_8',
         '1059939431064289360/sleep_9.gif',
         "1059939431064289360/sleep_10.gif", '1059939431064289360/sleep_11.gif', '1059939431064289360/sleep_12.gif',
         '1059939431064289360/sleep_13.gif', '1059939431064289360/sleep_14'
         ]
clap = ['1053311607784079370/clap_1.gif', '1053311607784079370/clap_2', '1053311607784079370/clap_3',
        '1053311607784079370/clap_4', '1053311607784079370/clap_5', '1053311607784079370/clap_6'
        ]


class Confirm(disnake.ui.View):
    def __init__(self):
        super().__init__(timeout=10.0)
        self.value: Optional[bool] = None

    
    @disnake.ui.button(style=disnake.ButtonStyle.grey,emoji='✅')
    async def confirm(self, button: disnake.ui.Button, inter: disnake.MessageInteraction):
        self.value = True
        self.stop()
        
    
    @disnake.ui.button(style=disnake.ButtonStyle.grey,emoji='❌')
    async def cancel(self, button: disnake.ui.Button, inter: disnake.MessageInteraction):
        self.value = False
        self.stop()

async def check_user(ctx):
    return await ctx.send("Вам так одиноко( Могу лишь посоветовать зайти в  " + "<#1037434967967420468>. ",
                          ephemeral=True)





class Reaction(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        print('Module {} is loaded'.format(self.__class__.__name__))

    @commands.command(name='bite', aliases=['кусь', 'Кусь', 'укусить'])
    async def bite(self, ctx, member: disnake.Member = None):
        if member is None:
            member = ctx.author
        embed = disnake.Embed(color=disnake.Color.from_rgb(47, 50, 55), title="Реакция: Укусить")
        embed.description = f"{ctx.author.mention} укусил {member.mention}"
        url = (random.choice(bite))
        embed.set_image(url=url)
        await ctx.reply(embed=embed)


    @commands.command(name='kiss',aliases=['поцеловать'])
    async def kiss(self, ctx,*, member: disnake.Member = None):
        if member and member.bot:
            await check_user(ctx)
        view = Confirm()
        embed = disnake.Embed(title='Реакция : Поцелуй',description=f'{member.mention},тебя тут поцеловать хотят. Что ответим?',color=disnake.Color.from_rgb(47, 50, 55))
        message = await ctx.reply(embed=embed,view=view)
        await view.wait()
        if view.value is None:
            embed=disnake.Embed(title='Реакция:Поцелуй',description=f'{member.mention} проигнорировал / не заметил реакции',color=disnake.Color.from_rgb(47, 50, 55))
            await message.edit(embed=embed)
        elif view.value :
            embed = disnake.Embed(color=disnake.Color.from_rgb(47, 50, 55), title="Реакция: Поцелуй")
            embed.description = f"{ctx.author.mention} поцеловал {member.mention}"
            url = (random.choice(kiss))
            embed.set_image(url=url)
            await message.edit(embed=embed)
        else:
            embed = disnake.Embed(title='Реакция:Поцелуй',description=f'{member.mention} отказал вам',color=disnake.Color.from_rgb(47, 50, 55))
            await message.edit(embed=embed)
        for child in view.children:
            if isinstance(child, disnake.ui.Button):
                child.disabled = True
                view.clear_items
                await message.edit(view=view)
        

    @commands.command(name='hug', aliases=['обнять'])
    async def hug(self, ctx,*, member: disnake.Member = None):
        embed = disnake.Embed(color=disnake.Color.from_rgb(47, 50, 55), title="Реакция: Обнять")
        if member is None or member == ctx.author:
            embed.description = f"{ctx.author.mention} обнимает всех в чате"
        else:
            embed.description = f"{ctx.author.mention} обнимает {member.mention}"
        url = "https://cdn.discordapp.com/attachments/1059124472407412857/" + (random.choice(hug))
        embed.set_image(url=url)
        await ctx.reply(embed=embed)

    @commands.command(name='smoke', aliases=['смоке', 'курить'])
    async def smoke(self,ctx,*, member: disnake.Member = None):
        if member and member.bot:
            await check_user(ctx)
        embed = disnake.Embed(color=disnake.Color.from_rgb(47, 50, 55), title="Реакция: Курить")
        if member is None or member == ctx.author:
            embed.description = f"{ctx.author.mention} курит"
        else:
            embed.description = f"{ctx.author.mention} курит вместе с {member.mention}"
        url = "https://cdn.discordapp.com/attachments/1059151359833800714/" + (random.choice(smoke))
        embed.set_image(url=url)
        await ctx.reply(embed=embed)

    @commands.command(name='wave', aliases=['помохать', 'махать'])
    async def wave(self, ctx,*, member: disnake.Member = None):
        if member and member.bot:
            await check_user(ctx)
        embed = disnake.Embed(color=disnake.Color.from_rgb(47, 50, 55), title="Реакция: Помохать")
        if member is None or member == ctx.author:
            embed.description = f"{ctx.author.mention} приветствует всех"
        else:
            embed.description = f"{ctx.author.mention} приветстувет {member.mention}"
        url = "https://cdn.discordapp.com/attachments/1059171946983604336/" + (random.choice(wave))
        embed.set_image(url=url)
        await ctx.reply(embed=embed)

    @commands.command(name='pat', aliases=['погладить', 'гладить'])
    async def pat(self, ctx,*, member: disnake.Member = None):
        embed = disnake.Embed(color=disnake.Color.from_rgb(47, 50, 55), title="Реакция: Погладить")
        if member is None or member == ctx.author:
            embed.description = f"{ctx.author.mention} гладит всех в чате"
        else:
            embed.description = f"{ctx.author.mention} гладит {member.mention}"
        url = "https://cdn.discordapp.com/attachments/1059172720757194874/" + (random.choice(pat))
        embed.set_image(url=url)
        await ctx.reply(embed=embed)

    @commands.command(name='wink', aliases=['подмигнуть'])
    async def wink(self, ctx,*, member: disnake.Member = None):
        if member and member.bot:
            await check_user(ctx)
        embed = disnake.Embed(color=disnake.Color.from_rgb(47, 50, 55), title="Реакция: Подмигнуть")
        if member is None or member == ctx.author:
            embed.description = f"{ctx.author.mention} подмигивает"
        else:
            embed.description = f"{ctx.author.mention} подмигивает {member.mention}"
        url = "https://cdn.discordapp.com/attachments/1059175444278161509/" + (random.choice(wink))
        embed.set_image(url=url)
        await ctx.reply(embed=embed)

    @commands.command(name='lick', aliases=['лизь', 'облизать', 'лик'])
    async def lick(self, ctx,*, member: disnake.Member = None):
        if member and member.bot:
            await check_user(ctx)
        embed = disnake.Embed(color=disnake.Color.from_rgb(47, 50, 55), title="Реакция: Лизать")
        if member is None or member == ctx.author:
            embed.description = f"{ctx.author.mention} лижет самого себя"
        else:
            embed.description = f"{ctx.author.mention} лижет {member.mention}"
        url = "https://cdn.discordapp.com/attachments/1059177540373192735/" + (random.choice(lick))
        embed.set_image(url=url)
        await ctx.reply(embed=embed)

    @commands.command(name='bonk', aliases=['ударить', 'бонк'])
    async def bonk(self, ctx,*, member: disnake.Member = None):
        embed = disnake.Embed(color=disnake.Color.from_rgb(47, 50, 55), title="Реакция: Ударить")
        if member is None or member == ctx.author:
            embed.description = f"{ctx.author.mention} бьет себя"
        else:
            embed.description = f"{ctx.author.mention} бьет {member.mention}"
        url = "https://cdn.discordapp.com/attachments/1059178858173182042/" + (random.choice(bonk))
        embed.set_image(url=url)
        await ctx.reply(embed=embed)

    @commands.command(name='smile', aliases=['смайл', 'улыбнутся', 'улыбка'])
    async def smile(self, ctx,*, member: disnake.Member = None):
        if member and member.bot:
             await check_user(ctx)
        embed = disnake.Embed(color=disnake.Color.from_rgb(47, 50, 55), title="Реакция: Улыбнутся")
        if member is None or member == ctx.author:
            embed.description = f"{ctx.author.mention} улыбается"
        else:
            embed.description = f"{ctx.author.mention} улыбается {member.mention}"
        url = "https://cdn.discordapp.com/attachments/1059169551775957073/" + (random.choice(smile))
        embed.set_image(url=url)
        await ctx.reply(embed=embed)

    @commands.command(name='happy', aliases=['хэппи', 'счастье'])
    async def happy(self, ctx):
        embed = disnake.Embed(color=disnake.Color.from_rgb(47, 50, 55), title="Реакция: Счастливый")
        embed.description = f"{ctx.author.mention} счастлив"
        url = "https://i.waifu.pics/" + (random.choice(happy))
        embed.set_image(url=url)
        await ctx.reply(embed=embed)

    @commands.command(name='smug', aliases=['самолюбие', 'самодовольный'])
    async def smug(self, ctx):
        embed = disnake.Embed(color=disnake.Color.from_rgb(47, 50, 55), title="Реакция: Самодовольный")
        embed.description = f"{ctx.author.mention} самодоволен"
        url = "https://i.waifu.pics/" + (random.choice(smug))
        embed.set_image(url=url)
        await ctx.reply(embed=embed)

    @commands.command(name='dance', aliases=['танцевать', 'танец', 'дэнс'])
    async def dance(self, ctx,*, member: disnake.Member = None):
        if member and member.bot:
            await check_user(ctx)
        view = Confirm()
        if member==ctx.author or member is None:
            embed = disnake.Embed(color=disnake.Color.from_rgb(47, 50, 55), title="Реакция: Танцевать")
            embed.description = f"{ctx.author.mention} танцует "
            url = "https://cdn.discordapp.com/attachments/1059167103430692954/" + (random.choice(dance))
            embed.set_image(url=url)
            await ctx.send(embed=embed)
        if member==member :
            embed = disnake.Embed(color=disnake.Color.from_rgb(47, 50, 55), title="Реакция: Танцевать",
            description=f'Пользователя {member.mention} пригласил на танец {ctx.author.mention} ')
            message = await ctx.send(embed=embed,view=view)
            await view.wait()
        elif view is None :
            embed=disnake.Embed(title='Реакция:Поцелуй',description=f'{member.mention} проигнорировал / не заметил реакции',color=disnake.Color.from_rgb(47, 50, 55))
            await message.edit(embed=embed)
        elif view.value:
            embed = disnake.Embed(color=disnake.Color.from_rgb(47, 50, 55), title="Реакция: Танцевать")
            embed.description = f"{ctx.author.mention} танцует вместе с {member.mention}"
            url = "https://cdn.discordapp.com/attachments/1059167103430692954/" + (random.choice(dance))
            embed.set_image(url=url)
            await ctx.send(embed=embed)
        else:
            embed = disnake.Embed(color=disnake.Color.from_rgb(47, 50, 55), title="Реакция: Танцевать")
            embed.description=f'{member.mention} отказал вам'
        for child in view.children:
            if isinstance(child, disnake.ui.Button):
                child.disabled = True
                view.clear_items
                await message.edit(view=view)





    

    @commands.command(name='slap', aliases=['пощечина', 'слэп', 'слап'])
    async def slap(self, ctx,*, member: disnake.Member):
        if member.bot:
            return await check_user(ctx)
        embed = disnake.Embed(color=disnake.Color.from_rgb(47, 50, 55), title="Реакция: Пощечина")
        embed.description = f"{ctx.author.mention} дал пощечину {member.mention}"
        if member == ctx.author:
            embed.description = f"{ctx.author.mention} дал пощечину самому себе"
        url = "https://i.waifu.pics/" + (random.choice(slap))
        embed.set_image(url=url)
        await ctx.reply(embed=embed)

    @commands.command(name='squeeze', aliases=['тискать', 'потискать'])
    async def squeeze(self, ctx,*, member: disnake.Member):
        if member.bot:
            return await check_user(ctx)
        embed = disnake.Embed(color=disnake.Color.from_rgb(47, 50, 55), title="Реакция: Тискать")
        embed.description = f"{ctx.author.mention} потискал {member.mention}"
        if member == ctx.author:
            embed.description = f"{ctx.author.mention} потискал самого себя"
        url = "https://media.discordapp.net/attachments/1059553104640610336/" + (random.choice(squeeze))
        embed.set_image(url=url)
        await ctx.reply(embed=embed)

    @commands.command(name='suicide', aliases=['суициднутся', 'вены'])
    async def suicide(self,*, ctx):
        embed = disnake.Embed(color=disnake.Color.from_rgb(47, 50, 55), title="Реакция: Суицид",
                              description=f"{ctx.author.mention} суициднулся")
        embed.set_image(url="https://cdn.discordapp.com/attachments/1059802994058723429/" + (random.choice(suicide))
                            + "/suicide.gif")
        await ctx.reply(embed=embed)

    @commands.command(name='blush', aliases=['краснеть', 'блаш'])
    async def blush(self, ctx):
        embed = disnake.Embed(color=disnake.Color.from_rgb(47, 50, 55), title="Реакция: Краснеть")
        embed.description = f"{ctx.author.mention} покраснел"
        url = "https://cdn.discordapp.com/attachments/1059160467592986725/" + (random.choice(blush)) + '/blush.gif'
        embed.set_image(url=url)
        await ctx.reply(embed=embed)

    @commands.command(name='poke', aliases=['тыкнуть', 'тык'])
    async def poke(self, ctx,*, member: disnake.Member):
        if member.bot:
            return await check_user(ctx)
        embed = disnake.Embed(color=disnake.Color.from_rgb(47, 50, 55), title="Реакция: Тыкнуть")
        embed.description = f"{ctx.author.mention} тыкнул {member.mention}"
        if member == ctx.author:
            embed.description = f"{ctx.author.mention} тыкнул самого себя"
        url = "https://cdn.discordapp.com/attachments/1059831965672558683/" + (random.choice(poke)) + "/poke.gif"
        embed.set_image(url=url)
        await ctx.reply(embed=embed)

    @commands.command(name='love', aliases=['люблю', 'любовь'])
    async def love(self, ctx,*, member: disnake.Member):
        if member == ctx.author:
            return await ctx.send("Ошибка №26: нельзя поцеловать самого себя.", ephemeral=True)
        elif member.bot:
            return await check_user(ctx)
        embed = disnake.Embed(color=disnake.Color.from_rgb(47, 50, 55), title="Реакция: Признание в любви")
        embed.description = f"{ctx.author.mention} признается в любви {member.mention}"
        url = "https://cdn.discordapp.com/attachments/1059831443209068605/" + (random.choice(love)) + "/love.gif"
        embed.set_image(url=url)
        await ctx.reply(embed=embed)

    @commands.command(name='depression', aliases=['тильт', 'депрессия'])
    async def depression(self, ctx,*, member: disnake.Member = None):
        if member and member.bot:
            return await check_user(ctx)
        embed = disnake.Embed(color=disnake.Color.from_rgb(47, 50, 55), title="Реакция: Депрессия")
        member = f"из-за {member.mention}" if member and member != ctx.author else ""
        embed.description = f"{ctx.author.mention} тильтует" + member
        embed.set_image(url=("https://cdn.discordapp.com/attachments/1059862574377742386/"
                             + (random.choice(depression)) + "/depression.gif"))
        await ctx.reply(embed=embed)

    


def setup(bot):
    bot.add_cog(Reaction(bot))
