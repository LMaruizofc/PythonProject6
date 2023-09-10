import discord, hexacolors, asyncio
from discord.ui import Button
from config import configData
from db.mysql import insertdbMYSQL, verifyidMYSQL

class wl0(discord.ui.View):

    def __init__(self, user, bot) -> None:

        self.user = user

        self.bot = bot

        super().__init__()

    @discord.ui.button(label = 'Iniciar WL', style = discord.ButtonStyle.blurple)
    async def iniciar(self, button: discord.ui.Button, interaction: discord.Interaction):

        if interaction.user.id != self.user.id:

            return

        wl = discord.Embed(color = hexacolors.string('indigo'),
        title = 'Oque é RDM?',
        description =
        '''
1️⃣: Fazer RP de praça
2️⃣: Andar de carro
3️⃣: Matar alguém sem motivo
4️⃣: Matar alguem atropelado
5️⃣: Estacionar o carro em cima de alguem
6️⃣: Estacionar o carro em lugar proibido
        ''')

        wl.set_thumbnail(url = interaction.guild.icon)

        channel = interaction.channel

        def check(m):

            return m.content and m.author.id == interaction.user.id

        try:

            await interaction.response.edit_message(delete_after = 0)

            m1 = await channel.send('Qual o nome e sobrenome do Personagem?')

            msg = await self.bot.wait_for(event = 'message', check = check, timeout = 130)

            nome = str(msg.content)

            await m1.delete()

            await msg.delete()

            def check2(m):

                return m.content and m.author.id == interaction.user.id

            try:

                m2 = await channel.send('Qual seu ID?')

                msg2 = await self.bot.wait_for(event = 'message', check = check2, timeout = 130)

                idperson = int(msg2.content)

                await m2.delete()

                await msg2.delete()

                if verifyidMYSQL(idperson) == 1:

                    await channel.send('Id já existente, verifique novamente seu id')

                    await asyncio.sleep(5)

                    await channel.delete()

                    return

                def check3(m):

                    return m.content and m.author.id == interaction.user.id
                
                try:

                    m3 = await channel.send('Qual a história do seu personagem?')

                    msg3 = await self.bot.wait_for(event = 'message', check = check3, timeout = 130)

                    histo = msg2.content

                    await m3.delete()

                    await msg3.delete()

                    await channel.send(embed = wl, view = wl1(interaction.user, idperson,nome))

                except Exception as error:

                    print(error)

            except Exception as error:

                print(error)

        except Exception as error:

            print(error)

    @discord.ui.button(label = 'Cancelar WL', style = discord.ButtonStyle.blurple)
    async def cancelar(self, button: discord.ui.Button, interaction: discord.Interaction):

        if interaction.user.id != self.user.id:

            return

        await interaction.response.send_message('Whitelist cancelada')

        await asyncio.sleep(2)

        await interaction.channel.delete()
# ---------------------------------------------------------------------
# ---------------------------------------------------------------------
# ---------------------------------------------------------------------
# ---------------------------------------------------------------------
# ---------------------------------------------------------------------
# ---------------------------------------------------------------------
# ---------------------------------------------------------------------
# ---------------------------------------------------------------------
# ---------------------------------------------------------------------
# ---------------------------------------------------------------------
class wl1(discord.ui.View):

    def __init__(self, user, idperson, nome) -> None:

        self.user = user

        self.validador = 0

        self.idperson = idperson,

        self.name = nome

        super().__init__()
    
    @discord.ui.button(label = '1️⃣', style = discord.ButtonStyle.blurple)
    async def w1(self, button: discord.ui.Button, interaction: discord.Interaction):

        id = self.idperson[0]

        nome = self.name
        wl = discord.Embed(color = hexacolors.string('indigo'),
        title = 'Oque é VDM?',
        description =
        '''
1️⃣: É ficar irritando uma pessoa
2️⃣: Andar de carro
3️⃣: Matar alguém sem motivo
4️⃣: Pular de paraquedas de um lugar alto
5️⃣: Usar algum veiculo para matar alguem
6️⃣: Estacionar o carro em lugar proibido
        ''')

        wl.set_thumbnail(url = interaction.guild.icon)

        if interaction.user.id != self.user.id:

            return
        
        validar = self.validador

        await interaction.response.edit_message(embed = wl, view = wl2(interaction.user, id, nome,validar))

    @discord.ui.button(label = '2️⃣', style = discord.ButtonStyle.blurple)
    async def w2(self, button: discord.ui.Button, interaction: discord.Interaction):
        
        id = self.idperson[0]

        nome = self.name

        wl = discord.Embed(color = hexacolors.string('indigo'),
        title = 'Oque é VDM?',
        description =
        '''
1️⃣: É ficar irritando uma pessoa
2️⃣: Andar de carro
3️⃣: Matar alguém sem motivo
4️⃣: Pular de paraquedas de um lugar alto
5️⃣: Usar algum veiculo para matar alguem
6️⃣: Estacionar o carro em lugar proibido
        ''')

        wl.set_thumbnail(url = interaction.guild.icon)

        if interaction.user.id != self.user.id:

            return
        
        validar = self.validador

        await interaction.response.edit_message(embed = wl, view = wl2(interaction.user, id, nome,validar))

    @discord.ui.button(label = '3️⃣', style = discord.ButtonStyle.blurple)
    async def w3(self, button: discord.ui.Button, interaction: discord.Interaction):

        id = self.idperson[0]

        nome = self.name

        wl = discord.Embed(color = hexacolors.string('indigo'),
        title = 'Oque é VDM?',
        description =
        '''
1️⃣: É ficar irritando uma pessoa
2️⃣: Andar de carro
3️⃣: Matar alguém sem motivo
4️⃣: Pular de paraquedas de um lugar alto
5️⃣: Usar algum veiculo para matar alguem
6️⃣: Estacionar o carro em lugar proibido
        ''')

        wl.set_thumbnail(url = interaction.guild.icon)

        if interaction.user.id != self.user.id:

            return

        self.validador += 1

        validar = self.validador

        await interaction.response.edit_message(embed = wl, view = wl2(interaction.user, id, nome,validar))

    @discord.ui.button(label = '4️⃣', style = discord.ButtonStyle.blurple)
    async def w4(self, button: discord.ui.Button, interaction: discord.Interaction):

        id = self.idperson[0]

        nome = self.name

        wl = discord.Embed(color = hexacolors.string('indigo'),
        title = 'Oque é VDM?',
        description =
        '''
1️⃣: É ficar irritando uma pessoa
2️⃣: Andar de carro
3️⃣: Matar alguém sem motivo
4️⃣: Pular de paraquedas de um lugar alto
5️⃣: Usar algum veiculo para matar alguem
6️⃣: Estacionar o carro em lugar proibido
        ''')

        wl.set_thumbnail(url = interaction.guild.icon)

        if interaction.user.id != self.user.id:

            return
        
        validar = self.validador

        await interaction.response.edit_message(embed = wl, view = wl2(interaction.user, id, nome,validar))

    @discord.ui.button(label = '5️⃣', style = discord.ButtonStyle.blurple)
    async def w5(self, button: discord.ui.Button, interaction: discord.Interaction):

        id = self.idperson[0]

        nome = self.name

        wl = discord.Embed(color = hexacolors.string('indigo'),
        title = 'Oque é VDM?',
        description =
        '''
1️⃣: É ficar irritando uma pessoa
2️⃣: Andar de carro
3️⃣: Matar alguém sem motivo
4️⃣: Pular de paraquedas de um lugar alto
5️⃣: Usar algum veiculo para matar alguem
6️⃣: Estacionar o carro em lugar proibido
        ''')

        wl.set_thumbnail(url = interaction.guild.icon)

        if interaction.user.id != self.user.id:

            return
        
        validar = self.validador

        await interaction.response.edit_message(embed = wl, view = wl2(interaction.user, id, nome,validar))
    
    @discord.ui.button(label = '6️⃣', style = discord.ButtonStyle.blurple)
    async def w6(self, button: discord.ui.Button, interaction: discord.Interaction):

        id = self.idperson[0]

        nome = self.name

        wl = discord.Embed(color = hexacolors.string('indigo'),
        title = 'Oque é VDM?',
        description =
        '''
1️⃣: É ficar irritando uma pessoa
2️⃣: Andar de carro
3️⃣: Matar alguém sem motivo
4️⃣: Pular de paraquedas de um lugar alto
5️⃣: Usar algum veiculo para matar alguem
6️⃣: Estacionar o carro em lugar proibido
        ''')

        wl.set_thumbnail(url = interaction.guild.icon)

        if interaction.user.id != self.user.id:

            return
        
        validar = self.validador

        await interaction.response.edit_message(embed = wl, view = wl2(interaction.user, id, nome,validar))
# ---------------------------------------------------------------------
# ---------------------------------------------------------------------
# ---------------------------------------------------------------------
# ---------------------------------------------------------------------
# ---------------------------------------------------------------------
# ---------------------------------------------------------------------
# ---------------------------------------------------------------------
# ---------------------------------------------------------------------
# ---------------------------------------------------------------------
# ---------------------------------------------------------------------
class wl2(discord.ui.View):

    def __init__(self, user, idperson, nome, validador) -> None:

        self.user = user

        self.validador = validador

        self.idperson = idperson,

        self.name = nome

        super().__init__()
    
    @discord.ui.button(label = '1️⃣', style = discord.ButtonStyle.blurple)
    async def w1(self, button: discord.ui.Button, interaction: discord.Interaction):

        id = self.idperson[0]

        nome = self.name

        wl = discord.Embed(color = hexacolors.string('indigo'),
        title = 'O que é RP?',
        description =
        '''
1️⃣: Escutar Rock Paulera
2️⃣: Reduzir a punição na cidade
3️⃣: É representar um policial
4️⃣: São lugares onde não se pode roubar ou matar
5️⃣: É utilizar informações de fora do game
6️⃣: É viver o personagem dentro do jogo como se fosse você
        ''')

        wl.set_thumbnail(url = interaction.guild.icon)

        if interaction.user.id != self.user.id:

            return
        
        validar = self.validador

        await interaction.response.edit_message(embed = wl, view = wl3(interaction.user, id, nome, validar))

    @discord.ui.button(label = '2️⃣', style = discord.ButtonStyle.blurple)
    async def w2(self, button: discord.ui.Button, interaction: discord.Interaction):
        
        id = self.idperson[0]

        nome = self.name

        wl = discord.Embed(color = hexacolors.string('indigo'),
        title = 'O que é RP?',
        description =
        '''
1️⃣: Escutar Rock Paulera
2️⃣: Reduzir a punição na cidade
3️⃣: É representar um policial
4️⃣: São lugares onde não se pode roubar ou matar
5️⃣: É utilizar informações de fora do game
6️⃣: É viver o personagem dentro do jogo como se fosse você
        ''')

        wl.set_thumbnail(url = interaction.guild.icon)

        wl.set_thumbnail(url = interaction.guild.icon)

        if interaction.user.id != self.user.id:

            return
        
        validar = self.validador

        await interaction.response.edit_message(embed = wl, view = wl3(interaction.user, id, nome, validar))

    @discord.ui.button(label = '3️⃣', style = discord.ButtonStyle.blurple)
    async def w3(self, button: discord.ui.Button, interaction: discord.Interaction):

        id = self.idperson[0]

        nome = self.name

        wl = discord.Embed(color = hexacolors.string('indigo'),
        title = 'O que é RP?',
        description =
        '''
1️⃣: Escutar Rock Paulera
2️⃣: Reduzir a punição na cidade
3️⃣: É representar um policial
4️⃣: São lugares onde não se pode roubar ou matar
5️⃣: É utilizar informações de fora do game
6️⃣: É viver o personagem dentro do jogo como se fosse você
        ''')

        wl.set_thumbnail(url = interaction.guild.icon)

        wl.set_thumbnail(url = interaction.guild.icon)

        if interaction.user.id != self.user.id:

            return
    
        validar = self.validador

        await interaction.response.edit_message(embed = wl, view = wl3(interaction.user, id, nome, validar))

    @discord.ui.button(label = '4️⃣', style = discord.ButtonStyle.blurple)
    async def w4(self, button: discord.ui.Button, interaction: discord.Interaction):

        id = self.idperson[0]

        nome = self.name

        wl = discord.Embed(color = hexacolors.string('indigo'),
        title = 'O que é RP?',
        description =
        '''
1️⃣: Escutar Rock Paulera
2️⃣: Reduzir a punição na cidade
3️⃣: É representar um policial
4️⃣: São lugares onde não se pode roubar ou matar
5️⃣: É utilizar informações de fora do game
6️⃣: É viver o personagem dentro do jogo como se fosse você
        ''')

        wl.set_thumbnail(url = interaction.guild.icon)

        wl.set_thumbnail(url = interaction.guild.icon)

        if interaction.user.id != self.user.id:

            return
        
        validar = self.validador

        await interaction.response.edit_message(embed = wl, view = wl3(interaction.user, id, nome, validar))

    @discord.ui.button(label = '5️⃣', style = discord.ButtonStyle.blurple)
    async def w5(self, button: discord.ui.Button, interaction: discord.Interaction):

        id = self.idperson[0]

        nome = self.name

        wl = discord.Embed(color = hexacolors.string('indigo'),
        title = 'O que é RP?',
        description =
        '''
1️⃣: Escutar Rock Paulera
2️⃣: Reduzir a punição na cidade
3️⃣: É representar um policial
4️⃣: São lugares onde não se pode roubar ou matar
5️⃣: É utilizar informações de fora do game
6️⃣: É viver o personagem dentro do jogo como se fosse você
        ''')

        wl.set_thumbnail(url = interaction.guild.icon)

        if interaction.user.id != self.user.id:

            return
        
        self.validador += 1
        
        validar = self.validador

        await interaction.response.edit_message(embed = wl, view = wl3(interaction.user, id, nome, validar))
    
    @discord.ui.button(label = '6️⃣', style = discord.ButtonStyle.blurple)
    async def w6(self, button: discord.ui.Button, interaction: discord.Interaction):

        id = self.idperson[0]

        nome = self.name

        wl = discord.Embed(color = hexacolors.string('indigo'),
        title = 'O que é RP?',
        description =
        '''
1️⃣: Escutar Rock Paulera
2️⃣: Reduzir a punição na cidade
3️⃣: É representar um policial
4️⃣: São lugares onde não se pode roubar ou matar
5️⃣: É utilizar informações de fora do game
6️⃣: É viver o personagem dentro do jogo como se fosse você
        ''')

        wl.set_thumbnail(url = interaction.guild.icon)

        if interaction.user.id != self.user.id:

            return
        
        validar = self.validador

        await interaction.response.edit_message(embed = wl, view = wl3(interaction.user, id, nome, validar))
# ---------------------------------------------------------------------
# ---------------------------------------------------------------------
# ---------------------------------------------------------------------
# ---------------------------------------------------------------------
# ---------------------------------------------------------------------
# ---------------------------------------------------------------------
# ---------------------------------------------------------------------
# ---------------------------------------------------------------------
# ---------------------------------------------------------------------
# ---------------------------------------------------------------------
class wl3(discord.ui.View):

    def __init__(self, user, idperson, nome, validador) -> None:

        self.user = user

        self.validador = validador

        self.idperson = idperson,

        self.name = nome

        super().__init__()
    
    @discord.ui.button(label = '1️⃣', style = discord.ButtonStyle.blurple)
    async def w1(self, button: discord.ui.Button, interaction: discord.Interaction):

        id = self.idperson[0]

        nome = self.name

        wl = discord.Embed(color = hexacolors.string('indigo'),
        title = 'O que é CL?',
        description =
        '''
1️⃣: É deslogar no meio de uma ação e não voltar
2️⃣: Valorizar a sua vida como se ela fosse unica e ela é
3️⃣: É utilizar um carro como arma
4️⃣: É deslogar da cidade
5️⃣: É fazer Anti-RP
6️⃣: É Reagir a voz de assalto
        ''')

        wl.set_thumbnail(url = interaction.guild.icon)

        if interaction.user.id != self.user.id:

            return
        
        validar = self.validador

        await interaction.response.edit_message(embed = wl, view = wl4(interaction.user, id, nome, validar))

    @discord.ui.button(label = '2️⃣', style = discord.ButtonStyle.blurple)
    async def w2(self, button: discord.ui.Button, interaction: discord.Interaction):
        
        id = self.idperson[0]

        nome = self.name

        wl = discord.Embed(color = hexacolors.string('indigo'),
        title = 'O que é CL?',
        description =
        '''
1️⃣: É deslogar no meio de uma ação e não voltar
2️⃣: Valorizar a sua vida como se ela fosse unica e ela é
3️⃣: É utilizar um carro como arma
4️⃣: É deslogar da cidade
5️⃣: É fazer Anti-RP
6️⃣: É Reagir a voz de assalto
        ''')

        wl.set_thumbnail(url = interaction.guild.icon)

        wl.set_thumbnail(url = interaction.guild.icon)

        if interaction.user.id != self.user.id:

            return
        
        validar = self.validador

        await interaction.response.edit_message(embed = wl, view = wl4(interaction.user, id, nome, validar))

    @discord.ui.button(label = '3️⃣', style = discord.ButtonStyle.blurple)
    async def w3(self, button: discord.ui.Button, interaction: discord.Interaction):

        id = self.idperson[0]

        nome = self.name

        wl = discord.Embed(color = hexacolors.string('indigo'),
        title = 'O que é CL?',
        description =
        '''
1️⃣: É deslogar no meio de uma ação e não voltar
2️⃣: Valorizar a sua vida como se ela fosse unica e ela é
3️⃣: É utilizar um carro como arma
4️⃣: É deslogar da cidade
5️⃣: É fazer Anti-RP
6️⃣: É Reagir a voz de assalto
        ''')

        wl.set_thumbnail(url = interaction.guild.icon)

        wl.set_thumbnail(url = interaction.guild.icon)

        if interaction.user.id != self.user.id:

            return
    
        validar = self.validador

        await interaction.response.edit_message(embed = wl, view = wl4(interaction.user, id, nome, validar))

    @discord.ui.button(label = '4️⃣', style = discord.ButtonStyle.blurple)
    async def w4(self, button: discord.ui.Button, interaction: discord.Interaction):

        id = self.idperson[0]

        nome = self.name

        wl = discord.Embed(color = hexacolors.string('indigo'),
        title = 'O que é CL?',
        description =
        '''
1️⃣: É deslogar no meio de uma ação e não voltar
2️⃣: Valorizar a sua vida como se ela fosse unica e ela é
3️⃣: É utilizar um carro como arma
4️⃣: É deslogar da cidade
5️⃣: É fazer Anti-RP
6️⃣: É Reagir a voz de assalto
        ''')

        wl.set_thumbnail(url = interaction.guild.icon)

        wl.set_thumbnail(url = interaction.guild.icon)

        if interaction.user.id != self.user.id:

            return
        
        validar = self.validador

        await interaction.response.edit_message(embed = wl, view = wl4(interaction.user, id, nome, validar))

    @discord.ui.button(label = '5️⃣', style = discord.ButtonStyle.blurple)
    async def w5(self, button: discord.ui.Button, interaction: discord.Interaction):

        id = self.idperson[0]

        nome = self.name

        wl = discord.Embed(color = hexacolors.string('indigo'),
        title = 'O que é CL?',
        description =
        '''
1️⃣: É deslogar no meio de uma ação e não voltar
2️⃣: Valorizar a sua vida como se ela fosse unica e ela é
3️⃣: É utilizar um carro como arma
4️⃣: É deslogar da cidade
5️⃣: É fazer Anti-RP
6️⃣: É Reagir a voz de assalto
        ''')

        wl.set_thumbnail(url = interaction.guild.icon)

        if interaction.user.id != self.user.id:

            return
        
        validar = self.validador

        await interaction.response.edit_message(embed = wl, view = wl4(interaction.user, id, nome, validar))
    
    @discord.ui.button(label = '6️⃣', style = discord.ButtonStyle.blurple)
    async def w6(self, button: discord.ui.Button, interaction: discord.Interaction):

        id = self.idperson[0]

        nome = self.name

        wl = discord.Embed(color = hexacolors.string('indigo'),
        title = 'O que é CL?',
        description =
        '''
1️⃣: É deslogar no meio de uma ação e não voltar
2️⃣: Valorizar a sua vida como se ela fosse unica e ela é
3️⃣: É utilizar um carro como arma
4️⃣: É deslogar da cidade
5️⃣: É fazer Anti-RP
6️⃣: É Reagir a voz de assalto
        ''')

        wl.set_thumbnail(url = interaction.guild.icon)

        if interaction.user.id != self.user.id:

            return

        self.validador += 1
        
        validar = self.validador

        await interaction.response.edit_message(embed = wl, view = wl4(interaction.user, id, nome, validar))
# ---------------------------------------------------------------------
# ---------------------------------------------------------------------
# ---------------------------------------------------------------------
# ---------------------------------------------------------------------
# ---------------------------------------------------------------------
# ---------------------------------------------------------------------
# ---------------------------------------------------------------------
# ---------------------------------------------------------------------
# ---------------------------------------------------------------------
# ---------------------------------------------------------------------
class wl4(discord.ui.View):

    def __init__(self, user, idperson, nome, validador) -> None:

        self.user = user

        self.validador = validador

        self.idperson = idperson,

        self.name = nome

        super().__init__()
    
    @discord.ui.button(label = '1️⃣', style = discord.ButtonStyle.blurple)
    async def w1(self, button: discord.ui.Button, interaction: discord.Interaction):

        id = self.idperson[0]

        nome = self.name

        wl = discord.Embed(color = hexacolors.string('indigo'),
        title = 'O que é Anti-RP?',
        description =
        '''
1️⃣: É fazer rp de cego dentro da cidade
2️⃣: É fazer algo que você não faria na vida real ou sair do personagem
3️⃣: É fazer RP de acedio/estupro
4️⃣: É dirigir sem habilitação
5️⃣: É matar pessoas aleatorias sem motivo
6️⃣: É Jogar jogo dentro da cidade
        ''')

        wl.set_thumbnail(url = interaction.guild.icon)

        if interaction.user.id != self.user.id:

            return
        
        self.validador += 1
        
        validar = self.validador

        await interaction.response.edit_message(embed = wl, view = wl5(interaction.user, id, nome, validar))

    @discord.ui.button(label = '2️⃣', style = discord.ButtonStyle.blurple)
    async def w2(self, button: discord.ui.Button, interaction: discord.Interaction):
        
        id = self.idperson[0]

        nome = self.name

        wl = discord.Embed(color = hexacolors.string('indigo'),
        title = 'O que é Anti-RP?',
        description =
        '''
1️⃣: É fazer rp de cego dentro da cidade
2️⃣: É fazer algo que você não faria na vida real ou sair do personagem
3️⃣: É fazer RP de acedio/estupro
4️⃣: É dirigir sem habilitação
5️⃣: É matar pessoas aleatorias sem motivo
6️⃣: É Jogar jogo dentro da cidade
        ''')

        wl.set_thumbnail(url = interaction.guild.icon)

        wl.set_thumbnail(url = interaction.guild.icon)

        if interaction.user.id != self.user.id:

            return
        
        validar = self.validador

        await interaction.response.edit_message(embed = wl, view = wl5(interaction.user, id, nome, validar))

    @discord.ui.button(label = '3️⃣', style = discord.ButtonStyle.blurple)
    async def w3(self, button: discord.ui.Button, interaction: discord.Interaction):

        id = self.idperson[0]

        nome = self.name

        wl = discord.Embed(color = hexacolors.string('indigo'),
        title = 'O que é Anti-RP?',
        description =
        '''
1️⃣: É fazer rp de cego dentro da cidade
2️⃣: É fazer algo que você não faria na vida real ou sair do personagem
3️⃣: É fazer RP de acedio/estupro
4️⃣: É dirigir sem habilitação
5️⃣: É matar pessoas aleatorias sem motivo
6️⃣: É Jogar jogo dentro da cidade
        ''')

        wl.set_thumbnail(url = interaction.guild.icon)

        wl.set_thumbnail(url = interaction.guild.icon)

        if interaction.user.id != self.user.id:

            return
    
        validar = self.validador

        await interaction.response.edit_message(embed = wl, view = wl5(interaction.user, id, nome, validar))

    @discord.ui.button(label = '4️⃣', style = discord.ButtonStyle.blurple)
    async def w4(self, button: discord.ui.Button, interaction: discord.Interaction):

        id = self.idperson[0]

        nome = self.name

        wl = discord.Embed(color = hexacolors.string('indigo'),
        title = 'O que é Anti-RP?',
        description =
        '''
1️⃣: É fazer rp de cego dentro da cidade
2️⃣: É fazer algo que você não faria na vida real ou sair do personagem
3️⃣: É fazer RP de acedio/estupro
4️⃣: É dirigir sem habilitação
5️⃣: É matar pessoas aleatorias sem motivo
6️⃣: É Jogar jogo dentro da cidade
        ''')

        wl.set_thumbnail(url = interaction.guild.icon)

        wl.set_thumbnail(url = interaction.guild.icon)

        if interaction.user.id != self.user.id:

            return
        
        validar = self.validador

        await interaction.response.edit_message(embed = wl, view = wl5(interaction.user, id, nome, validar))

    @discord.ui.button(label = '5️⃣', style = discord.ButtonStyle.blurple)
    async def w5(self, button: discord.ui.Button, interaction: discord.Interaction):

        id = self.idperson[0]

        nome = self.name

        wl = discord.Embed(color = hexacolors.string('indigo'),
        title = 'O que é Anti-RP?',
        description =
        '''
1️⃣: É fazer rp de cego dentro da cidade
2️⃣: É fazer algo que você não faria na vida real ou sair do personagem
3️⃣: É fazer RP de acedio/estupro
4️⃣: É dirigir sem habilitação
5️⃣: É matar pessoas aleatorias sem motivo
6️⃣: É Jogar jogo dentro da cidade
        ''')

        wl.set_thumbnail(url = interaction.guild.icon)

        if interaction.user.id != self.user.id:

            return
        
        validar = self.validador

        await interaction.response.edit_message(embed = wl, view = wl5(interaction.user, id, nome, validar))
    
    @discord.ui.button(label = '6️⃣', style = discord.ButtonStyle.blurple)
    async def w6(self, button: discord.ui.Button, interaction: discord.Interaction):

        id = self.idperson[0]

        nome = self.name
        wl = discord.Embed(color = hexacolors.string('indigo'),
        title = 'O que é Anti-RP?',
        description =
        '''
1️⃣: É fazer rp de cego dentro da cidade
2️⃣: É fazer algo que você não faria na vida real ou sair do personagem
3️⃣: É fazer RP de acedio/estupro
4️⃣: É dirigir sem habilitação
5️⃣: É matar pessoas aleatorias sem motivo
6️⃣: É Jogar jogo dentro da cidade
        ''')

        wl.set_thumbnail(url = interaction.guild.icon)

        if interaction.user.id != self.user.id:

            return
        
        validar = self.validador

        await interaction.response.edit_message(embed = wl, view = wl5(interaction.user, id, nome, validar))
# ---------------------------------------------------------------------
# ---------------------------------------------------------------------
# ---------------------------------------------------------------------
# ---------------------------------------------------------------------
# ---------------------------------------------------------------------
# ---------------------------------------------------------------------
# ---------------------------------------------------------------------
# ---------------------------------------------------------------------
# ---------------------------------------------------------------------
# ---------------------------------------------------------------------
class wl5(discord.ui.View):

    def __init__(self, user, idperson, nome, validador) -> None:

        self.user = user

        self.validador = validador

        self.idperson = idperson,

        self.name = nome

        super().__init__()
    
    @discord.ui.button(label = '1️⃣', style = discord.ButtonStyle.blurple)
    async def w1(self, button: discord.ui.Button, interaction: discord.Interaction):

        channel = interaction.channel

        id = self.idperson[0]

        if interaction.user.id != self.user.id:

            return

        if self.validador == 5:

            await interaction.response.edit_message(delete_after = 0)

            await channel.send('WL finalizada, estou analizando suas respostas', delete_after = 2)

            await asyncio.sleep(3)

            await channel.send(f'Parabens, você passou na WL do {interaction.guild.name}')

            insertdbMYSQL(id)

            await interaction.user.add_roles(discord.utils.get(interaction.guild.roles, id = configData['cargos']['cidadao']))

            await interaction.user.remove_roles(discord.utils.get(interaction.guild.roles, id = configData['cargos']['semwl']))

            await asyncio.sleep(2)

            await channel.delete()
        
        else:

            await channel.send('WL finalizada, estou analizando suas respostas', delete_after = 2)

            await asyncio.sleep(3)

            await channel.send(f'Infelizmente você não passou na WL, tente novamente')

            await asyncio.sleep(2)

            await channel.delete()

    @discord.ui.button(label = '2️⃣', style = discord.ButtonStyle.blurple)
    async def w2(self, button: discord.ui.Button, interaction: discord.Interaction):

        channel = interaction.channel
    
        id = self.idperson[0]

        nome = self.name

        if interaction.user.id != self.user.id:

            return

        self.validador += 1

        if self.validador == 5:

            await interaction.response.edit_message(delete_after = 0)

            await channel.send('WL finalizada, estou analizando suas respostas', delete_after = 2)

            await asyncio.sleep(3)

            await channel.send(f'Parabens, você passou na WL do {interaction.guild.name}')

            insertdbMYSQL(id)

            await interaction.user.add_roles(discord.utils.get(interaction.guild.roles, id = configData['cargos']['cidadao']))

            await interaction.user.remove_roles(discord.utils.get(interaction.guild.roles, id = configData['cargos']['semwl']))

            await asyncio.sleep(3)

            await channel.delete()
        
        else:

            await channel.send('WL finalizada, estou analizando suas respostas', delete_after = 2)

            await asyncio.sleep(3)

            await channel.send(f'Infelizmente você não passou na WL, tente novamente')

            await asyncio.sleep(3)

            await channel.delete()

    @discord.ui.button(label = '3️⃣', style = discord.ButtonStyle.blurple)
    async def w3(self, button: discord.ui.Button, interaction: discord.Interaction):

        channel = interaction.channel

        id = self.idperson[0]

        nome = self.name

        if interaction.user.id != self.user.id:

            return

        if self.validador == 5:

            await interaction.response.edit_message(delete_after = 0)

            await channel.send('WL finalizada, estou analizando suas respostas', delete_after = 2)

            await asyncio.sleep(3)

            await channel.send(f'Parabens, você passou na WL do {interaction.guild.name}')

            insertdbMYSQL(id)

            await interaction.user.add_roles(discord.utils.get(interaction.guild.roles, id = configData['cargos']['cidadao']))

            await interaction.user.remove_roles(discord.utils.get(interaction.guild.roles, id = configData['cargos']['semwl']))

            await asyncio.sleep(3)

            await channel.delete()
        
        else:

            await channel.send('WL finalizada, estou analizando suas respostas', delete_after = 2)

            await asyncio.sleep(3)

            await channel.send(f'Infelizmente você não passou na WL, tente novamente')

            await asyncio.sleep(3)

            await channel.delete()

    @discord.ui.button(label = '4️⃣', style = discord.ButtonStyle.blurple)
    async def w4(self, button: discord.ui.Button, interaction: discord.Interaction):

        channel = interaction.channel

        id = self.idperson[0]

        nome = self.name

        if interaction.user.id != self.user.id:

            return

        if self.validador == 5:

            await interaction.response.edit_message(delete_after = 0)

            await channel.send('WL finalizada, estou analizando suas respostas', delete_after = 2)

            await asyncio.sleep(3)

            await channel.send(f'Parabens, você passou na WL do {interaction.guild.name}')

            insertdbMYSQL(id)

            await interaction.user.add_roles(discord.utils.get(interaction.guild.roles, id = configData['cargos']['cidadao']))

            await interaction.user.remove_roles(discord.utils.get(interaction.guild.roles, id = configData['cargos']['semwl']))

            await asyncio.sleep(3)

            await channel.delete()
        
        else:

            await channel.send('WL finalizada, estou analizando suas respostas', delete_after = 2)

            await asyncio.sleep(3)

            await channel.send(f'Infelizmente você não passou na WL, tente novamente')

            await asyncio.sleep(3)

            await channel.delete()

    @discord.ui.button(label = '5️⃣', style = discord.ButtonStyle.blurple)
    async def w5(self, button: discord.ui.Button, interaction: discord.Interaction):

        channel = interaction.channel

        id = self.idperson[0]

        nome = self.name

        if interaction.user.id != self.user.id:

            return

        if self.validador == 5:

            await interaction.response.edit_message(delete_after = 0)

            await channel.send('WL finalizada, estou analizando suas respostas', delete_after = 2)

            await asyncio.sleep(3)

            await channel.send(f'Parabens, você passou na WL do {interaction.guild.name}')

            insertdbMYSQL(id)

            await interaction.user.add_roles(discord.utils.get(interaction.guild.roles, id = configData['cargos']['cidadao']))

            await interaction.user.remove_roles(discord.utils.get(interaction.guild.roles, id = configData['cargos']['semwl']))

            await asyncio.sleep(3)

            await channel.delete()

        else:

            await channel.send('WL finalizada, estou analizando suas respostas', delete_after = 2)

            await asyncio.sleep(3)

            await channel.send(f'Infelizmente você não passou na WL, tente novamente')

            await asyncio.sleep(3)

            await channel.delete()

    @discord.ui.button(label = '6️⃣', style = discord.ButtonStyle.blurple)
    async def w6(self, button: discord.ui.Button, interaction: discord.Interaction):

        channel = interaction.channel

        id = self.idperson[0]

        nome = self.name

        if interaction.user.id != self.user.id:

            return

        if self.validador == 5:

            await interaction.response.edit_message(delete_after = 0)

            await channel.send('WL finalizada, estou analizando suas respostas', delete_after = 2)

            await asyncio.sleep(3)

            await channel.send(f'Parabens, você passou na WL do {interaction.guild.name}')

            insertdbMYSQL(id)

            await interaction.user.add_roles(discord.utils.get(interaction.guild.roles, id = configData['cargos']['cidadao']))

            await interaction.user.remove_roles(discord.utils.get(interaction.guild.roles, id = configData['cargos']['semwl']))

            await asyncio.sleep(3)

            await channel.delete()
        
        else:

            await channel.send('WL finalizada, estou analizando suas respostas', delete_after = 2)

            await asyncio.sleep(3)

            await channel.send(f'Infelizmente você não passou na WL, tente novamente')

            await asyncio.sleep(3)

            await channel.delete()

class jumpto(Button):

    def __init__(self, url):

        super().__init__(

            label = 'Atalho para a Wl',

            style=discord.ButtonStyle.url,
        
            url = url
        )
    async def callback(self, button: discord.ui.Button, interaction: discord.Interaction):

        pass