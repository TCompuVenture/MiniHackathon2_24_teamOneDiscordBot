###API KEYS HERE###
from symbol import return_stmt

#IMPORT DISCORD.PY. ALLOWS ACCESS TO DISCORD'S API.
import discord





def create_grid():
    print("Behold, the game board: ")
    board = [[" ", " ", " "],
             [" ", " ", " "],
             [" ", " ", " "]]
    return board

def game():
    board = create_grid()
    #print(board)

async def assignPlayer(x_str):
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
    print(type(discord.member))

 #EVENT LISTENER FOR WHEN A NEW MESSAGE IS SENT TO A CHANNEL.
@bot.event
async def on_message(message):
    channel = bot.get_channel(1297890380578033664)
    #currPlayer = discord.member
    # call to grid function
    #grid = create_grid()
    x_str= str(message.author)
    #assignPlayer(x_str)
    if "Team" in x_str:
        print("bot")
    else:
        print(message.author)





        # SENDS BACK A MESSAGE TO THE CHANNEL.
        #await message.channel.send(grid[0])
        #await message.channel.send(grid[1])
        #await message.channel.send(grid[2])


bot.run("")