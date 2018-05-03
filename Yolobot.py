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

startup_extensions = ["cogs"]

class Owner():
    def __init__(self, bot):
        self.bot = bot

async def __local_check(self, ctx):  #Sets some things up
    return await self.bot.is_owner(ctx.author)

@bot.event
async def on_ready():  #does more shit
    print("YoloBot is now online!")
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
    await user.add_roles(mute)
    await ctx.send('```css\n That user has been muted.\n```')
    
@bot.command()
async def bottime(ctx):
    t = (2009, 2, 17, 17, 3, 38, 1, 48, 0)
    t = time.mktime(t)
    await ctx.send('The current time is now ' + time.strftime('%H:%M:%S') + ' in my timezone')
    
@bot.event
async def on_message(message):
    if message.content == 'YoloBot is trash':
        await message.channel.send('fuck you too.')
    elif message.content == 'die in a hole':
        await message.channel.send('stfu')
    elif message.content == 'yolobot is a bot that is made by yolotroll101':
        await message.channel.send('That is 100 percent true! :grin:')
    await bot.process_commands(message)

@bot.command()
@commands.has_any_role('Your King', 'Admin')
async def createrole(ctx, a: int):
    guild = ctx.guild
    await guild.create_role(name=a)
    
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
        await ctx.send('`PONG! :P~`')
        
@bot.command()
async def load(extention_name : "cogs"):
    try:
        bot.load_extension(extension_name)
    except (AttributeError, ImportError) as e:
        await bot.say("```py\n{}: {}\n```".format(type(e).__name__, str(e)))
    return
    await bot.say("{} loaded.".format(extension_name))
        
@bot.command()
async def cookie(ctx):
    await ctx.send(':cookie:')

@bot.command()
async def botinfo(ctx):
    embed = discord.Embed(title="YoloBot", description="Yolotroll101's first bot! I'm currently under construction!", color=0x00FF00)
    
    # give info about you here
    embed.add_field(name="My creator:", value="Yolotroll101")
    
    # Shows the number of servers the bot is member of.
    embed.add_field(name="How many servers I'm on:", value=f"{len(bot.guilds)}")

    # give users a link to invite thsi bot to their server
    embed.add_field(name="Invite me here:", value="https://discordapp.com/oauth2/authorize?client_id=438176819187941416&scope=YoloBot&permissions=2146958591")
    
    embed.add_field(name="Donate to my creator for better updates!", value="paypal.me/YoloBot")

    await ctx.send(embed=embed)
    
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
    elif isinstance(error, commands.CommandInvokeError):
        await cmd_error5(ctx)
        raise error
        
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
    await ctx.send("```css\nYolobot Help\nDebug commands\n--------------\n~help = Shows the help list\n~ping = tests if the bot responds\n~tatltuae = The answer\n~Cookie = creates a cookie!\n \nUn-categorized commands\n-----------------------\nTime = Shows the time\n \nRole commands\n-------------\n~listroles [requires Mod role or higher] = Lists all roles and their ID's.\n~roletester = Tests to see if the required roles thingy-mobabber works.\n \nModeration Commands\n-------------------\n~mute [Requires Mod role or higher] = Mutes a specified user.\n \nOther commands\n--------------\n~Calculator <add/subtract/multiply/divide> = A calculator, duh.\n~disconnect [Bot Owner Only] = Disconnects the bot.```")

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

bot.run('insert fucking token god dammit my bot was declined because of this haha jokes.')
