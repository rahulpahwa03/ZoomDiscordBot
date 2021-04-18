import discord
from discord.ext import commands
import random
from discord.utils import get
from time import sleep
import pyautogui
import webbrowser

TOKEN = 'ODMyOTU4MDA4Mzc0ODUzNjUy.YHrWmA.HZ9Ic5lzoe_L1AIh058CZOEo0js'

client = commands.Bot(command_prefix='.')

# activity
act = ['Marking attendance', 'Helping you get attendance above 75%', 'I can take class for you']



@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Game(random.choice(act)))
    print('ready')


# help command for class
@client.command()
async def helpclass(ctx):
    title = 'MARK ATTENDACNE BY USING THESE COMMANDS'
    description = '.joinclass - To join the class \n' \
                  '.leavemeeting - To leave the meeting \n' \
                  '.raisehand - To raise hand \n' \
                  '.lowerhand - To lower the hand \n' \
                  '.present = To mark attendance in chat \n'

    embed = discord.Embed(title=title, discription='', color=discord.Colour.green())
    embed.add_field(name=description, value=ctx.author.mention, inline=True)

    msg = await ctx.send(embed=embed)
    await msg.add_reaction('❤')

# meeting join Harsha
@client.command()
async def joinclass(ctx):
    url = 'https://zoom.us/j/4013344534?pwd=aDJtdGdCd281MFRoVTZZcmt2U0V5UT09'
    webbrowser.open(url)
    sleep(7)
    pyautogui.write('JIMSBCA')
    pyautogui.hotkey('enter')
    title = 'JOINED CLASS'
    desc = 'You earned 20 love points'

    embed = discord.Embed(title=title, discription='', color=discord.Colour.green())
    embed.add_field(name=desc, value=ctx.author.mention, inline=True)

    await ctx.send(embed=embed)


# meeting end command
@client.command()
async def leavemeeting(ctx):
    pyautogui.hotkey('alt', 'f4')
    title = 'LEFT CLASS'
    desc = 'You earned 10 love points'

    embed = discord.Embed(title=title, discription='', color=discord.Colour.green())
    embed.add_field(name=desc, value=ctx.author.mention, inline=True)

    await ctx.send(embed=embed)


# raise hand
@client.command()
async def raisehand(ctx):
    pyautogui.hotkey('alt', 'y')
    title = 'HAND RAISED'
    desc = 'You earned 50 love points'

    embed = discord.Embed(title=title, discription='', color=discord.Colour.green())
    embed.add_field(name=desc, value=ctx.author.mention, inline=True)

    await ctx.send(embed=embed)


# lower hand
@client.command()
async def lowerhand(ctx):
    pyautogui.hotkey('alt', 'y')
    title = 'HAND LOWERED'
    desc = 'You earned 30 love points'

    embed = discord.Embed(title=title, discription='', color=discord.Colour.green())
    embed.add_field(name=desc, value=ctx.author.mention, inline=True)

    await ctx.send(embed=embed)


# present in chat
@client.command()
async def present(ctx):
    pyautogui.hotkey('alt', 'h')
    text = "rahul pahwa 0511420219 present"
    pyautogui.write(text)
    pyautogui.press('enter')
    pyautogui.hotkey('alt', 'f4')

    title = 'MARKED PRESENT'
    desc = 'You earned 200 love points'

    embed = discord.Embed(title=title, discription='', color=discord.Colour.green())
    embed.add_field(name=desc, value=ctx.author.mention, inline=True)

    await ctx.send(embed=embed)


client.run(TOKEN)
