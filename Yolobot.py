#Imports stuff so the commands can work
import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import logging
import traceback

client = discord.Client()
bot = commands.Bot(command_prefix='~')
bot.remove_command('help')

class Owner():
    def __init__(self, bot):
        self.bot = bot

async def __local_check(self, ctx):  #Sets some things up
    return await self.bot.is_owner(ctx.author)

@bot.event
async def on_ready():  #does more shit
    print("I'm fucking ready, where the fuck are you lol?")
    botchannel = bot.get_channel(439486977490944011)
    await botchannel.send('YoloBot is now online!')
    await bot.change_presence(activity=discord.Game(name='Type ~help!'))
    bot.appinfo = await bot.application_info()

@bot.command()
@commands.is_owner()
async def disconnect(ctx):
    botchannel = bot.get_channel(439486977490944011)
    await botchannel.send('YoloBot is now offline')
    await bot.logout()  #This is the code ran on booting up the bot

@bot.command()
@commands.has_any_role('Your King', 'Admin', 'Mod')
async def mute(ctx, user: discord.Member):
    mute = discord.utils.get(ctx.guild.roles, name='Muted')
    user = ctx.message.author
    await user.add_roles(mute)
    await ctx.say('```css\n That user has been muted.\n```')
    
@bot.command()
async def bottime(ctx):
    t = (2009, 2, 17, 17, 3, 38, 1, 48, 0)
    t = time.mktime(t)
    await ctx.say('The current time is now ' + time.strftime('%H:%M:%S') + ' in my timezone')
    
@bot.event
async def on_message(message):
    if message.content == 'YoloBot is trash':
        await message.channel.send('fuck you too.')
    await bot.process_commands(message)

@bot.command()
@commands.has_any_role('Your King', 'Admin', 'Mod')  #Goes offline
async def roletester(ctx):
    await ctx.send('You have the required role!')

@bot.command()
@commands.has_any_role('Your King', 'Admin')
async def listroles(ctx):
    rolelist = ''
    for r in ctx.guild.roles:  #Some things that don't require you to use the prefix.
        rolelist += '{}: {}\n'.format(r.id, r.name)
    await ctx.send('All roles on this server: \n' + rolelist)

@bot.group(pass_context=True)
async def calculator(ctx):
    if ctx.invoked_subcommand == None:
        await ctx.say('You need to add a function!')

#test bullshit lol
@calculator.command()
async def add(ctx, a: int, b: int):
    if a == None:
        await ctx.say('You need to use 2 numbers!')
    else:
        await ctx.send(a + b)
    
@calculator.command()
async def subtract(ctx, a: int, b: int):  #Lists the roles and their ID's
    if a == None:
        await ctx.say('You need to use 2 numbers!')
    else:
        await ctx.send(a - b)

@calculator.command()
async def multiply(ctx, a: int, b: int):
    if a == None:
        await ctx.say('You need to use 2 numbers!')
    else:
        await ctx.send(a * b)

@calculator.command()
async def divide(ctx, a: int, b: int):  #This is the group of commands for the calculator
    if a == None:
        await ctx.say('You need to use 2 numbers!')
    else:
        await ctx.send(a / b)

@bot.command()
async def ping(ctx):
    if a == None:
        await ctx.say('You need to use 2 numbers!')
    else:
        await ctx.send('`PONG! :P~`')

@bot.command()
async def cookie(ctx):
    await ctx.send(':cookie:')

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await cmd_error(ctx)
    elif isinstance(error, commands.MissingRequiredArgument):
        await cmd_error2(ctx)
    elif isinstance(error, commands.BadArgument):
        await cmd_error3(ctx)
    elif isinstance(error, commands.CheckFailure):
        await cmd_error4(ctx)
    elif isinstance(error, commands.CommandInvokeError():
        await cmd_error5(ctx)
        
#Ping command
async def cmd_error(ctx):
    await ctx.channel.send('```css\nThat command does not exist, did you misspell it?```')

async def cmd_error2(ctx):
    await ctx.channel.send('```css\nYou are missing an argument. Please add one!```')  #Cookie command

async def cmd_error3(ctx):
    await ctx.channel.send('```css\nYou have used an invalid argument. Please use a valid one.```')
    
async def cmd_error4(ctx):
    await ctx.channel.send('```css\nYou do not have permission to use this command.\n```')
    
async def cmd_error5(ctx):
    await ctx.channel.send('```css\nThere seems to have been a problem with the command. Please notify my creator about this.\n```')

@bot.command()
async def help(ctx):
    await ctx.send("```css\nYolobot Help\nDebug commands\n--------------\n~help = Shows the help list\n~ping = tests if the bot responds\n~tatltuae = The answer\n~Cookie = creates a cookie!\n \nUn-categorized commands\n-----------------------\nTime = Shows the time\n \nRole commands\n-------------\n~listroles [requires Mod role or higher] = Lists all roles and their ID's.\n~roletester = Tests to see if the required roles thingy-mobabber works.\n \nModeration Commands\n-------------------\n~mute [Requires Mod role or higher] = Mutes a specified user. *does not currently work.\n \nOther commands\n--------------\n~Calculator <add/subtract/multiply/divide> = A calculator, duh.\n~disconnect [Bot Owner Only] = Disconnects the bot.```")

@bot.command()
async def tatltuae(ctx, member: discord.Member = None):
    if member is None:
        member = ctx.author.mention
    await ctx.send('{0} the answer is 42.'.format(member))

@bot.command()
async def info(ctx, user: discord.Member):
    await ctx.send('The users name is: {}'.format(user.name))
    await ctx.send('The users ID is: {}'.format(user.id))
    await ctx.send('The users status is: {}'.format(user.status))
    await ctx.send('The users highest role is: {}'.format(user.top_role))
    await ctx.send('The user joined at: {}'.format(user.joined_at))

bot.run('NDM4MTc2ODE5MTg3OTQxNDE2.DcTmFw.SoXBcImAbLzB69KHHvb9hqxCIx4')
