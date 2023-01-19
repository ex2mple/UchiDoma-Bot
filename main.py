import discord, requests, random
from discord.ext import commands
from discord import option

bot = discord.Bot(debug_guilds=['921377212500967444', ])


@bot.event
async def on_ready():
    print(f'Бот: {bot.user}\nСтатус: Онлайн')


@bot.slash_command()
async def ping(ctx):
    await ctx.respond(f'PONG!')


@bot.slash_command()
async def calc(ctx, instance):
    try:
        await ctx.respond(f'{instance} = {eval(instance)}')
    except SyntaxError:
        await ctx.respond('Ошибка ввода!')
    except ArithmeticError:
        await ctx.respond('Невозможно выполнить операцию!')

@bot.slash_command()
@option('count', default=1)
async def dice(ctx, count: int):
    if count == 1:
        side = random.randint(1, 6)
        await ctx.respond(f'Выпало число: {side} 🎲')
        return
    nums = [str(random.randint(1, 6)) for i in range(count)]
    await ctx.respond(f'Выпали числа: ' + ', '.join(nums))

@bot.slash_command()
async def cat(ctx):
    url = 'https://cataas.com/cat?json=true'
    response = requests.request("GET", url).json()
    await ctx.respond(f'https://cataas.com{response["url"]}')


bot.run('MTA2NTAwNTIyMTEzMjExMTk0Mw.GpxVOT.TXBUn74UtJcAuVGPlaXPUOcZ2lHmZ05hB2Xw1A')
