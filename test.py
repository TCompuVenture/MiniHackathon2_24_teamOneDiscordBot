###API KEYS HERE###

 #IMPORT DISCORD.PY. ALLOWS ACCESS TO DISCORD'S API.
import discord

 #GETS THE CLIENT OBJECT FROM DISCORD.PY. CLIENT IS SYNONYMOUS WITH BOT.
bot = discord.Client(intents=discord.Intents.all())

 #EVENT LISTENER FOR WHEN THE BOT HAS SWITCHED FROM OFFLINE TO ONLINE.
@bot.event
async def on_ready():
    # CREATES A COUNTER TO KEEP TRACK OF HOW MANY GUILDS / SERVERS THE BOT IS CONNECTED TO.
    guild_count = 0

    # LOOPS THROUGH ALL THE GUILD / SERVERS THAT THE BOT IS ASSOCIATED WITH.
    for guild in bot.guilds:
        # PRINT THE SERVER'S ID AND NAME.
        print(f"- {guild.id} (name: {guild.name})")

        # INCREMENTS THE GUILD COUNTER.
        guild_count = guild_count + 1

    # PRINTS HOW MANY GUILDS / SERVERS THE BOT IS IN.
    print(bot.guilds)

@bot.event
async def on_ready():
    channel = bot.get_channel(1297890380578033664)
    await channel.send("** TIC TAC TOE ** \n")
    await channel.send("Type 'Accept' to join\n")

 #EVENT LISTENER FOR WHEN A NEW MESSAGE IS SENT TO A CHANNEL.
@bot.event
async def on_message(message):
    channel = bot.get_channel(1297890380578033664)
    # CHECKS IF THE MESSAGE THAT WAS SENT IS EQUAL TO "HELLO".
    # need to assign player vars
    global player1
    player1 = ""
    global player2
    player2 = ""
    if message.content == "Accept" or message.content == 'accept':
        #check which player slots are available
        if player1 == "":
            player1 = discord.member
            await channel.send("You are player 1")
        elif player2 == "":
            player2 = discord.member
            await channel.send("You are player 2")
        else:
            await channel.send("Game full. Cannot join :((")



        # SENDS BACK A MESSAGE TO THE CHANNEL.
        await message.channel.send("")


bot.run("API TOKEN")