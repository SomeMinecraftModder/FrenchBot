# welcome to my mess - Windows XP

import discord
import random

client = discord.Client()

math_game_en = 0  # set variables for the math game
math_game_fr = 0
current_math_channel_fr = None
current_math_channel = None


def read_token():  # read the token
    token_file = open("token.txt")
    return token_file.read()


def generate_random_calcule():  # fonc for the math - generate ramdom calccule
    a = random.randint(1, 50)
    b = random.randint(1, 50)
    good_result = a + b
    random_str = str(a) + "+" + str(b)
    return good_result, random_str


async def about_en(ctx):  # about in english
    embed = discord.Embed(title="About this bot",
                          description="This bot is just a little experiment. \n It just send message when you say some "
                                      "specific stuff :) \n Made by Windows XP#4881",
                          color=0xFF5733)
    await ctx.send(embed=embed)


async def howtonull_en(ctx):  # how to null in english
    embed = discord.Embed(title="How to null",
                          description="This little guide will show you how to null !",
                          color=0x2525F0)
    embed.add_field(name="Method 1", value="Just type \** **", inline=False)
    embed.add_field(name="Method 2", value="Just type \_ _", inline=False)
    embed.add_field(name="Method 3", value="Just copy the following character:᲼", inline=False)
    await ctx.send(embed=embed)


async def about_fr(ctx):  # about in french
    embed = discord.Embed(title="A propos",
                          description="Ce bot est juste une petite experience,\n juste pour le fun ! (:\n créer par "
                                      "Windows XP#4881",
                          color=0xFF5733)
    await ctx.send(embed=embed)


async def howtonull_fr(ctx):  # how to nul in french
    embed = discord.Embed(title="Comment ne rien dire",
                          description="Ce petit guide vous permettra de ne rien dire. litéralement!",
                          color=0x2525F0)
    embed.add_field(name="Methode 1", value="Taper juste \** **", inline=False)
    embed.add_field(name="Methode 2", value="Taper juste \_ _", inline=False)
    embed.add_field(name="Methode 3", value="Il suffit juste de copier le caractère suivant:᲼", inline=False)
    await ctx.send(embed=embed)


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    await client.change_presence(status=discord.Status.idle, activity=discord.Game('EN:Type =help | FR:Tape =aide'))
    # ^^^ set the thing


@client.event  # this is the main part of my mess
async def on_message(message):
    if message.author == client.user:
        return
    # await message.add_reaction("🐔")
    # await message.add_reaction("🐣")
    # await message.add_reaction("🐤")
    # await message.add_reaction("🐓")

    if "language" in message.content:
        await message.channel.send('*Did you know that french is the best language ever ?*')
        await message.channel.send('https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.languagemagazine'
                                   '.com%2Fwp-content%2Fuploads%2F2019%2F07%2Ffrench2-1024x724.jpg&f=1&nofb=1')
    if "food" in message.content:
        await message.channel.send('*Did you know that bread is best food ever ?*')
        await message.channel.send('https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fghisoni-mariotti.com'
                                   '%2Fwp-content%2Fuploads%2F2018%2F11%2FBaguette_Tradition.jpg&f=1&nofb=1')
    if "country" in message.content:
        await message.channel.send('*Did you know that french is the best country ever ?*')
        await message.channel.send('https://lafrenchtech.com/wp-content/uploads/2019/09/French-tech_Visa-1.jpg')
    if "flag" in message.content:
        await message.channel.send('*Did you know that french flag is the best flag ever ?*')
        await message.channel.send('https://c.files.bbci.co.uk/117CC/production/_108582617_041057304-1.jpg')
    if message.content == '=help':
        await message.channel.send('```list of command:\n=help: show this message\n=about: about this bot\n=null: '
                                   'how to null\n=math start: a simple but hard math game\n=math stop: stop the '
                                   'current math game\n=numserver: give the number of server where FrenchBot is in```')
    if message.content == '=aide':
        await message.channel.send('```listes des commandes:\n=aide: affiche ce message\n=apropos: a propos de ce '
                                   'bot\n=rien: un guide pour ne rien dire. littéralement.\n=math commence: un petit '
                                   'jeu '
                                   'sur les math\n=math arrete: stope le jeu de math\n=listeserveur: donne le nombre '
                                   'de serveur dans lequelle il y a FrenchBot '
                                   '```')
    if message.content == "=about":
        await about_en(message.channel)
    if message.content == "=apropos":
        await about_fr(message.channel)
    if message.content == "=rien":
        await howtonull_fr(message.channel)
    if message.content == "=invite":
        await message.channel.send('https://discord.com/api/oauth2/authorize?client_id=829379849902358549&permissions'
                                   '=2148002880&scope=bot')
    if message.content.startswith('=numserver'):
        await message.channel.send("I'm in " + str(len(client.guilds)) + " servers!")
    if message.content.startswith('=listeserveur'):
        await message.channel.send("Je suis dans " + str(len(client.guilds)) + " serveurs!")
    if message.content == "=math start":
        global math_game_en
        global current_math_channel
        current_math_channel = message.channel.mention
        math_game_en = 1
        all_random_calcule = generate_random_calcule()
        random_calcule = all_random_calcule[1]
        global random_calcule_result
        random_calcule_result = all_random_calcule[0]
        await message.channel.send("**The annoying math game has started!**")
        await message.channel.send("The first to respond win!")
        await message.channel.send("what is " + random_calcule + "?")

    if message.content == "=math commence":
        global math_game_fr
        global current_math_channel_fr
        current_math_channel_fr = message.channel.mention
        math_game_fr = 1
        all_random_calcule_fr = generate_random_calcule()
        random_calcule_fr = all_random_calcule_fr[1]
        global random_calcule_result_fr
        random_calcule_result_fr = all_random_calcule_fr[0]
        await message.channel.send("**Le jeu nul de math a commencé!**")
        await message.channel.send("Le premier qui répond gagne !")
        await message.channel.send("Quelle est le resultat de " + random_calcule_fr + "?")

    if math_game_en and message.channel.mention == current_math_channel:
        try:
            int(message.content)
            if random_calcule_result == int(message.content):
                await message.channel.send("Good result!")
                math_game_en = 0
            else:
                await message.channel.send("Nope.")

        except ValueError:
            pass

    if math_game_fr and message.channel.mention == current_math_channel_fr:
        try:
            int(message.content)
            if random_calcule_result_fr == int(message.content):
                await message.channel.send("Bravo!")
                math_game_fr = 0
            else:
                await message.channel.send("Nope...")

        except ValueError:
            pass

    if message.content == "=math stop":
        if math_game_en:
            await message.channel.send("Game stopped !")
            await message.channel.send("The correct result was : %s!" % random_calcule_result)
        else:
            await message.channel.send("The game was already stopped!")
        math_game_en = 0

    if message.content == "=math arrete":
        if math_game_fr:
            await message.channel.send("Le jeu est stopé !")
            await message.channel.send("Le bon resultat est: %s!" % random_calcule_result_fr)
        else:
            await message.channel.send("Le jeu est déjà stopé!")
        math_game_fr = 0
    if message.content == "=null":
        await howtonull_en(message.channel)
    if random.randint(0, 50) == 5:
        await message.channel.send('Fact: french is not *that* hard')
    if random.randint(0, 50) == 5:
        await message.channel.send(
            'https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fmedia.istockphoto.com'
            '%2Fphotos%2Fbaguette-loaf-of-french-bread-baked-food-isolated-on-white-picture'
            '-id172392441%3Fk%3D6%26m%3D172392441%26s%3D612x612%26w%3D0%26h'
            '%3DDxOV2rIX9bvx6fM4EEr0LFBXCc_jNz7YVHMtQzpYDHQ%3D&f=1&nofb=1')


client.run(read_token())
